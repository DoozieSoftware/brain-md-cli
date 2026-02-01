# context.md - Live Session State
# Generated from brain.md by 'brain boot' command
# Created: 2026-02-01 23:32:51
#
# This is your live RAM - edit freely during the session.
# Changes are auto-compiled when using 'brain watch'.
#
# === KERNEL (AI Configuration) ===
KERNEL:
  role: "Lead GNC Engineer"
  mode: "Mission-Critical/Safety-First"
  token_budget: 8192

# === REGISTERS (Session Variables) ===
REGISTERS:
  project_root: "./src"
  current_phase: "Safety Verification"
  mission_segment: "Orbital Insertion"

# === MEMORY_POINTERS (External References) ===
MEMORY_POINTERS[3]{type, path, description}:
  "file", "@orbital_mechanics.c", "Burn Calculation Logic"
  "file", "@telemetry_schema.json", "Telemetry Packet Definition"
  "file", "@safety_constraints.req", "Safety Requirements"

# === PROCESS_STACK (Task Queue) ===
PROCESS_STACK[3]{priority, task}:
  "1", "Audit calculate_delta_v against REQ-SAFE-002"
  "2", "Verify engine gimbal clamps (REQ-SAFE-004)"
  "3", "Sign off on Flight Readiness Review"

# === SESSION_SCRATCHPAD (Live Notes) ===
# Edit this section freely during your session.
# Use it for brainstorming, notes, or temporary thoughts.

SESSION_SCRATCHPAD:
  session_notes: >-
    Realized we haven't checked the redundant nav solution yet.
    Halting implementation to verify safety constraints.

  todo_list:
    - "First thing to do"
    - "Second thing to do"

  current_focus: >-
    Verifying REQ-SAFE-002 before proceeding.

# === END OF CONTEXT ===
# To recompile: brain compile context.md
# To watch changes: brain watch context.md
