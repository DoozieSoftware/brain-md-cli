# Roadmap

> Strategic evolution of Brain.md from a CLI tool to a Context Operating System

## Vision

Evolve from a "Prompt Compiler" to the standard "BIOS" for AI interaction—where context is RAM, not history.

---

## Near-Term: The Workflow Engine

**Goal:** Remove all friction. Make "Context is RAM" feel like magic.

### Session State Management ✓
- `brain boot` & `context.md` with `SESSION_SCRATCHPAD`
- Live editing with auto-compile via `brain watch`
- Move from "compiling blueprints" to "managing live sessions"

### Surgical Memory
- **Partial Loading:** `@schema.sql:20-50` (Load lines 20-50 only)
- **Symbol Pointers:** `@auth.py#login` (Load function only)
- **Why:** Massive token savings—reference massive docs but load only what matters

### Model Context Protocol (MCP) Integration
- Local server that Claude Desktop, Cursor, and other tools can query directly
- "Hey Claude, load @brain" (no more manual pasting)
- Seamless integration with AI tools

### Recursive Brains
- Nested contexts: `MEMORY: - @backend_brain.md`
- Modular architecture for different project areas
- Change focus from Backend to Frontend with one line

---

## Mid-Term: The Feedback Loop

**Goal:** The AI participates in its own memory management (under supervision).

### Reverse Sync (The "Commit" Feature)
- `brain patch` command
- AI outputs `== UPDATE_BRAIN ==` block
- CLI prompts user: *"AI wants to mark Task 1 as DONE. Accept? (y/n)"*
- AI creates its own "save points" with approval

### Team Collaboration
- `shared_brain.md` (committed to Git) vs `local_brain.md` (user preferences)
- Teams define "Project Truth" (Stack, Rules)
- Individuals define their "Session Focus"

### Semantic Memory
- Vector-enhanced pointers: `@docs/** (query="authentication")`
- Search local vector store for relevant chunks
- Load only matching content
- Infinite context window simulation

---

## Long-Term: The Nonomous OS

**Goal:** A dedicated interface for AI orchestration.

### Desktop Application
- Native GUI (Electron/Rust)
- **Left Panel:** File tree & pointers
- **Center:** Live stack with drag-and-drop tasks
- **Right:** Real-time token budget gauge
- Drag files into window to load into RAM

### Multi-Brain Orchestration
- Multiple contexts simultaneously
  - **Context A:** Coder (Strict Rules)
  - **Context B:** Reviewer (Security Rules)
  - **Context C:** PM (Summary Rules)
- Pipe output of A into input of B automatically

---

## The "Anti-Roadmap"

To stay true to the **Nonomous Principle**, we will strictly avoid:

### Chat History Databases
- Never store conversation logs
- Context must be stateless
- Session = current state of file, not timeline

### Auto-Magic Agents
- User must always approve a context update
- No autonomous memory drift
- Human-in-the-loop always

### Proprietary Formats
- TOON remains open spec
- `brain.md` is just text
- No lock-in to vendor formats

---

## Current Status

**Latest Release:** v0.3.0 - Live Context Management

### Completed Features
- ✓ TOON Parser with tabular arrays, heredocs, comments
- ✓ Pointer resolution for external files
- ✓ Watch mode with auto-recompile
- ✓ Token budget enforcement
- ✓ Mode-specific driver prompts
- ✓ Session state management (`brain boot`)
- ✓ Live editing with `SESSION_SCRATCHPAD`

### In Progress
- Surgical memory (range pointers, symbol resolution)
- MCP server integration

### Planned
- Reverse sync and patching
- Team collaboration features
- Semantic memory with vector search
- Desktop GUI application
- Multi-brain orchestration

---

## Getting Involved

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines on contributing to the roadmap.

**Priority Areas:**
1. Workflow friction reduction
2. MCP integration for popular AI tools
3. Token optimization features
4. GUI for visual context management
