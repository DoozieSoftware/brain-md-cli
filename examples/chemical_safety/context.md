# context.md - Live Session State
# Generated from brain.md by 'brain boot' command
# Created: 2026-01-10 13:56:47
#
# This is your live RAM - edit freely during the session.
# Changes are auto-compiled when using 'brain watch'.
#
# === KERNEL (AI Configuration) ===
KERNEL:
  user: "Commander Vance"
  role: "Incident Commander, Chemical Plant Sector 7"
  expertise: "Hazardous Materials Management"
  goal: "Execute Containment and Neutralization."
  safety_override: "Prioritize human life over asset protection."

# === REGISTERS (Session Variables) ===
REGISTERS:
  incident_id: "INC-2023-991"
  zone_alert: "Zone 4"
  current_phase: "PHASE 2 - CONTAINMENT & NEUTRALIZATION"
  hazard_confirmed: "Hydrazine-X"

# === MEMORY_POINTERS (Context Loading) ===
# Identification docs removed to reduce noise/cost.
# Loading operational protocols.
MEMORY_POINTERS[2]{description, pointer}
"Protocol: Alpha Containment", "@protocol_containment_alpha.md"
"Neutralization Procedure", "@neutralization_procedure.md"

# === PROCESS_STACK (Current Tasks) ===
PROCESS_STACK[2]{priority, task}
1, "Generate a step-by-step checklist for the hazmat team based on Alpha Containment and Neutralization protocols."
2, "Draft an update message for Central Command confirming Phase 2 initiation."

# === SESSION_SCRATCHPAD (Live Notes) ===
SESSION_SCRATCHPAD:
  status: "Leak confirmed. HZ-X. Concentration critical. Initiating containment."
