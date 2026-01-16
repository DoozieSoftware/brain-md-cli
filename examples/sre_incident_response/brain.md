# brain.md (TOON Format)

KERNEL:
  role: "Senior SRE Lead"
  mode: "Critical/Incident-Response"
  token_budget: 8000

REGISTERS:
  incident_id: "INC-909"
  severity: "SEV-1"
  status: "INVESTIGATING"
  primary_shard: "shard-04"

MEMORY_POINTERS[3]{type, path, description}:
  file, "@incident_report.txt", "Current Symptoms"
  file, "@logs_shard_04.txt", "Recent Error Logs"
  file, "@runbook_diagnose.md", "Diagnostic Procedures"

PROCESS_STACK[3]{priority, task}:
  1, "Analyze Error Logs for Patterns"
  2, "Check Replication Lag on Shard-04"
  3, "Hypothesize Root Cause"
