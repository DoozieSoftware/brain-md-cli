# Brain.md

> Context Control Protocol for LLMs - Stateless RAM Model

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://img.shields.io/badge/python-3.10+-blue.svg)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](https://img.shields.io/badge/license-MIT-green.svg))
[![Version: 0.3.0](https://img.shields.io/badge/version-0.3.0-blue.svg)](https://img.shields.io/badge/version-0.3.0-blue.svg)
[![Documentation](https://img.shields.io/badge/docs-latest-brightgreen.svg)](https://akshaydoozie.github.io/brain-md/)

Brain.md is a CLI tool that compiles human-readable `brain.md` files into token-optimized TOON (Token-Oriented Object Notation) payloads for injection into Large Language Model (LLM) context windows.

## Features

- **TOON Parser**: Full-featured parser supporting sections, key-value pairs, tabular arrays, and heredocs
- **Pointer Resolution**: Automatically resolves and injects external file references
- **Live Context Management**: `brain boot` creates editable context.md for session state
- **Watch Mode**: Auto-recompiles on file changes with debouncing and OS notifications
- **Token Budget Enforcement**: Ensures payloads stay within specified token limits
- **Mode-Specific Prompts**: Supports Strict, Creative, and Analysis driver prompt modes
- **Comment Stripping**: Removes comments from final payload while preserving in source files
- **State, Not History**: Manages live RAM state (context.md), not chat history

## Installation

```bash
# Install in development mode (includes testing tools)
pip install -e ".[dev]"

# Install for production use only
pip install -e brain-md
```

## Quick Start

```bash
# Create a brain.md file
cat > brain.md <<'EOF'
KERNEL:
  role: "Senior Developer"
  mode: "Strict/Code-Only"
  token_budget: 4000

MEMORY_POINTERS[1]{type, path, description}:
  file, "@schema.sql", "Database schema"

PROCESS_STACK[1]{priority, task}:
  1, "Optimize database queries"
EOF'

# Create a reference file
echo "CREATE TABLE users (id INT PRIMARY KEY);" > schema.sql

# Boot a session (creates context.md with SESSION_SCRATCHPAD)
brain boot brain.md

# Watch for changes (auto-compiles context.md to clipboard)
brain watch context.md

# Or compile directly
brain compile brain.md --clipboard
```

## Commands

### brain boot

Initialize a session by creating `context.md` from `brain.md`.

```bash
# Usage
brain boot <source>

# Features
- Creates live, editable context.md file
- Preserves all TOON sections (KERNEL, REGISTERS, MEMORY_POINTERS, PROCESS_STACK)
- Adds SESSION_SCRATCHPAD for live session notes
- Generates session metadata (timestamp, source file)
- Works seamlessly with watch mode
```

**Example**:

```bash
# Boot a session
brain boot brain.md

# Output
✔ Session boot successful
   Source: brain.md
   Context: context.md
   Tokens: 360
   Pointers Resolved: 2

💡 Tip: Run 'brain watch' to monitor context.md for live compilation
```

**context.md Structure**:

```yaml
# context.md - Live Session State
# Generated from brain.md by 'brain boot' command

# === KERNEL (AI Configuration) ===
KERNEL:
  role: "Senior Developer"
  mode: "Strict/Code-Only"

# === REGISTERS (Session Variables) ===
REGISTERS:
  project: "my-project"

# === MEMORY_POINTERS (External References) ===
MEMORY_POINTERS[1]{type, path}:
  file, "@schema.sql"

# === PROCESS_STACK (Task Queue) ===
PROCESS_STACK[1]{priority, task}:
  1, "Initial task"

# === SESSION_SCRATCHPAD (Live Notes) ===
SESSION_SCRATCHPAD:
  session_notes: >-
    Add your session notes here...

  todo_list:
    - "First thing to do"

  current_focus: >-
    What you're working on right now...
```

### brain compile

Compiles a brain.md file into a token-optimized TOON payload.

```bash
# Usage
brain compile <source> [OPTIONS]

# Options
--clipboard, -c          Copy output to system clipboard
--output, -o <path>      Write output to file instead of stdout
```

**Examples**:

```bash
# Compile to clipboard (default: stdout)
brain compile brain.md

# Compile to clipboard and show token count
brain compile brain.md --clipboard

# Compile to file
brain compile brain.md --output context.toon
```

### brain watch

Watches brain.md and all referenced @pointer files for changes, auto-recompiling and copying to clipboard.

```bash
# Usage
brain watch <source>

# Features
- Monitors brain.md and all referenced files
- Auto-recompiles on any file change
- Copies to clipboard on recompile
- Sends OS notifications for success/failure
- 0.5s debounce to prevent rapid recompiles
- Press Ctrl+C to stop watching
```

**Example**:

```bash
# Watch for changes (auto-copies to clipboard)
brain watch brain.md

# Start watching and initial compilation
👀 Watching examples/brain.md...
Press Ctrl+C to stop

✔ Brain.md compiled: 298 tokens, 2 files resolved
```

### brain version

Shows the current Brain.md version.

```bash
brain version
```

## TOON Format

Brain.md uses TOON (Token-Oriented Object Notation), a text format optimized for minimal token usage while maintaining human readability.

### Sections

```yaml
KERNEL:
  role: "Senior Developer"
  mode: "Strict/Code-Only"
  token_budget: 4000

REGISTERS:
  project_root: "./src"
  current_phase: "Development"

MEMORY_POINTERS[2]{type, path, description}:
  file, "@schema.sql", "Database Structure"
  file, "@api.py", "API endpoints"

PROCESS_STACK[3]{priority, task}:
  1, "Analyze schema for indexing"
  2, "Draft migration script"
  3, "Update documentation"
```

### Tabular Arrays

High-density lists that define keys once to save tokens:

```yaml
MEMORY_POINTERS[2]{type, path, description}:
  file, "@schema.sql", "Database schema"
  file, "@api.py", "API endpoints"
```

Equivalent JSON:

```json
{
  "MEMORY_POINTERS": [
    {"type": "file", "path": "@schema.sql", "description": "Database Structure"},
    {"type": "file", "path": "@api.py", "description": "API endpoints"}
  ]
}
```

### Pointers

Reference external files using `@` prefix:

```yaml
MEMORY_POINTERS[1]{type, path, description}:
  file, "@config.py", "Configuration file"
```

With line ranges:

```yaml
MEMORY_POINTERS[1]{type, path, description}:
  file, "@app.py:10-50", "Main application file"
```

### Heredocs

Raw text blocks for code, SQL, or other formatted content:

```yaml
>>>
CREATE TABLE users (
    id INT PRIMARY KEY,
    name TEXT NOT NULL
);
<<<
```

### Comments

Lines starting with `#` are comments and are stripped from the final compiled payload, but preserved in the source file for editing.

```yaml
# This is a comment and will be stripped from compiled output
KERNEL:
  role: "Developer"

REGISTERS:
  # Inline comments are preserved
  key: "value with comment"  # This comment stays
```

### Driver Prompts

Brain.md automatically generates mode-specific driver prompts based on the `mode` value in the KERNEL section:

| Mode | Driver Prompt |
|------|---------------|
| `strict` or `code-only` | `SYSTEM RESET. FORMAT=TOON. STRICT MODE: Code only, no explanations. \`>>>` denotes raw file. EXECUTE \`PROCESS_STACK\`.` |
| `creative` | `SYSTEM RESET. FORMAT=TOON. CREATIVE MODE: Explore freely within constraints. \`>>>` denotes raw file. EXECUTE \`PROCESS_STACK\`.` |
| `analysis` or `planning` | `SYSTEM RESET. FORMAT=TOON. ANALYSIS MODE: Review and report, no modifications. \`>>>` denotes raw file. EXECUTE \`PROCESS_STACK\`.` |
| Other (default) | `SYSTEM RESET. FORMAT=TOON. \`>>>` denotes raw file content. EXECUTE \`PROCESS_STACK\`.` |

## Configuration

### Token Budget

Enforce a maximum token count for the compiled payload:

```yaml
KERNEL:
  role: "Developer"
  token_budget: 4000
```

If the compiled payload exceeds the token budget, compilation will fail with a `BudgetExceededError` showing the actual and budgeted token counts.

### Modes

Control how the AI should interpret the TOON payload:

| Mode | Behavior |
|------|----------|
| `Strict/Code-Only` | Generate code only, no explanations or comments |
| `Creative` | Explore freely within constraints, ask follow-up questions |
| `Analysis/Planning` | Review and report, do not modify anything |
| Default | Standard interpretation |

## Advanced Usage

### Token Budget Enforcement

```yaml
KERNEL:
  role: "Developer"
  token_budget: 1000
```

```bash
# This will fail if compiled payload exceeds 1000 tokens
brain compile brain.md
```

### Mode-Specific Prompts

```yaml
KERNEL:
  role: "Developer"
  mode: "Strict/Code-Only"
```

```bash
# Generates strict mode driver prompt
brain compile brain.md
```

```yaml
KERNEL:
  role: "Designer"
  mode: "Creative"
```

```bash
# Generates creative mode driver prompt
brain compile brain.md
```

### Multiple Pointers with Line Ranges

```yaml
MEMORY_POINTERS[2]{type, path, description}:
  file, "@schema.sql:1-100", "Schema definition"
  file, "@main.py:50-100", "Main function"
```

### Heredoc Content

```yaml
MEMORY_POINTERS[1]{type, path, description}:
  file, "@query.sql", "SQL query"
```

**query.sql**:
```sql
>>>
SELECT users.name, orders.total
FROM users
JOIN orders ON users.id = orders.user_id
<<<
```

## Troubleshooting

### Compilation Errors

**Pointer not found**:
```
✗ Compilation failed: Pointer target not found: @missing-file.md -> /path/to/file
```
**Solution**: Ensure the referenced file exists relative to brain.md

**Token budget exceeded**:
```
✗ Compilation failed: Token budget exceeded: 1500 tokens (budget: 1000)
```
**Solution**: Reduce content or increase token budget

### Watch Mode Issues

**File not being watched**:
```yaml
# Ensure referenced files are in the same directory or use absolute paths
MEMORY_POINTERS[1]{type, path, description}:
  file, "/absolute/path/to/file.txt", "Reference"
```

**Rapid recompilation**:
- The watcher uses 0.5s debounce to prevent rapid recompiles
- If you're still seeing rapid recompiles, the files may be changing very frequently
- Consider increasing the debounce time in the source code

## Development

### Setting Up Development Environment

```bash
# Clone repository
git clone https://github.com/[username]/brain-md.git
cd brain-md

# Create virtual environment
python -m venv .venv
source .venv/bin/activate

# Install development dependencies
pip install -e ".[dev]"

# Verify installation
brain --version
```

### Running Tests

```bash
# Run all tests
pytest tests/

# Run tests with coverage
pytest --cov=brain_md --cov-report=html

# Run specific test file
pytest tests/test_compiler.py

# Run property-based tests (requires Hypothesis)
pytest tests/properties/test_compiler_properties.py -v
```

### Project Structure

```
brain-md/
├── brain_md/
│   ├── __init__.py
│   ├── cli.py              # CLI entry point
│   ├── compiler.py          # Core compilation logic
│   ├── boot.py             # Session initialization (creates context.md)
│   ├── parser.py           # TOON format parser
│   ├── pointer.py          # Pointer resolution
│   ├── watcher.py          # File system monitoring
│   ├── tokens.py           # Token estimation
│   └── models.py           # Data models
├── docs/                   # Sphinx documentation
├── spec/                   # Format specifications
├── examples/               # Example brain.md files
└── templates/              # Starter templates
```

## Contributing

Contributions are welcome! Please read [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## Changelog

See [CHANGELOG.md](CHANGELOG.md) for version history and changes.

## License

This project is licensed under the MIT License - see [LICENSE](LICENSE) file for details.

## Links

- [Documentation](https://dooziesoftware.github.io/brain-md-cli/)
- [Roadmap](ROADMAP.md)
- [TOON Specification](spec/TOON_SPEC_v1.0.md)
- [Driver Prompt Specification](spec/DRIVER_PROMPT.md)
- [Contributing Guidelines](CONTRIBUTING.md)
- [GitHub Issues](https://github.com/DoozieSoftware/brain-md-cli/issues)

## Acknowledgments

Brain.md is built with:
- [typer](https://typer.tiangolo.com/) - CLI framework
- [rich](https://rich.readthedocs.io/) - Terminal formatting
- [tiktoken](https://github.com/openai/tiktoken) - Token estimation
- [watchdog](https://python-watchdog.readthedocs.io/) - File system monitoring
- [pyperclip](https://pyperclip.readthedocs.io/) - Clipboard access
- [Hypothesis](https://hypothesis.readthedocs.io/) - Property-based testing
- [pytest](https://docs.pytest.org/) - Testing framework
