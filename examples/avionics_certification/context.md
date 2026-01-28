# context.md - Live Session State
# Generated from brain.md by 'brain boot' command
# Created: 2026-01-28 23:48:20
#
# This is your live RAM - edit freely during the session.
# Changes are auto-compiled when using 'brain watch'.
#
# === KERNEL (AI Configuration) ===
KERNEL:
  role: "Senior Avionics Engineer"
  mode: "Analysis"
  token_budget: 2000

# === REGISTERS (Session Variables) ===
REGISTERS:
  certification_level: "DO-178C Level A"
  current_module: "Elevator Control Law"
  jira_ticket: "AV-1024"

# === MEMORY_POINTERS (External References) ===
MEMORY_POINTERS[3]{type, path, description}:
  "file", "@safety_requirements.req", "Safety Requirements"
  "file", "@traceability_matrix.csv", "Requirements Traceability"
  "file", "@derivation_rules.txt", "Derivation Rules"

# === PROCESS_STACK (Task Queue) ===
PROCESS_STACK[2]{priority, task}:
  "1", "Verify coverage of all safety requirements in the traceability matrix"
  "2", "Audit REQ-SAFE-003 against Derivation Rules for missing traceability"

# === SESSION_SCRATCHPAD (Live Notes) ===
# Edit this section freely during your session.
# Use it for brainstorming, notes, or temporary thoughts.

SESSION_SCRATCHPAD:
  session_notes: >-
    Phase 1 complete. Implementation frozen. Moving to Verification.

  todo_list:
    - "Sign off REQ-SAFE-001"
    - "Sign off REQ-SAFE-002"

  current_focus: >-
    Traceability Analysis

# === END OF CONTEXT ===
# To recompile: brain compile context.md
# To watch changes: brain watch context.md