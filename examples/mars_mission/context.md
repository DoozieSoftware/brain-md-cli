# context.md - Live Session State
# Generated from brain.md by 'brain boot' command
# Created: 2026-01-01 13:32:38
#
# This is your live RAM - edit freely during the session.
# Changes are auto-compiled when using 'brain watch'.
#
# === KERNEL (AI Configuration) ===
KERNEL:
  name: "ARES-7 FDO Support"
  role: "Emergency Systems Operator"
  directives: "PRIORITY ZERO: STABILIZE SPACECRAFT STRUCTURE. IGNORE BURN PROTOCOLS."

# === MEMORY_POINTERS (External References) ===
MEMORY_POINTERS[2]{path, description}:
  "examples/mars_mission/telemetry_t_minus_10.log", "Live Telemetry Stream"
  "examples/mars_mission/emergency_solar_fix.md", "Solar Array Emergency Proc"

# === PROCESS_STACK (Task Queue) ===
PROCESS_STACK[3]{status, task}:
  "ACTIVE", "Calculate max RCS torque allowed before SAW-2 fracture."
  "PENDING", "Draft load-shedding sequence for power bus B."
  "ABORTED", "Orbital Insertion Burn (MOI) - STAND DOWN."

# === SESSION_SCRATCHPAD (Live Notes) ===
# Edit this section freely during your session.
# Use it for brainstorming, notes, or temporary thoughts.

SESSION_SCRATCHPAD:
  session_notes: >-
    Emergency declared at T-30 mins.
    Switching focus to structural integrity.

  todo_list:
    - "Disable Auto-Track"
    - "Inhibit Quads 3/4"

  current_focus: >-
    Preventing Solar Wing 2 snap.

# === END OF CONTEXT ===
# To recompile: brain compile context.md
# To watch changes: brain watch context.md