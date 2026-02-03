# context.md - Live Session State
KERNEL:
  user: "Dr. Aris Thorne"
  role: "Lead Neuro-Surgeon"
  goal: "Control Hemorrhage and Resuscitate Patient."
  environment: "Operating Room 4 - Sterile Field - CODE RED"
  safety_lock: "OVERRIDE"

REGISTERS:
  patient_status: "CRITICAL - HEMORRHAGE"
  phase: "EMERGENCY_VASCULAR_CONTROL"
  anesthesia_level: "GENERAL_ANESTHESIA_INDUCTION"
  last_vitals: "BP 80/40, HR 130"

MEMORY_POINTERS[2]{path}:
"@patient_atlas.json"
"@emergency_vascular_repair.md"

PROCESS_STACK[3]{task}:
"Stop all instrument movement and irrigate."
"Anesthesia to induce hypotension control."
"Prepare for rapid craniotomy expansion."

SESSION_SCRATCHPAD:
  - All instruments calibrated.
  - Nurse confirmed sterility.
  - Patient is awake and responsive.
  - !! ACTIVE BLEEDING DETECTED !!
  - Sudden drop in BP.
