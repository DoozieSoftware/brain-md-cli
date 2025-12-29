# TOON Specification v1.0
## Token-Oriented Object Notation

### 1. Purpose

TOON is a text format optimized for LLM context injection. It prioritizes:
- Minimal token usage
- High parser reliability
- Human readability

---

### 2. Syntax Rules

#### 2.1 Headers
Upper-case keys followed by colon. Defines a section.

```
KERNEL:
REGISTERS:
PROCESS_STACK:
```

#### 2.2 Key-Value Pairs
Indented under headers. Two-space indent required.

```
KERNEL:
  role: "Senior Architect"
  mode: "Strict/Code-Only"
  token_budget: 4000
```

#### 2.3 Tabular Arrays
High-density lists that define keys once in the header to save tokens.

Format: `SECTION_NAME[count]{key1, key2, ...}:`

```
MEMORY_POINTERS[2]{type, path, description}:
  file, "@agents.md", "Team Definitions"
  file, "@schema.sql", "Database Structure"
```

Equivalent JSON (for reference):
```json
{
  "MEMORY_POINTERS": [
    {"type": "file", "path": "@agents.md", "description": "Team Definitions"},
    {"type": "file", "path": "@schema.sql", "description": "Database Structure"}
  ]
}
```

#### 2.4 Pointers
Strings prefixed with `@` reference external files.

```
"@filename.ext"           # Full file
"@filename.ext:20-50"     # Lines 20-50 only
"@subdir/file.md"         # Relative path
```

#### 2.5 Heredocs
Raw text blocks delimited by `>>>` and `<<<`. No escaping required.

```
@schema.sql:
>>>
CREATE TABLE users (
    id SERIAL PRIMARY KEY
);
<<<
```

---

### 3. Reserved Sections

| Section | Purpose |
|---------|---------|
| `KERNEL:` | Core AI configuration (role, mode, constraints) |
| `REGISTERS:` | Session variables (paths, phase, state) |
| `MEMORY_POINTERS:` | External file references |
| `PROCESS_STACK:` | Prioritized task queue |
| `RESOLVED_MEMORY:` | Compiler-generated section with injected file contents |

---

### 4. Indentation

- Two spaces per level (no tabs)
- Tabular array rows are indented once under the header
- Heredoc content is NOT indented

---

### 5. Comments

Lines starting with `#` are comments (ignored by compiler).

```
# This is a comment
KERNEL:
  role: "Architect"  # Inline comments NOT supported
```

---

### 6. String Values

- Quoted strings: `"value with spaces"`
- Unquoted allowed for single words: `mode: strict`
- Pointers must be quoted: `"@file.md"`

---

### 7. Example Document

```yaml
# brain.md (TOON Format)

KERNEL:
  role: "Senior Architect"
  mode: "Strict/Code-Only"
  token_budget: 4000

REGISTERS:
  project_root: "./src"
  current_phase: "Migration"

MEMORY_POINTERS[2]{type, path, description}:
  file, "@agents.md", "Team Persona Definitions"
  file, "@schema.sql", "Database Structure"

PROCESS_STACK[3]{priority, task}:
  1, "Analyze Schema for Indexing"
  2, "Draft Migration Script"
  3, "Update Documentation"
```
