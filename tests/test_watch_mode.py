"""Tests for watch mode functionality."""

import pytest
import tempfile
import time
from pathlib import Path
from brain_md.watcher import BrainWatcher, BrainFileHandler


def test_file_handler_debounce():
    """Test that file handler debounces rapid changes."""
    callback_calls = []

    def mock_callback():
        callback_calls.append(time.time())

    handler = BrainFileHandler(mock_callback, debounce_seconds=0.1)

    # Simulate multiple rapid modifications
    handler.on_modified(
        type("Event", (), {"is_directory": False, "src_path": "/tmp/test.md"})
    )
    time.sleep(0.05)  # Within debounce time
    handler.on_modified(
        type("Event", (), {"is_directory": False, "src_path": "/tmp/test.md"})
    )

    # Wait for debounce
    handler.trigger_callback_if_pending()
    time.sleep(0.1)

    # Should have triggered callback
    assert len(callback_calls) == 1


def test_file_handler_ignores_temp_files():
    """Test that handler ignores temporary and cache files."""
    callback_calls = []

    def mock_callback():
        callback_calls.append(True)

    handler = BrainFileHandler(mock_callback)

    # Test .pyc file
    event = type("Event", (), {"is_directory": False, "src_path": "/tmp/test.pyc"})
    handler.on_modified(event)
    handler.trigger_callback_if_pending()

    assert len(callback_calls) == 0

    # Test .pyo file
    event = type("Event", (), {"is_directory": False, "src_path": "/tmp/test.pyo"})
    handler.on_modified(event)
    handler.trigger_callback_if_pending()

    assert len(callback_calls) == 0

    # Test __pycache__
    event = type(
        "Event", (), {"is_directory": False, "src_path": "/tmp/__pycache__/test.py"}
    )
    handler.on_modified(event)
    handler.trigger_callback_if_pending()

    assert len(callback_calls) == 0


def test_watcher_extracts_pointers():
    """Test that watcher extracts @pointers from content."""
    with tempfile.TemporaryDirectory() as tmpdir:
        brain_file = Path(tmpdir) / "brain.md"

        content = """
        KERNEL:
          role: "Test"
        
        MEMORY_POINTERS[2]{type, path, description}:
          file, "@file1.txt", "File 1"
          file, "@file2.txt", "File 2"
        """

        brain_file.write_text(content)

        watcher = BrainWatcher(brain_file, lambda _: None)
        pointers = watcher._extract_pointers(content)

        assert len(pointers) == 2
        # Pointers are extracted without @ prefix
        assert "file1.txt" in pointers[0]
        assert "file2.txt" in pointers[1]


def test_watcher_gets_watched_paths():
    """Test that watcher returns correct paths to watch."""
    with tempfile.TemporaryDirectory() as tmpdir:
        brain_file = Path(tmpdir) / "brain.md"
        ref_file1 = Path(tmpdir) / "ref1.txt"
        ref_file2 = Path(tmpdir) / "ref2.txt"

        brain_file.write_text("""
        KERNEL:
          role: "Test"
        
        MEMORY_POINTERS[2]{type, path, description}:
          file, "@ref1.txt", "Reference 1"
          file, "@ref2.txt", "Reference 2"
        """)

        ref_file1.write_text("Content 1")
        ref_file2.write_text("Content 2")

        watcher = BrainWatcher(brain_file, lambda _: None)
        watched = watcher._get_watched_paths()

        # Should watch brain.md and both referenced files
        assert len(watched) == 3
        # Check paths exist in watched list (macOS adds /private prefix)
        # Use resolve() to normalize paths
        watched_resolved = [p.resolve() for p in watched]
        assert brain_file.resolve() in watched_resolved
        assert ref_file1.resolve() in watched_resolved
        assert ref_file2.resolve() in watched_resolved


def test_watcher_compile_and_notify():
    """Test that watcher compiles and sends notifications."""
    notifications = []

    def mock_notification(title: str, message: str):
        notifications.append((title, message))

    with tempfile.TemporaryDirectory() as tmpdir:
        brain_file = Path(tmpdir) / "brain.md"

        brain_file.write_text("""
        KERNEL:
          role: "Test"
        """)

        watcher = BrainWatcher(
            brain_file, lambda _: None, notification_callback=mock_notification
        )

        # Compile
        success = watcher.compile_and_notify(output_to_clipboard=False)

        assert success is True
        assert len(notifications) == 1
        assert "Brain.md compiled" in notifications[0][0]


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
