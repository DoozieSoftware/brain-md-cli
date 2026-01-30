# context.md - Live Session State
# Generated from brain.md by 'brain boot' command
# Created: 2026-01-30 23:55:37
#
# This is your live RAM - edit freely during the session.
# Changes are auto-compiled when using 'brain watch'.
#
# === KERNEL (AI Configuration) ===
KERNEL:
  role: "Principal DBRE"
  mode: "Strict/Code-Only"
  token_budget: 4000

# === MEMORY_POINTERS (External References) ===
MEMORY_POINTERS[4]{type, path, description}:
  "file", "@schema_v1.sql", "Current Database Schema"
  "file", "@sharding_topology.yaml", "Cluster Topology Configuration"
  "file", "@query_patterns.log", "Recent Slow Query Logs"
  "file", "@migration_safety_checklist.md", "Migration Safety Rules"

# === PROCESS_STACK (Task Queue) ===
PROCESS_STACK[2]{priority, task}:
  "1", "Generate gh-ost migration scripts"
  "2", "Verify checksums"

# === SESSION_SCRATCHPAD (Live Notes) ===
# Edit this section freely during your session.
# Use it for brainstorming, notes, or temporary thoughts.

SESSION_SCRATCHPAD:
  session_notes: >-
    Analysis complete. Sharding key selected: 'id' (HASH).
    Moving to implementation phase.

  todo_list:
    - "First thing to do"
    - "Second thing to do"

  current_focus: >-
    Generating safe migration scripts.

# === END OF CONTEXT ===
# To recompile: brain compile context.md
# To watch changes: brain watch context.md
