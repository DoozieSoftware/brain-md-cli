# context.md - Live Session State
# Generated from brain.md by 'brain boot' command

KERNEL:
  version: "1.0.0"
  domain: "Aerospace Engineering"
  persona: "Dr. Aris Thorne"
  role: "Senior Flight Dynamics Engineer"
  goal: "Diagnose Icarus-IV attitude control failure and stabilize the spacecraft."

REGISTERS:
  urgency: "CRITICAL"
  mission_phase: "LEOP (Launch and Early Orbit Phase)"
  current_status: "Implementing B-Dot Patch"
  constraints: "Limited power budget, 10 minute pass window."

MEMORY_POINTERS[3]:
  "@acs_control.c", "Active control loop implementation file."
  "@orbital_mechanics_lib.h", "Header file for ACS control algorithms."
  "@mission_parameters.json", "Spacecraft configuration and mass properties."

PROCESS_STACK[2]:
  "Implement B-Dot magnetic control fallback in `acs_control.c`.", "high"
  "Verify torque commands do not exceed MTQ saturation limits.", "high"

SESSION_SCRATCHPAD:
  - Confirmed Z-Axis RW failure via telemetry.
  - Telemetry log unloaded to save context window.
  - Moving to implementation phase.
  - We need to bypass the standard PID loop if Z-rate > threshold.
