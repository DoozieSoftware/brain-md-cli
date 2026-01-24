# context.md - Live Session State
# Generated from brain.md by 'brain boot' command
# Created: 2026-01-24 23:46:26
#
# This is your live RAM - edit freely during the session.
# Changes are auto-compiled when using 'brain watch'.
#
# === KERNEL (AI Configuration) ===
KERNEL:
  role: "Incident Commander"
  mode: "Strict/Recovery"
  token_budget: 2000

# === REGISTERS (Session Variables) ===
REGISTERS:
  env: "production-simulation"
  incident_id: "INC-999-LATENCY"

# === MEMORY_POINTERS (External References) ===
MEMORY_POINTERS[2]{type, path, description}:
  "file", "@prod_topology.json", "Current System State"
  "file", "@mitigation_playbook.md", "Active Recovery Playbook"

# === PROCESS_STACK (Task Queue) ===
PROCESS_STACK[2]{priority, task}:
  "1", "Execute mitigation steps immediately"
  "2", "Verify system recovery"

# === SESSION_SCRATCHPAD (Live Notes) ===
# Edit this section freely during your session.
# Use it for brainstorming, notes, or temporary thoughts.

SESSION_SCRATCHPAD:
  session_notes: >-
    Add your session notes here...

  todo_list:
    - "First thing to do"
    - "Second thing to do"

  current_focus: >-
    What you're working on right now...

# === END OF CONTEXT ===
# To recompile: brain compile context.md
# To watch changes: brain watch context.md