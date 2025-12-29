# Design Document: Brain.md CLI

## Overview

The Brain.md CLI is a command-line tool that compiles human-readable `brain.md` files into token-optimized TOON payloads for LLM context injection. The architecture follows a unidirectional data flow: Source → Compiler → Payload.

The tool is built with Python using Typer for CLI, tiktoken for token estimation, and watchdog for file monitoring.

## Architecture

```
┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│   brain.md      │────▶│    Compiler     │────▶│  context.toon   │
│   (Source)      │     │   (CLI Tool)    │     │   (Payload)     │
└─────────────────┘     └─────────────────┘     └─────────────────┘
        │                       │                       │
        │                       ▼                       │
        │               ┌───────────────┐               │
        └──────────────▶│   Resolver    │               │
          @pointers     │ (File Loader) │               │
                        └───────────────┘               │
                                │                       │
                                ▼                       ▼
                        ┌───────────────┐     ┌─────────────────┐
                        │   Heredoc     │────▶│   LLM Context   │
                        │   Injector    │     │    Window       │
                        └───────────────┘     └─────────────────┘
```

## Components and Interfaces

### 1. CLI Module (`cli.py`)

Entry point using Typer. Exposes commands:

```python
@app.command("compile")
def compile_cmd(
    source: Path,
    clipboard: bool = False,
    output: Path | None = None,
) -> None:
    """Compile brain.md into TOON payload."""

@app.command("watch")
def watch_cmd(
    source: Path,
) -> None:
    """Watch brain.md and referenced files for changes."""

@app.command("version")
def version_cmd() -> None:
    """Show version information."""
```

### 2. Compiler Module (`compiler.py`)

Core compilation logic:

```python
def compile_brain(source: Path) -> CompileResult:
    """
    Compile brain.md to TOON payload.
    
    Returns:
        CompileResult with payload string and metadata
    
    Raises:
        CompileError: If source not found or pointer resolution fails
        BudgetExceededError: If payload exceeds token_budget
    """

def parse_brain_file(content: str) -> BrainConfig:
    """Parse TOON content into structured config."""

def resolve_pointers(
    content: str, 
    base_dir: Path
) -> tuple[str, list[ResolvedPointer]]:
    """Find and resolve all @pointer references."""
```

### 3. Parser Module (`parser.py`)

TOON format parsing:

```python
def parse_toon(content: str) -> dict:
    """
    Parse TOON formatted content.
    
    Handles:
    - SECTION: headers
    - key: value pairs
    - SECTION[n]{keys}: tabular arrays
    - # comments
    """

def parse_tabular_array(header: str, rows: list[str]) -> list[dict]:
    """Parse tabular array into list of dicts."""
```

### 4. Pointer Module (`pointer.py`)

File reference resolution:

```python
def parse_pointer(pointer: str) -> PointerSpec:
    """
    Parse pointer string into path and optional line range.
    
    Examples:
        "@schema.sql" -> PointerSpec(path="schema.sql", range=None)
        "@schema.sql:20-50" -> PointerSpec(path="schema.sql", range=(20, 50))
    """

def resolve_pointer(spec: PointerSpec, base_dir: Path) -> str:
    """Load file content, applying line range if specified."""
```

### 5. Token Module (`tokens.py`)

Token estimation:

```python
def estimate_tokens(text: str, model: str = "gpt-4") -> int:
    """Estimate token count using tiktoken."""
```

### 6. Watcher Module (`watcher.py`)

File system monitoring:

```python
class BrainWatcher:
    """Watches brain.md and referenced files for changes."""
    
    def __init__(self, source: Path, on_change: Callable):
        """Initialize watcher with callback."""
    
    def start(self) -> None:
        """Start watching files."""
    
    def stop(self) -> None:
        """Stop watching files."""
```

## Data Models

```python
from dataclasses import dataclass
from pathlib import Path

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
    kernel: dict[str, str | int]
    registers: dict[str, str]
    memory_pointers: list[dict]
    process_stack: list[dict]
    raw_content: str

@dataclass
class CompileResult:
    """Compilation output."""
    payload: str
    token_count: int
    resolved_pointers: list[ResolvedPointer]
    token_budget: int | None
```

## Error Handling

### Exception Hierarchy

```python
class BrainError(Exception):
    """Base exception for brain-md."""

class CompileError(BrainError):
    """Compilation failed."""

class PointerError(CompileError):
    """Pointer resolution failed."""

class ParseError(CompileError):
    """TOON parsing failed."""

class BudgetExceededError(CompileError):
    """Payload exceeds token budget."""
    def __init__(self, actual: int, budget: int):
        self.actual = actual
        self.budget = budget
```

### Error Messages

| Error | Message Format |
|-------|----------------|
| Source not found | `✗ Source file not found: {path}` |
| Pointer not found | `✗ Pointer target not found: @{pointer} -> {resolved_path}` |
| Budget exceeded | `✗ Token budget exceeded: {actual:,} tokens (budget: {budget:,})` |
| Parse error | `✗ Parse error at line {line}: {message}` |


## Correctness Properties

*A property is a characteristic or behavior that should hold true across all valid executions of a system—essentially, a formal statement about what the system should do. Properties serve as the bridge between human-readable specifications and machine-verifiable correctness guarantees.*

### Property 1: Valid compilation produces output

*For any* valid Brain_File, compiling it SHALL produce a non-empty Payload string.

**Validates: Requirements 1.3**

### Property 2: Driver prompt invariant

*For any* compiled Payload, the output SHALL begin with the Driver_Prompt string.

**Validates: Requirements 1.4**

### Property 3: Pointer resolution correctness

*For any* Brain_File containing pointers and *for any* pointer `@path` where the target file exists, the Compiler SHALL resolve the path relative to the Brain_File's directory.

**Validates: Requirements 2.1**

### Property 4: Line range extraction

*For any* file with N lines and *for any* valid line range `start-end` where `1 <= start <= end <= N`, extracting that range SHALL return exactly `end - start + 1` lines matching the original file's lines at those positions.

**Validates: Requirements 2.4**

### Property 5: Resolved content format

*For any* Brain_File with pointers, the compiled Payload SHALL contain a `RESOLVED_MEMORY` section where each resolved file's content is wrapped in `>>>` and `<<<` heredoc delimiters.

**Validates: Requirements 2.3, 2.5**

### Property 6: File output correctness

*For any* valid Brain_File and *for any* valid output path, compiling with `--output` SHALL write a file whose content equals the Payload that would be sent to stdout.

**Validates: Requirements 4.1**

### Property 7: Budget enforcement

*For any* Brain_File with `token_budget: N` in KERNEL, IF the compiled Payload has more than N tokens THEN compilation SHALL fail with BudgetExceededError. IF the Payload has N or fewer tokens THEN compilation SHALL succeed. IF no budget is specified THEN compilation SHALL succeed regardless of token count.

**Validates: Requirements 5.1, 5.2, 5.3**

### Property 8: TOON section parsing

*For any* valid TOON content with KERNEL or REGISTERS sections containing key-value pairs, parsing SHALL produce a dictionary where each key maps to its corresponding value.

**Validates: Requirements 7.1, 7.2**

### Property 9: Tabular array parsing

*For any* valid tabular array header `SECTION[n]{key1, key2, ...}:` followed by n rows of comma-separated values, parsing SHALL produce a list of n dictionaries where each dictionary has keys matching the header and values from the corresponding row.

**Validates: Requirements 7.3**

### Property 10: Comment stripping

*For any* TOON content containing lines starting with `#`, parsing SHALL ignore those lines and they SHALL NOT appear in the parsed output or affect the resulting structure.

**Validates: Requirements 7.4**

## Testing Strategy

### Property-Based Testing

We use **pytest** with **hypothesis** for property-based testing. Each correctness property maps to one property test.

Configuration:
- Minimum 100 examples per property test
- Each test tagged with: `# Feature: brain-cli, Property N: <description>`

### Unit Tests

Unit tests complement property tests for:
- Specific examples demonstrating correct behavior
- Edge cases (empty files, missing pointers, malformed TOON)
- Error condition verification
- CLI integration points

### Test File Structure

```
tests/
├── test_compiler.py      # Property tests for compilation
├── test_parser.py        # Property tests for TOON parsing
├── test_pointer.py       # Property tests for pointer resolution
├── test_tokens.py        # Unit tests for token estimation
├── test_cli.py           # Integration tests for CLI commands
└── conftest.py           # Shared fixtures and generators
```

### Generators

Custom Hypothesis strategies for generating:
- Valid TOON content with random sections
- Valid Brain_File configurations
- Random file contents for pointer targets
- Valid and invalid line ranges
- Tabular arrays with varying column counts
