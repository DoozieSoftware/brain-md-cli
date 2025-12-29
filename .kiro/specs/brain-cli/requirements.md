# Requirements Document

## Introduction

Brain.md is a Context Control Protocol for LLMs that replaces the standard chat history model with a stateless "RAM" model. The CLI tool (`brain-cli`) compiles a human-readable source file (`brain.md`) into a token-optimized payload (`context.toon`) for injection into AI context windows.

## Glossary

- **Brain_File**: The human-readable source file (`brain.md`) written in TOON format containing AI configuration, variables, and file pointers
- **Compiler**: The CLI engine that parses the Brain_File, resolves pointers, and assembles the payload
- **Payload**: The compiled output (`context.toon`) optimized for AI attention mechanisms
- **TOON**: Token-Oriented Object Notation - a text format optimized for minimal token usage
- **Pointer**: A string prefixed with `@` that references an external file (e.g., `"@schema.sql"`)
- **Heredoc**: Raw text block delimited by `>>>` and `<<<`
- **Driver_Prompt**: Standardized natural language prefix that teaches the AI how to interpret the TOON payload
- **Token_Budget**: Maximum allowed tokens for the compiled payload

## Requirements

### Requirement 1: Compile Brain File

**User Story:** As a developer, I want to compile my brain.md file into a TOON payload, so that I can inject consistent context into my AI sessions.

#### Acceptance Criteria

1. WHEN a user runs `brain compile <source>`, THE Compiler SHALL read the specified Brain_File
2. WHEN the Brain_File does not exist, THE Compiler SHALL display an error message and exit with non-zero status
3. WHEN the Brain_File is valid, THE Compiler SHALL output the compiled Payload to stdout
4. THE Compiler SHALL prepend the Driver_Prompt to every compiled Payload
5. WHEN compilation succeeds, THE Compiler SHALL display the estimated token count

### Requirement 2: Resolve Pointers

**User Story:** As a developer, I want to reference external files in my brain.md, so that I can include relevant code and documentation in my context.

#### Acceptance Criteria

1. WHEN the Compiler encounters a Pointer (string starting with `@`), THE Compiler SHALL locate the referenced file relative to the Brain_File directory
2. WHEN a Pointer target file does not exist, THE Compiler SHALL fail compilation with a descriptive error
3. THE Compiler SHALL wrap resolved file contents in Heredoc delimiters (`>>>` and `<<<`)
4. WHEN a Pointer includes a line range (e.g., `@file.sql:20-50`), THE Compiler SHALL extract only the specified lines
5. THE Compiler SHALL append all resolved file contents to a `RESOLVED_MEMORY` section in the Payload

### Requirement 3: Clipboard Integration

**User Story:** As a developer, I want to copy the compiled payload directly to my clipboard, so that I can quickly paste it into my AI interface.

#### Acceptance Criteria

1. WHEN a user runs `brain compile <source> --clipboard`, THE Compiler SHALL copy the Payload to the system clipboard
2. WHEN clipboard copy succeeds, THE Compiler SHALL display a success message with token count
3. WHEN clipboard copy fails, THE Compiler SHALL display an error and fall back to stdout output

### Requirement 4: File Output

**User Story:** As a developer, I want to save the compiled payload to a file, so that I can version control or reuse my context.

#### Acceptance Criteria

1. WHEN a user runs `brain compile <source> --output <path>`, THE Compiler SHALL write the Payload to the specified file
2. WHEN file write succeeds, THE Compiler SHALL display a success message with the file path and token count

### Requirement 5: Token Budget Enforcement

**User Story:** As a developer, I want to set a token budget in my brain.md, so that I can control API costs and stay within context limits.

#### Acceptance Criteria

1. WHEN the Brain_File contains `token_budget` in the KERNEL section, THE Compiler SHALL enforce this limit
2. WHEN the compiled Payload exceeds the Token_Budget, THE Compiler SHALL fail compilation with an error showing actual vs budget
3. WHEN no Token_Budget is specified, THE Compiler SHALL compile without budget enforcement

### Requirement 6: Watch Mode

**User Story:** As a developer, I want automatic recompilation when I save files, so that my context stays current without manual intervention.

#### Acceptance Criteria

1. WHEN a user runs `brain watch <source>`, THE Compiler SHALL monitor the Brain_File for changes
2. THE Compiler SHALL also monitor all files referenced by Pointers in the Brain_File
3. WHEN any monitored file changes, THE Compiler SHALL automatically recompile and copy to clipboard
4. WHEN recompilation succeeds, THE Compiler SHALL display an OS notification with token count
5. WHEN recompilation fails due to Token_Budget, THE Compiler SHALL display an error notification

### Requirement 7: TOON Parsing

**User Story:** As a developer, I want my brain.md parsed according to TOON spec, so that the format is consistent and predictable.

#### Acceptance Criteria

1. THE Compiler SHALL parse KERNEL section as key-value pairs
2. THE Compiler SHALL parse REGISTERS section as key-value pairs
3. THE Compiler SHALL parse tabular arrays with the format `SECTION[count]{keys}:`
4. THE Compiler SHALL treat lines starting with `#` as comments and ignore them
5. THE Compiler SHALL require two-space indentation for nested content
