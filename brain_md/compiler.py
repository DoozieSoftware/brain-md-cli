"""TOON Compiler - Resolves @pointers and assembles payload."""

import re
from pathlib import Path

from brain_md.models import BrainConfig, CompileResult, CompileError, ResolvedPointer
from brain_md.parser import parse_toon
from brain_md.tokens import estimate_tokens


def compile_brain(source: Path) -> CompileResult:
    """
    Compile a brain.md file into a TOON payload.

    1. Parse the source file using TOON parser
    2. Extract configuration from KERNEL section
    3. Detect @pointer references
    4. Resolve and inject file contents as appendix
    5. Return CompileResult with metadata

    Args:
        source: Path to brain.md file

    Returns:
        CompileResult with payload, token count, and metadata

    Raises:
        CompileError: If compilation fails or pointers not found
    """
    content = source.read_text()
    base_dir = source.parent

    # Parse TOON content into BrainConfig
    parsed = parse_toon(content)

    # Extract sections from parsed content
    brain_config = BrainConfig(
        kernel=parsed.get("KERNEL", {}),
        registers=parsed.get("REGISTERS", {}),
        memory_pointers=parsed.get("MEMORY_POINTERS", []),
        process_stack=parsed.get("PROCESS_STACK", []),
        raw_content=content,
    )

    # Find all @pointer references (quoted strings starting with @)
    pointer_pattern = r'"@([^"]+)"'
    resolved_pointers: list[ResolvedPointer] = []

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
            file_content = "\n".join(lines[start - 1 : end])

        resolved_pointers.append(
            ResolvedPointer(
                original=f"@{pointer}", path=full_path, content=file_content.strip()
            )
        )
        return match.group(0)  # Keep original reference

    # Collect all pointers (keeps original content intact)
    re.sub(pointer_pattern, collect_pointer, content)

    # Build appendix with resolved file contents
    appendix = ""
    if resolved_pointers:
        appendix = "\n\n# RESOLVED_MEMORY\n"
        for rp in resolved_pointers:
            appendix += f"\n{rp.original}:\n>>>\n{rp.content}\n<<<\n"

    # Add driver prompt header
    driver = "SYSTEM RESET. FORMAT=TOON. `>>>` denotes raw file content. EXECUTE `PROCESS_STACK`.\n\n"

    # Assemble final payload
    payload = driver + content + appendix

    # Estimate token count
    token_count = estimate_tokens(payload)

    # Extract token budget from KERNEL if present
    token_budget = None
    if "token_budget" in brain_config.kernel:
        budget_value = brain_config.kernel["token_budget"]
        # Convert to int if it's a string
        if isinstance(budget_value, str):
            token_budget = int(budget_value)
        else:
            token_budget = budget_value

    return CompileResult(
        payload=payload,
        token_count=token_count,
        resolved_pointers=resolved_pointers,
        token_budget=token_budget,
    )


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
