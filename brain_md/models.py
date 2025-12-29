"""Data models and exceptions for Brain.md CLI."""

from dataclasses import dataclass, field
from pathlib import Path


# =============================================================================
# Exception Hierarchy
# =============================================================================

class BrainError(Exception):
    """Base exception for brain-md."""
    pass


class CompileError(BrainError):
    """Compilation failed."""
    pass


class PointerError(CompileError):
    """Pointer resolution failed."""
    pass


class ParseError(CompileError):
    """TOON parsing failed."""
    pass


class BudgetExceededError(CompileError):
    """Payload exceeds token budget."""
    
    def __init__(self, actual: int, budget: int):
        self.actual = actual
        self.budget = budget
        super().__init__(
            f"Token budget exceeded: {actual:,} tokens (budget: {budget:,})"
        )


# =============================================================================
# Data Models
# =============================================================================

@dataclass
class PointerSpec:
    """Parsed pointer reference."""
    path: str
    line_range: tuple[int, int] | None = None


@dataclass
class ResolvedPointer:
    """Resolved pointer with content."""
    original: str      # "@schema.sql:20-50"
    path: Path         # Resolved absolute path
    content: str       # File content (with range applied)


@dataclass
class BrainConfig:
    """Parsed brain.md configuration."""
    kernel: dict[str, str | int] = field(default_factory=dict)
    registers: dict[str, str] = field(default_factory=dict)
    memory_pointers: list[dict] = field(default_factory=list)
    process_stack: list[dict] = field(default_factory=list)
    raw_content: str = ""


@dataclass
class CompileResult:
    """Compilation output."""
    payload: str
    token_count: int
    resolved_pointers: list[ResolvedPointer] = field(default_factory=list)
    token_budget: int | None = None
