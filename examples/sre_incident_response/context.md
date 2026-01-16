# context.md - Live Session State
# Generated from brain.md by 'brain boot' command
# Created: 2026-01-16 23:46:28
#
# This is your live RAM - edit freely during the session.
# Changes are auto-compiled when using 'brain watch'.
#
# === KERNEL (AI Configuration) ===
KERNEL:
  role: "Senior SRE Lead"
  mode: "Critical/Incident-Response"
  token_budget: 8000

# === REGISTERS (Session Variables) ===
REGISTERS:
  incident_id: "INC-909"
  severity: "SEV-1"
  status: "MITIGATING"
  primary_shard: "shard-04"
  action: "FAILOVER_INITIATED"

# === MEMORY_POINTERS (External References) ===
MEMORY_POINTERS[3]{type, path, description}:
  "file", "@incident_report.txt", "Current Symptoms"
  "file", "@logs_shard_04.txt", "Recent Error Logs"
  "file", "@runbook_failover.md", "Failover Procedures"

# === PROCESS_STACK (Task Queue) ===
PROCESS_STACK[3]{priority, task}:
  "1", "Verify Replica Health"
  "2", "Execute Failover Command"
  "3", "Verify Write Availability on New Primary"

# === SESSION_SCRATCHPAD (Live Notes) ===
# Edit this section freely during your session.
# Use it for brainstorming, notes, or temporary thoughts.

SESSION_SCRATCHPAD:
  session_notes: >-
    Diagnosis confirmed: Disk Saturation on Primary.
    Decision: Immediate Failover to Replica A.

  todo_list:
    - "Stop Primary"
    - "Promote Replica"

  current_focus: >-
    Executing Failover Sequence.

# === END OF CONTEXT ===
# To recompile: brain compile context.md
# To watch changes: brain watch context.md
