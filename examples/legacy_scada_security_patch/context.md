# context.md - Live Session State
# Generated from brain.md by 'brain boot' command
# Created: 2025-05-15 10:00:00
#
# This is your live RAM - edit freely during the session.
# Changes are auto-compiled when using 'brain watch'.
#
# === KERNEL (AI Configuration) ===
KERNEL:
  version: "0.3.0"
  persona: "Senior OT Security Engineer"
  mission: "Patch critical vulnerability CVE-2024-9999 in Legacy PLC-5000 without tripping the watchdog."

# === REGISTERS (Session Variables) ===
REGISTERS:
  current_state: "Patch Implementation via Serial"
  risk_level: "HIGH"
  target_hardware: "Siemens-Compatible PLC-5000"

# === MEMORY_POINTERS (Loaded Files) ===
MEMORY_POINTERS[3]:
  "@serial_debug_protocol.txt"
  "@modbus_map_plc5000.csv"
  "@firmware_v4.asm"

# === PROCESS_STACK (Task Queue) ===
PROCESS_STACK[2]:
  "Draft Assembly patch using POKE commands."
  "Verify Watchdog is disabled before upload."

# === SESSION_SCRATCHPAD (Live Notes) ===
SESSION_SCRATCHPAD:
  |
  Notes:
  - Do NOT touch Register 0x4000 (Emergency Stop).
  - Watchdog timer is 50ms.
  - Incident log removed to reduce noise. Focus on hex codes.
