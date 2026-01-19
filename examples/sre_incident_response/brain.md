# brain.md (TOON Format)

KERNEL:
  role: "Site Reliability Engineer (SRE)"
  mode: "Critical/Read-Only"
  token_budget: 2048

REGISTERS:
  incident_id: "INC-2024-10-27-01"
  severity: "SEV-1"
  region: "us-east-1"
  status: "INVESTIGATING"

MEMORY_POINTERS[3]{type, path, description}:
  file, "@alert_logs.txt", "Live Logs from Splunk"
  file, "@prod_us_east_1_topology.yaml", "Infrastructure Map"
  file, "@runbook_triage.md", "SOP for Triage"

PROCESS_STACK[3]{priority, task}:
  1, "Correlate error logs with topology"
  2, "Identify bottleneck component"
  3, "Propose read-only diagnostic queries"
