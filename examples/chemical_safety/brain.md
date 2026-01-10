KERNEL:
  user: "Commander Vance"
  role: "Incident Commander, Chemical Plant Sector 7"
  expertise: "Hazardous Materials Management"
  goal: "Identify leak source and contain immediately."
  safety_override: "Prioritize human life over asset protection."

REGISTERS:
  incident_id: "INC-2023-991"
  zone_alert: "Zone 4"
  current_phase: "PHASE 1 - IDENTIFICATION"

MEMORY_POINTERS[2]{description, pointer}
"Safety Data Sheet for HZ-X", "@chemical_A_SDS.txt"
"Sensor Logs", "@sensor_log_zones.csv"

PROCESS_STACK[2]{priority, task}
1, "Analyze sensor logs to confirm leak type and severity."
2, "Cross-reference SDS for immediate handling precautions."

SESSION_SCRATCHPAD:
Waiting for initial assessment...
