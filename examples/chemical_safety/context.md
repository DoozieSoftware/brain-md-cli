# context.md - Live Session State
# Generated from brain.md by 'brain boot' command
# Created: 2026-01-08 13:32:12
#
# This is your live RAM - edit freely during the session.
# Changes are auto-compiled when using 'brain watch'.
#
# === KERNEL (AI Configuration) ===
KERNEL:
  User: "Dr. Aris Thorne"
  Role: "Lead Process Safety Engineer"
  Facility: "North Sea Petrochem Site B"
  Safety_Level: "TIER 1 (Critical)"

# === REGISTERS (Session Variables) ===
REGISTERS:
  Current_Focus: "EMERGENCY RESPONSE - POTENTIAL LEAK"
  Reactor_Status: "PRESSURIZING (UNEXPECTED)"
  Permit_Type: "SUSPENDED"
  Active_Crew: "EVACUATED"

# === MEMORY_POINTERS (External References) ===
MEMORY_POINTERS[2]{type, path, description}:
  "file", "@reactor_alpha_specs.txt", "Reactor Alpha Specs"
  "file", "@hazop_guidelines.md", "HAZOP Guidelines"

# === PROCESS_STACK (Task Queue) ===
PROCESS_STACK[3]{priority, task}:
  "1", "Calculate worst-case pressure rise rate"
  "2", "Determine if PSV-101 capacity is sufficient for gas blow-by"
  "3", "Draft Emergency Alert"

# === SESSION_SCRATCHPAD (Live Notes) ===
# Edit this section freely during your session.
# Use it for brainstorming, notes, or temporary thoughts.

SESSION_SCRATCHPAD:
  ALERT: Pressure spike detected during cold shutdown.
  Valve V-302 likely passing.
  Needs immediate calculation of relief load.
