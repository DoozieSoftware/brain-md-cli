# context.md (Live State)

KERNEL:
  role: "Site Reliability Engineer (SRE)"
  mode: "Critical/Write-Access"
  token_budget: 2048

REGISTERS:
  incident_id: "INC-2024-10-27-01"
  severity: "SEV-1"
  region: "us-east-1"
  status: "REMEDIATING"

MEMORY_POINTERS[3]{type, path, description}:
  file, "@alert_logs.txt", "Live Logs from Splunk"
  file, "@prod_us_east_1_topology.yaml", "Infrastructure Map"
  file, "@runbook_remediation.md", "SOP for Remediation"

PROCESS_STACK[3]{priority, task}:
  1, "Execute Kill Blockers command"
  2, "Monitor connection drop"
  3, "Verify service recovery"

SESSION_SCRATCHPAD:
  session_notes: >-
    Root cause identified: Long running analytical query on primary.
