"""Pointer resolution module for brain.md compiler."""

import re
from pathlib import Path
from brain_md.models import CompileError, ResolvedPointer


def parse_pointer(pointer: str) -> tuple[str, tuple[int, int] | None]:
    """
    Parse a pointer string into path and optional line range.

    Examples:
        "schema.sql" -> ("schema.sql", None)
        "schema.sql:20-50" -> ("schema.sql", (20, 50))
    """
    if ":" in pointer and "-" in pointer.split(":")[-1]:
        path, range_str = pointer.rsplit(":", 1)
        try:
            start, end = map(int, range_str.split("-"))
            return path, (start, end)
        except ValueError:
            pass

    return pointer, None


def resolve_pointer(pointer: str, base_dir: Path) -> ResolvedPointer:
    """
    Resolve a pointer reference to file content.

    Args:
        pointer: The pointer string (e.g., "@file.txt" or "@file.txt:20-50")
        base_dir: Base directory for resolving relative paths

    Returns:
        ResolvedPointer with original, path, and content

    Raises:
        CompileError: If pointer target file not found
    """
    file_path, line_range = parse_pointer(pointer)

    full_path = base_dir / file_path
    if not full_path.exists():
        raise CompileError(f"Pointer target not found: @{pointer} -> {full_path}")

    file_content = full_path.read_text()

    # Apply line range if specified
    if line_range:
        start, end = line_range
        lines = file_content.splitlines()
        file_content = "\n".join(lines[start - 1 : end])

    return ResolvedPointer(
        original=f"@{pointer}", path=full_path, content=file_content.strip()
    )


def extract_pointers(content: str) -> list[str]:
    """
    Extract all @pointer references from content.

    Args:
        content: The text content to search

    Returns:
        List of pointer strings (without @ prefix)
    """
    pointer_pattern = r'"@([^"]+)"'
    matches = re.finditer(pointer_pattern, content)
    return [m.group(1) for m in matches]
