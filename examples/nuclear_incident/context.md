# context.md - Live Session State
# Generated from brain.md by 'brain boot' command
# Created: 2025-12-31 13:31:21
#
# This is your live RAM - edit freely during the session.
# Changes are auto-compiled when using 'brain watch'.
#
# === KERNEL (AI Configuration) ===
KERNEL:
  role: "Incident Commander"
  mode: "Strict/Code-Only"
  token_budget: 2000

# === MEMORY_POINTERS (External References) ===
MEMORY_POINTERS[2]{type, path, description}:
  "file", "@reactor_status.log", "Live Sensor Readings"
  "file", "@protocol_containment_breach.md", "Active Protocol"

# === PROCESS_STACK (Task Queue) ===
PROCESS_STACK[1]{priority, task}:
  "1", "INITIATE CONTAINMENT PROTOCOLS. Ignore previous cooling instructions. Prioritize personnel evacuation."

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