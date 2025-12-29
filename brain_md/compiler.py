"""TOON Compiler - Resolves @pointers and assembles payload."""

import re
from pathlib import Path


class CompileError(Exception):
    """Raised when compilation fails."""
    pass


def compile_brain(source: Path) -> str:
    """
    Compile a brain.md file into a TOON payload.
    
    1. Parse the source file
    2. Detect @pointer references
    3. Resolve and inject file contents as appendix
    4. Return assembled payload
    """
    content = source.read_text()
    base_dir = source.parent
    
    # Find all @pointer references (quoted strings starting with @)
    pointer_pattern = r'"@([^"]+)"'
    resolved_files: dict[str, str] = {}
    
    def collect_pointer(match: re.Match) -> str:
        pointer = match.group(1)
        file_path, line_range = parse_pointer(pointer)
        
        full_path = base_dir / file_path
        if not full_path.exists():
            raise CompileError(f"Pointer target not found: @{pointer} -> {full_path}")
        
        file_content = full_path.read_text()
        
        # Apply line range if specified
        if line_range:
            start, end = line_range
            lines = file_content.splitlines()
            file_content = "\n".join(lines[start - 1:end])
        
        resolved_files[pointer] = file_content.strip()
        return match.group(0)  # Keep original reference
    
    # Collect all pointers (keeps original content intact)
    re.sub(pointer_pattern, collect_pointer, content)
    
    # Build appendix with resolved file contents
    appendix = ""
    if resolved_files:
        appendix = "\n\n# RESOLVED_MEMORY\n"
        for pointer, file_content in resolved_files.items():
            appendix += f"\n@{pointer}:\n>>>\n{file_content}\n<<<\n"
    
    # Add driver prompt header
    driver = "SYSTEM RESET. FORMAT=TOON. `>>>` denotes raw file content. EXECUTE `PROCESS_STACK`.\n\n"
    
    return driver + content + appendix


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
