# NEURO-ROBOTIC SURGICAL ASSISTANT - CONTEXT STATE

KERNEL:
  user: "Dr. Aris Thorne"
  role: "Lead Neuro-Surgeon"
  goal: "Execute flawless DBS lead placement for tremor control."
  environment: "Operating Room 4 - Sterile Field"
  safety_lock: "ENGAGED"

REGISTERS:
  patient_status: "stable"
  phase: "trajectory_verification"
  anesthesia_level: "conscious_sedation"
  last_vitals: "BP 120/80, HR 72"

MEMORY_POINTERS[2]{path}:
"@patient_atlas.json"
"@craniotomy_protocol.txt"

PROCESS_STACK[3]{task}:
"Verify entry point coordinates matches MRI plan."
"Advance micro-electrode to Z -10mm."
"Listen for thalamic burst activity."

SESSION_SCRATCHPAD:
  - All instruments calibrated.
  - Nurse confirmed sterility.
  - Patient is awake and responsive.
