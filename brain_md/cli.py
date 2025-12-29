"""Brain.md CLI - The Compiler Engine."""

import typer
from pathlib import Path
from rich.console import Console

from brain_md.compiler import compile_brain
from brain_md.boot import boot_cmd as boot_cmd_func
from brain_md.watcher import BrainWatcher

app = typer.Typer(
    name="brain",
    help="Context Control Protocol for LLMs",
    no_args_is_help=True,
    add_completion=False,
)
console = Console()


@app.command("compile")
def compile_cmd(
    source: Path = typer.Argument(
        Path("brain.md"),
        help="Path to brain.md source file",
    ),
    clipboard: bool = typer.Option(
        False,
        "--clipboard",
        "-c",
        help="Copy output to system clipboard",
    ),
    output: Path | None = typer.Option(
        None,
        "--output",
        "-o",
        help="Write output to file instead of stdout",
    ),
):
    """Compile brain.md into a token-optimized TOON payload."""
    if not source.exists():
        console.print(f"[red]✗ Source file not found:[/red] {source}")
        raise typer.Exit(1)

    try:
        result = compile_brain(source)

        payload = result.payload
        token_count = result.token_count
        resolved_count = len(result.resolved_pointers)

        if output:
            output.write_text(payload)
            console.print(
                f"[green]✔ Written to {output}[/green] ({token_count:,} tokens, {resolved_count} files resolved)"
            )
        elif clipboard:
            import pyperclip

            pyperclip.copy(payload)
            console.print(
                f"[green]✔ Copied to clipboard[/green] ({token_count:,} tokens, {resolved_count} files resolved)"
            )
        else:
            console.print(payload)
            console.print(
                f"\n[dim]({token_count:,} tokens, {resolved_count} files resolved)[/dim]",
                highlight=False,
            )

    except Exception as e:
        console.print(f"[red]✗ Compilation failed:[/red] {e}")
        raise typer.Exit(1)


@app.command("boot")
def boot_cmd(
    source: Path = typer.Argument(
        Path("brain.md"),
        help="Path to brain.md source file",
    ),
):
    """Initialize a session by creating context.md (Dashboard)."""
    boot_cmd_func(source)


@app.command("flush")
def flush_cmd(
    source: Path = typer.Argument(
        Path("brain.md"),
        help="Flush context stack - mark tasks/notes/registers as complete",
    ),
    pointers: bool = typer.Option(
        False,
        "--pointers",
        "-p",
        help="Clear all pointer contexts (LIFO order)",
    ),
    notes: bool = typer.Option(
        False,
        "--notes",
        "-n",
        help="Clear all note entries",
    ),
    registers: bool = typer.Option(
        False,
        "--registers",
        "-r",
        help="Clear all registers",
    ),
    all: bool = typer.Option(
        False,
        "--all",
        "-a",
        help="Flush everything (stack + all entries)",
    ),
    force: bool = typer.Option(
        False,
        "--force",
        "-f",
        help="Force flush even if stack is empty",
    ),
):
    """Flush context stack - mark tasks/notes/registers as complete."""
    if not source.exists():
        console.print(f"[red]✗ Source file not found:[/red] {source}")
        raise typer.Exit(1)

    console.print("[yellow]⚠ Flush command not yet implemented[/yellow]")
    console.print("[dim]This will be available in v0.4.0[/dim]")


@app.command("watch")
def watch_cmd(
    source: Path = typer.Argument(
        Path("brain.md"),
        help="Path to brain.md source file",
    ),
):
    """Watch brain.md and referenced files for changes, auto-recompiling."""
    if not source.exists():
        console.print(f"[red]✗ Source file not found:[/red] {source}")
        raise typer.Exit(1)

    console.print(f"[cyan]👀 Watching {source}...[/cyan]")
    console.print("[dim]Press Ctrl+C to stop[/dim]\n")

    def on_notification(title: str, message: str):
        """Handle notifications during watch mode."""
        if "failed" in title.lower():
            console.print(f"[red]✗ {title}:[/red] {message}")
        else:
            console.print(f"[green]✔ {title}:[/green] {message}")

    def on_change(source_path: Path):
        """Callback when files change."""
        # Compile and auto-copy to clipboard
        watcher.compile_and_notify(output_to_clipboard=True)

    # Create and start watcher
    watcher = BrainWatcher(
        source=source,
        on_change=on_change,
        notification_callback=on_notification,
    )

    try:
        watcher.start()
        # Initial compilation
        watcher.compile_and_notify(output_to_clipboard=True)

        # Keep running until interrupted
        import signal
        import sys

        def signal_handler(sig, frame):
            console.print("\n[dim]Stopping watcher...[/dim]")
            watcher.stop()
            sys.exit(0)

        signal.signal(signal.SIGINT, signal_handler)
        signal.pause()

    except Exception as e:
        console.print(f"[red]✗ Watcher error:[/red] {e}")
        raise typer.Exit(1)


if __name__ == "__main__":
    app()
