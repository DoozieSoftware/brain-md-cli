# context.md - Live Session State

# === KERNEL (AI Configuration) ===
KERNEL:
  role: "Senior Safety Engineer"
  mode: "Strict/Code-Only"
  token_budget: 4096

# === REGISTERS (Session Variables) ===
REGISTERS:
  system_state: "IMPLEMENTATION"
  incident_id: "NULL"

# === MEMORY_POINTERS (External References) ===
MEMORY_POINTERS[2]{type, path, description}:
  "file", "@wayside_controller.c", "Main Controller Logic"
  "file", "@safety_kernel.h", "Safety Overlay Headers"

# === PROCESS_STACK (Task Queue) ===
PROCESS_STACK[1]{priority, task}:
  "1", "Implement fail-safe logic in update_signal_aspect"

# === SESSION_SCRATCHPAD (Live Notes) ===
SESSION_SCRATCHPAD:
  session_notes: >-
    Analysis complete. Moving to implementation.
    Rule 01 verified.

  todo_list:
    - "Verify interlock call"

  current_focus: >-
    Writing C code.
