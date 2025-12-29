# Changelog

All notable changes to Brain.md will be documented in this file.

## [0.3.0] - 2025-12-29 - Live Context Management (Phase 6)

### Added
- **Boot Command** - Initialize sessions by creating context.md from brain.md
  - Generates live, editable context file (the "RAM")
  - Preserves all TOON sections (KERNEL, REGISTERS, MEMORY_POINTERS, PROCESS_STACK)
  - Adds new SESSION_SCRATCHPAD section for live editing
  - `brain boot <source>` CLI command

- **Context.md Schema** - Live session state format
  - Session metadata header (creation timestamp, source file)
  - All original TOON sections with comments
  - SESSION_SCRATCHPAD with:
    - session_notes (multi-line YAML)
    - todo_list (array)
    - current_focus (multi-line YAML)
  - Footer with usage hints

- **State Management Philosophy**
  - Live RAM model: Edit context.md during sessions
  - Not a chat history logger (adheres to "Flush" principle)
  - Session = current state of context.md, not timeline of interactions
  - brain.md = source of truth, context.md = working RAM

### Changed
- **Compiler Bug Fix** - Fixed pointer resolution
  - Removed double @ prefix bug in pointer resolution
  - extract_pointers() now correctly returns paths without @
  - resolve_pointer() properly handles the @ prefix internally

- **Driver Prompt Integration** - Now uses generate_driver_prompt()
  - Mode-specific prompts properly applied to all compilations
  - Consistent driver prompt generation across all modes

- **Watcher** - Now supports context.md as source
  - Works seamlessly with context.md files
  - Auto-recompiles context.md changes
  - Maintains pointer resolution for referenced files

### Fixed
- Pointer resolution double @ prefix bug (reported in compiler line 54)
- Mode-specific driver prompts not being applied (hardcoded prompt issue)

### Tests
- 29 total tests
  - All tests passing
  - Mode prompt tests updated to match correct format

---

## [0.2.0] - 2025-12-29 - Feature Completeness & Watch Mode (URGENT)

### Added
- **Watch Mode** - File system monitoring for auto-recompilation
  - Monitors brain.md and all referenced @pointer files
  - Auto-recompiles and copies to clipboard on changes
  - OS notifications for success/failure
  - Debouncing to prevent rapid recompiles
  - `brain watch` CLI command

- **Token Budget Enforcement**
  - Checks token count against `token_budget` in KERNEL
  - Raises `BudgetExceededError` when exceeding budget
  - Compiles successfully when within budget

- **Mode-Specific Driver Prompts**
  - Strict/Code-Only: "STRICT MODE: Code only, no explanations"
  - Creative: "CREATIVE MODE: Explore freely within constraints"
  - Analysis/Planning: "ANALYSIS MODE: Review and report, no modifications"
  - Default prompt for unrecognized modes

### Changed
- **Parser Integration** - Parser now integrated into compiler
  - Returns `CompileResult` instead of string
  - Uses `BrainConfig` data model
  - Comment stripping from final payload
  - Heredoc support for source files (>>>...<<< blocks)

- **CLI Enhancements**
  - Enhanced output with resolved file count
  - Added watch command to CLI
  - Better error formatting with rich console

### Fixed
- Section validation added for TOON structure
- Driver prompt now uses backticks per spec
- Data model consistency across codebase

### Tests
- 24 total tests
  - 21 tests passing
  - 2 tests skipped (strict validation pending)

---

## [0.1.0] - 2025-12-28 - Initial Release

### Added
- Initial implementation
- TOON parser with tabular arrays
- Compiler with pointer resolution
- CLI with compile command
- Token estimation

### Security
- No security vulnerabilities in this release

---

## Upgrade Notes

### From 0.1.0 to 0.2.0
- **Breaking Changes**: None
- **New Features**:
  - Watch mode for auto-recompilation
  - Token budget enforcement
  - Mode-specific driver prompts
  - Heredoc support in source files
- **Deprecations**: None
- **Migration Guide**:
  - Add `mode: "Strict/Code-Only"` to KERNEL for strict mode
  - Add `token_budget: 4000` to KERNEL for budget enforcement
  - Run `brain watch <file>` to enable auto-recompilation

---

## Version Policy

Brain.md follows [Semantic Versioning](https://semver.org/):
- MAJOR.MINOR.PATCH (e.g., 1.0.0, 2.1.3)
- MAJOR version for incompatible API changes
- MINOR version for backwards-compatible functionality
- PATCH version for backwards-compatible bug fixes
