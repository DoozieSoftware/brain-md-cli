# context.md - Live Session State
# Generated from brain.md by 'brain boot' command
# Created: 2026-01-15 23:57:31
#
# This is your live RAM - edit freely during the session.
# Changes are auto-compiled when using 'brain watch'.
#
# === KERNEL (AI Configuration) ===
KERNEL:
  role: "Lead Backend Architect"
  mode: "Critical/Migration"
  token_budget: 8000

# === REGISTERS (Session Variables) ===
REGISTERS:
  project_root: "./src"
  current_phase: "Emergency-Rollback"

# === MEMORY_POINTERS (External References) ===
MEMORY_POINTERS[2]{type, path, description}:
  "file", "@legacy_ledger.java", "Source of Truth (Legacy)"
  "file", "@reconciliation_script.py", "Variance Detector"

# === PROCESS_STACK (Task Queue) ===
PROCESS_STACK[3]{priority, task}:
  "1", "Investigate Reconciliation Variance"
  "2", "Run Rollback Protocol"
  "3", "Notify Compliance Team"

# === SESSION_SCRATCHPAD (Live Notes) ===
# Edit this section freely during your session.
# Use it for brainstorming, notes, or temporary thoughts.

SESSION_SCRATCHPAD:
  session_notes: >-
    ALERT: The reconciliation script found a mismatch in the user balance table.
    We are aborting the migration immediately.

  todo_list:
    - "Check logs for double-write errors"
    - "Isolate the affected user IDs"

  current_focus: >-
    Analyzing the diff output from the Python script.

# === END OF CONTEXT ===
# To recompile: brain compile context.md
# To watch changes: brain watch context.md
