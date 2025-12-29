# Implementation Plan: Brain.md CLI

## Overview

Phased implementation following the PRD: Core tooling first (compile), then friction removal (watch), then optimization (line ranges, recursive brains).

## Tasks

- [x] 1. Project setup and core data models
  - [x] 1.1 Initialize Python package structure with pyproject.toml
    - Create `brain_md/` package with `__init__.py`
    - Configure dependencies: typer, rich, tiktoken, hypothesis
    - Set up `brain` CLI entrypoint
    - _Requirements: N/A (infrastructure)_
  - [x] 1.2 Implement data models in `models.py`
    - Create PointerSpec, ResolvedPointer, BrainConfig, CompileResult dataclasses
    - Create exception hierarchy: BrainError, CompileError, PointerError, ParseError, BudgetExceededError
    - _Requirements: 1.2, 2.2, 5.2_

- [ ] 2. TOON Parser implementation
  - [ ] 2.1 Implement basic TOON parser in `parser.py`
    - Parse SECTION: headers
    - Parse key: value pairs with two-space indentation
    - Strip # comments
    - _Requirements: 7.1, 7.2, 7.4, 7.5_
  - [ ] 2.2 Write property test for section parsing
    - **Property 8: TOON section parsing**
    - **Validates: Requirements 7.1, 7.2**
  - [ ] 2.3 Implement tabular array parsing
    - Parse SECTION[n]{keys}: header format
    - Parse comma-separated value rows
    - Return list of dictionaries
    - _Requirements: 7.3_
  - [ ] 2.4 Write property test for tabular array parsing
    - **Property 9: Tabular array parsing**
    - **Validates: Requirements 7.3**
  - [ ] 2.5 Write property test for comment stripping
    - **Property 10: Comment stripping**
    - **Validates: Requirements 7.4**

- [ ] 3. Pointer resolution
  - [ ] 3.1 Implement pointer parsing in `pointer.py`
    - Parse `@path` format
    - Parse `@path:start-end` line range format
    - Return PointerSpec dataclass
    - _Requirements: 2.1, 2.4_
  - [ ] 3.2 Write property test for line range extraction
    - **Property 4: Line range extraction**
    - **Validates: Requirements 2.4**
  - [ ] 3.3 Implement pointer resolution
    - Locate files relative to brain.md directory
    - Load file content
    - Apply line range if specified
    - Raise PointerError if file not found
    - _Requirements: 2.1, 2.2_
  - [ ] 3.4 Write property test for pointer resolution
    - **Property 3: Pointer resolution correctness**
    - **Validates: Requirements 2.1**

- [ ] 4. Checkpoint - Parser and pointer tests pass
  - Ensure all tests pass, ask the user if questions arise.

- [ ] 5. Core compiler
  - [ ] 5.1 Implement token estimation in `tokens.py`
    - Use tiktoken with cl100k_base encoding
    - Return integer token count
    - _Requirements: 1.5_
  - [ ] 5.2 Implement compiler in `compiler.py`
    - Read brain.md source file
    - Parse TOON content
    - Find and resolve all @pointers
    - Build RESOLVED_MEMORY section with heredoc-wrapped content
    - Prepend driver prompt
    - Return CompileResult with payload and token count
    - _Requirements: 1.1, 1.3, 1.4, 2.3, 2.5_
  - [ ] 5.3 Write property test for compilation output
    - **Property 1: Valid compilation produces output**
    - **Validates: Requirements 1.3**
  - [ ] 5.4 Write property test for driver prompt invariant
    - **Property 2: Driver prompt invariant**
    - **Validates: Requirements 1.4**
  - [ ] 5.5 Write property test for resolved content format
    - **Property 5: Resolved content format**
    - **Validates: Requirements 2.3, 2.5**

- [ ] 6. Token budget enforcement
  - [ ] 6.1 Implement budget checking in compiler
    - Extract token_budget from KERNEL section
    - Compare payload tokens against budget
    - Raise BudgetExceededError if exceeded
    - _Requirements: 5.1, 5.2, 5.3_
  - [ ] 6.2 Write property test for budget enforcement
    - **Property 7: Budget enforcement**
    - **Validates: Requirements 5.1, 5.2, 5.3**

- [ ] 7. Checkpoint - Compiler tests pass
  - Ensure all tests pass, ask the user if questions arise.

- [ ] 8. CLI implementation
  - [ ] 8.1 Implement `brain compile` command in `cli.py`
    - Accept source path argument
    - Call compiler and output to stdout
    - Display token count
    - Handle errors with rich formatting
    - _Requirements: 1.1, 1.2, 1.3, 1.5_
  - [ ] 8.2 Implement --clipboard flag
    - Copy payload to system clipboard using pyperclip
    - Display success message
    - Fall back to stdout on clipboard error
    - _Requirements: 3.1, 3.2, 3.3_
  - [ ] 8.3 Implement --output flag
    - Write payload to specified file path
    - Display success message with path and token count
    - _Requirements: 4.1, 4.2_
  - [ ] 8.4 Write property test for file output
    - **Property 6: File output correctness**
    - **Validates: Requirements 4.1**

- [ ] 9. Watch mode (Phase 3)
  - [ ] 9.1 Implement file watcher in `watcher.py`
    - Use watchdog to monitor brain.md
    - Extract pointer paths and monitor those files too
    - Trigger callback on any file change
    - _Requirements: 6.1, 6.2_
  - [ ] 9.2 Implement `brain watch` command
    - Start watcher daemon
    - On change: recompile and copy to clipboard
    - Display OS notification on success/failure
    - _Requirements: 6.3, 6.4, 6.5_

- [ ] 10. Final checkpoint
  - Ensure all tests pass, ask the user if questions arise.

## Notes

- All property tests are required for comprehensive coverage
- Phase 4 (surgical pointers, recursive brains) and Phase 5 (patching) are out of scope for MVP
- Line range support (`@file:20-50`) is included in pointer resolution (task 3.1)
