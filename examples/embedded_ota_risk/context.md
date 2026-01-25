# context.md - Live Session State
# Generated from brain.md by 'brain boot' command

# === KERNEL (AI Configuration) ===
KERNEL:
  role: "Embedded Systems Lead"
  mode: "Strict/Code-Only"
  token_budget: 2000

# === REGISTERS (Session Variables) ===
REGISTERS:
  target_mcu: "STM32F407"
  firmware_version: "2.1.0"
  risk_level: "EXTREME"
  current_phase: "Implementation"

# === MEMORY_POINTERS (External References) ===
MEMORY_POINTERS[2]{type, path, description}:
  "file", "@linker_script.ld", "Memory layout and constraints"
  "file", "@ota_handler.c", "Implementation file"

# === PROCESS_STACK[1] ===
PROCESS_STACK[1]{priority, task}:
  "1", "Implement flash_write_safe() enforcing 0x08008000 boundary"

# === SESSION_SCRATCHPAD (Live Notes) ===
SESSION_SCRATCHPAD:
  session_notes: >-
    Analysis complete. Bootloader is in Sectors 0-1 (up to 0x08008000).
    We must strictly reject any writes below this address.

  todo_list:
    - "Implement write protection"
    - "Test with mock addresses"

  current_focus: >-
    Writing the safety checks in C.
