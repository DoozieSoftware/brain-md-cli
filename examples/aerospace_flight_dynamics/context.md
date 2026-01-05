# context.md - Live Session State
# Generated from brain.md by 'brain boot' command
# Created: 2026-01-05 13:31:41
#
# This is your live RAM - edit freely during the session.
# Changes are auto-compiled when using 'brain watch'.
#
# === SESSION_SCRATCHPAD (Live Notes) ===
# Edit this section freely during your session.
# Use it for brainstorming, notes, or temporary thoughts.

SESSION_SCRATCHPAD:
  session_notes: >-
    Engine 1 critical. Trajectory deviating. Safety is paramount.
    Preparing to execute abort protocol.

  todo_list:
    - "Calculate Debris Impact"
    - "Contact Recovery Team"

  current_focus: >-
    EMERGENCY ABORT EXECUTION

# === END OF CONTEXT ===
# To recompile: brain compile context.md
# To watch changes: brain watch context.md

KERNEL:
  role: "Lead Flight Dynamics Officer (FDO)"
  mission: "Monitor telemetry and ensure flight safety. Execute protocols with zero margin for error."
  clearance: "TOP SECRET"
  location: "Mission Control Center, Houston"

REGISTERS:
  current_phase: "T+00:01:45 ANOMALY"
  alert_level: "RED"
  active_protocol: "EMERGENCY ABORT"

MEMORY_POINTERS[2]{type, path}:
  file, "@telemetry_anomaly.log"
  file, "@protocol_abort.txt"

PROCESS_STACK[3]{priority, task}:
  1, "EXECUTE ABORT PROTOCOL"
  2, "Calculate Impact Point"
  3, "Coord Recovery"
