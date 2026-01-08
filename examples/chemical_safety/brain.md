KERNEL:
  User: "Dr. Aris Thorne"
  Role: "Lead Process Safety Engineer"
  Facility: "North Sea Petrochem Site B"
  Safety_Level: "TIER 1 (Critical)"

REGISTERS:
  Current_Focus: "Routine Maintenance - Annual Turnaround"
  Reactor_Status: "Cold_Shutdown"
  Permit_Type: "Cold_Work"
  Active_Crew: "Mechanical Team A"

MEMORY_POINTERS[2]{type, path, description}:
  file, "@reactor_alpha_specs.txt", "Reactor Alpha Specs"
  file, "@hazop_guidelines.md", "HAZOP Guidelines"

PROCESS_STACK[3]{priority, task}:
  1, "Review startup purge procedures"
  2, "Check catalyst loading verify checklist"
  3, "Draft handover email to Operations Manager"

SESSION_SCRATCHPAD:
  Dr. Thorne is reviewing the startup procedure after the maintenance window.
  Verifying the Nitrogen purge duration against the specs.
