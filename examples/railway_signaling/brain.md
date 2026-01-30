KERNEL:
  role: "Senior Safety Engineer"
  mode: "Analysis/Planning"
  token_budget: 4096

REGISTERS:
  system_state: "DESIGN_REVIEW"
  incident_id: "NULL"

MEMORY_POINTERS[2]{type, path, description}:
  file, "@interlocking_rules.txt", "Formal safety logic"
  file, "@track_layout.json", "Physical topology"

PROCESS_STACK[2]{priority, task}:
  1, "Verify signal K23 conflict with switch W4"
  2, "Generate counter-example trace"

SESSION_SCRATCHPAD:
  notes: "Investigating potential race condition in sector 7."
