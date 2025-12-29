"""Brain.md CLI - The Compiler Engine."""

import typer
from pathlib import Path
from rich.console import Console

from brain_md.compiler import compile_brain
from brain_md.tokens import estimate_tokens

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
        False, "--clipboard", "-c",
        help="Copy output to system clipboard",
    ),
    output: Path | None = typer.Option(
        None, "--output", "-o",
        help="Write output to file instead of stdout",
    ),
):
    """Compile brain.md into a token-optimized TOON payload."""
    if not source.exists():
        console.print(f"[red]✗ Source file not found:[/red] {source}")
        raise typer.Exit(1)

    try:
        payload = compile_brain(source)
        token_count = estimate_tokens(payload)

        if output:
            output.write_text(payload)
            console.print(f"[green]✔ Written to {output}[/green] ({token_count:,} tokens)")
        elif clipboard:
            import pyperclip
            pyperclip.copy(payload)
            console.print(f"[green]✔ Copied to clipboard[/green] ({token_count:,} tokens)")
        else:
            console.print(payload)
            console.print(f"\n[dim]({token_count:,} tokens)[/dim]", highlight=False)

    except Exception as e:
        console.print(f"[red]✗ Compilation failed:[/red] {e}")
        raise typer.Exit(1)


@app.command("version")
def version_cmd():
    """Show version information."""
    from brain_md import __version__
    console.print(f"brain-md v{__version__}")


if __name__ == "__main__":
    app()
