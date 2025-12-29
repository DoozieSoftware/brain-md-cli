"""Boot command - Creates context.md from brain.md."""

from pathlib import Path
from rich.console import Console

from brain_md.compiler import compile_brain
from brain_md.models import CompileError


def boot_cmd(source: Path = Path("brain.md")) -> None:
    """
    Initialize a session by creating context.md (Dashboard).

    This creates a live, editable context file from the source brain.md.
    The context.md serves as the working RAM during a session.

    Args:
        source: Path to brain.md source file (default: brain.md)
    """
    console = Console()

    if not source.exists():
        console.print(f"[red]✗ Source file not found:[/red] {source}")
        raise CompileError(f"Source file not found: {source}")

    try:
        # Read and parse source
        content = source.read_text()

        # Define context.md output path
        context_file = source.parent / "context.md"

        # Generate context.md content
        context_content = _generate_context_content(content)

        # Write context.md
        context_file.write_text(context_content)

        # Verify and show stats
        result = compile_brain(context_file)

        console.print(f"[green]✔ Session boot successful[/green]")
        console.print(f"   Source: {source}")
        console.print(f"   Context: {context_file}")
        console.print(f"   Tokens: {result.token_count:,}")
        console.print(f"   Pointers Resolved: {len(result.resolved_pointers)}")
        console.print(
            "\n[dim]💡 Tip: Run 'brain watch' to monitor context.md for live compilation[/dim]"
        )

    except CompileError as e:
        console.print(f"[red]✗ Boot failed:[/red] {e}")
        raise


def _generate_context_content(source_content: str) -> str:
    """
    Generate context.md content from brain.md source.

    The context.md includes:
    - All original TOON sections (KERNEL, REGISTERS, etc.)
    - New SESSION_SCRATCHPAD for live editing
    - Session metadata header

    Args:
        source_content: Content from brain.md

    Returns:
        Generated context.md content
    """
    import datetime

    # Parse source to extract sections
    from brain_md.parser import parse_toon

    parsed = parse_toon(source_content)

    # Build context.md
    lines = [
        "# context.md - Live Session State",
        "# Generated from brain.md by 'brain boot' command",
        f"# Created: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        "#",
        "# This is your live RAM - edit freely during the session.",
        "# Changes are auto-compiled when using 'brain watch'.",
        "#",
    ]

    # Add KERNEL section if exists
    if "KERNEL" in parsed:
        lines.append("# === KERNEL (AI Configuration) ===")
        kernel = parsed["KERNEL"]
        lines.append("KERNEL:")
        for key, value in kernel.items():
            if isinstance(value, str):
                lines.append(f'  {key}: "{value}"')
            else:
                lines.append(f"  {key}: {value}")
        lines.append("")

    # Add REGISTERS section if exists
    if "REGISTERS" in parsed:
        lines.append("# === REGISTERS (Session Variables) ===")
        registers = parsed["REGISTERS"]
        lines.append("REGISTERS:")
        for key, value in registers.items():
            lines.append(f'  {key}: "{value}"')
        lines.append("")

    # Add MEMORY_POINTERS section if exists
    if "MEMORY_POINTERS" in parsed:
        lines.append("# === MEMORY_POINTERS (External References) ===")
        pointers = parsed["MEMORY_POINTERS"]
        if pointers:
            # Get column headers from first item
            headers = list(pointers[0].keys())
            lines.append(f"MEMORY_POINTERS[{len(pointers)}]{{{', '.join(headers)}}}:")
            for row in pointers:
                values = [f'"{row.get(h, "")}"' for h in headers]
                lines.append(f"  {', '.join(values)}")
        lines.append("")

    # Add PROCESS_STACK section if exists
    if "PROCESS_STACK" in parsed:
        lines.append("# === PROCESS_STACK (Task Queue) ===")
        stack = parsed["PROCESS_STACK"]
        if stack:
            headers = list(stack[0].keys())
            lines.append(f"PROCESS_STACK[{len(stack)}]{{{', '.join(headers)}}}:")
            for row in stack:
                values = [f'"{row.get(h, "")}"' for h in headers]
                lines.append(f"  {', '.join(values)}")
        lines.append("")

    # Add SESSION_SCRATCHPAD (new interactive section)
    lines.append("# === SESSION_SCRATCHPAD (Live Notes) ===")
    lines.append("# Edit this section freely during your session.")
    lines.append("# Use it for brainstorming, notes, or temporary thoughts.")
    lines.append("")
    lines.append("SESSION_SCRATCHPAD:")
    lines.append("  session_notes: >-")
    lines.append("    Add your session notes here...")
    lines.append("")
    lines.append("  todo_list:")
    lines.append('    - "First thing to do"')
    lines.append('    - "Second thing to do"')
    lines.append("")
    lines.append("  current_focus: >-")
    lines.append("    What you're working on right now...")
    lines.append("")

    # Add footer
    lines.append("# === END OF CONTEXT ===")
    lines.append("# To recompile: brain compile context.md")
    lines.append("# To watch changes: brain watch context.md")

    return "\n".join(lines)
