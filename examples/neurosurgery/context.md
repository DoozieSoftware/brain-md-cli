# context.md - Live Session State
# Generated from brain.md by 'brain boot' command
# Created: 2025-12-29 13:15:40
#
# This is your live RAM - edit freely during the session.
# Changes are auto-compiled when using 'brain watch'.
#
# === KERNEL (AI Configuration) ===
KERNEL:
  role: "Surgical Navigation Assistant"
  mode: "Strict/Code-Only"
  token_budget: 8000

# === MEMORY_POINTERS (External References) ===
MEMORY_POINTERS[2]{type, path, description}:
  "file", "@patient_x_data.txt", "Current Patient Data"
  "file", "@protocol_emergency.md", "Active Protocol: EMERGENCY"

# === PROCESS_STACK (Task Queue) ===
PROCESS_STACK[1]{priority, task}:
  "1", "EXECUTE EMERGENCY PROTOCOL: VASCULAR CONTROL"

# === SESSION_SCRATCHPAD (Live Notes) ===
# Edit this section freely during your session.
# Use it for brainstorming, notes, or temporary thoughts.

SESSION_SCRATCHPAD:
  session_notes: >-
    HEMORRHAGE DETECTED SECTOR 4.
    Arterial loop compromised.
    ABORTING PRE-OP PLAN.

  todo_list:
    - "Identify vessel"
    - "Calculate occlusion point"

  current_focus: >-
    SAVING THE PATIENT

# === END OF CONTEXT ===
# To recompile: brain compile context.md
# To watch changes: brain watch context.md
