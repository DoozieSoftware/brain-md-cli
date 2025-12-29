"""File watcher for automatic recompilation."""

import os
import re
import threading
import time
from pathlib import Path
from typing import Callable, Optional

from brain_md.compiler import compile_brain
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class BrainFileHandler(FileSystemEventHandler):
    """Handler for file modification events."""

    def __init__(self, callback: Callable[[], None], debounce_seconds: float = 0.5):
        """
        Initialize file handler.

        Args:
            callback: Function to call when file changes
            debounce_seconds: Minimum time between callbacks
        """
        super().__init__()
        self.callback = callback
        self.debounce_seconds = debounce_seconds
        self.last_call = 0.0
        self.pending_changes = False
        self._lock = threading.Lock()

    def on_modified(self, event):
        """Handle file modification events."""
        if event.is_directory:
            return

        # Ignore temporary files and __pycache__
        src_path_str = str(event.src_path)
        if (
            src_path_str.endswith(".pyc")
            or src_path_str.endswith(".pyo")
            or "__pycache__" in src_path_str
        ):
            return

        # Mark that we have a pending change
        with self._lock:
            self.pending_changes = True

    def trigger_callback_if_pending(self):
        """Trigger callback if there are pending changes and debounce time has passed."""
        with self._lock:
            current_time = time.time()
            if (
                self.pending_changes
                and (current_time - self.last_call) >= self.debounce_seconds
            ):
                self.pending_changes = False
                self.last_call = current_time
                try:
                    self.callback()
                except Exception:
                    pass


class BrainWatcher:
    """Watches brain.md and referenced files for changes."""

    def __init__(
        self,
        source: Path,
        on_change: Callable[[Path], None],
        notification_callback: Optional[Callable[[str, str], None]] = None,
    ):
        """
        Initialize brain watcher.

        Args:
            source: Path to brain.md file
            on_change: Callback when any file changes, receives source path
            notification_callback: Callback for OS notifications (title, message)
        """
        self.source = source.resolve()
        self.base_dir = self.source.parent
        self.on_change = on_change
        self.notification_callback = notification_callback
        self.observer: Optional[Observer] = None
        self.watched_paths: list[Path] = []
        self.file_handler: Optional[BrainFileHandler] = None

        # Notification support is optional
        self._notify_available = False
        try:
            import plyer

            self._plyer = plyer
            self._notify_available = True
        except ImportError:
            self._notify_available = False

    def _extract_pointers(self, content: str) -> list[str]:
        """Extract @pointer references from content."""
        pointer_pattern = r'"@([^"]+)"'
        matches = re.finditer(pointer_pattern, content)
        return [m.group(1) for m in matches]

    def _get_watched_paths(self) -> list[Path]:
        """Get all paths that should be watched."""
        watched = [self.source]

        # Read brain.md to find pointers
        try:
            content = self.source.read_text()
            pointers = self._extract_pointers(content)

            # Add each pointer file to watched list
            for pointer in pointers:
                # Handle line ranges: file.txt:10-20
                if ":" in pointer:
                    path = pointer.split(":")[0]
                else:
                    path = pointer

                file_path = (self.base_dir / path).resolve()
                if file_path.exists() and file_path not in watched:
                    watched.append(file_path)
        except Exception:
            pass  # If we can't read brain.md, just watch it

        return watched

    def _notify(self, title: str, message: str):
        """Send OS notification if available."""
        if self.notification_callback:
            self.notification_callback(title, message)
        elif self._notify_available:
            try:
                self._plyer.notify(title=title, message=message, app_name="Brain.md")
            except Exception:
                pass

    def start(self):
        """Start watching files."""
        if self.observer is not None and self.observer.is_alive():
            return  # Already running

        # Get all paths to watch
        self.watched_paths = self._get_watched_paths()

        # Create file handler with debounce
        def on_change():
            # Re-read pointers in case they changed
            new_watched = self._get_watched_paths()

            # If new files to watch, restart observer
            if set(new_watched) != set(self.watched_paths):
                self.stop()
                self.watched_paths = new_watched
                self._start_observer()
                return

            # Trigger callback
            self.on_change(self.source)

        self.file_handler = BrainFileHandler(on_change)

        # Start observer
        self._start_observer()

        # Start debounce timer to check for pending changes
        self._debounce_thread = threading.Thread(
            target=self._debounce_loop, daemon=True
        )
        self._debounce_thread.start()

    def _start_observer(self):
        """Start or restart the watchdog observer."""
        if self.observer is not None:
            self.observer.stop()

        self.observer = Observer()

        # Watch each file's directory
        watched_dirs = set()
        for path in self.watched_paths:
            watched_dirs.add(str(path.parent))

        for watch_dir in watched_dirs:
            self.observer.schedule(self.file_handler, watch_dir, recursive=False)

        self.observer.start()

    def _debounce_loop(self):
        """Background thread to trigger callback on pending changes."""
        while self.observer is not None and self.observer.is_alive():
            time.sleep(0.1)
            if self.file_handler is not None:
                self.file_handler.trigger_callback_if_pending()

    def stop(self):
        """Stop watching files."""
        if self.observer is not None:
            self.observer.stop()
            self.observer.join()
            self.observer = None

        self.watched_paths = []

    def compile_and_notify(self, output_to_clipboard: bool = True) -> bool:
        """
        Compile brain.md and send notification.

        Args:
            output_to_clipboard: If True, copy to clipboard

        Returns:
            True if compilation succeeded, False otherwise
        """
        try:
            result = compile_brain(self.source)

            # Copy to clipboard if requested
            if output_to_clipboard:
                import pyperclip

                pyperclip.copy(result.payload)

            # Send success notification
            self._notify(
                title="Brain.md compiled",
                message=f"{result.token_count:,} tokens, {len(result.resolved_pointers)} files resolved",
            )

            return True
        except Exception as e:
            # Send error notification
            self._notify(title="Compilation failed", message=str(e))
            return False
