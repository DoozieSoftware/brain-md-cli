# brain.md (TOON Format)

KERNEL:
  role: "Lead Backend Architect"
  mode: "Critical/Migration"
  token_budget: 8000

REGISTERS:
  project_root: "./src"
  current_phase: "Migration-Phase-1"

MEMORY_POINTERS[2]{type, path, description}:
  file, "@legacy_ledger.java", "Source of Truth (Legacy)"
  file, "@idempotency_strategy.md", "Safety Rules"

PROCESS_STACK[3]{priority, task}:
  1, "Review Legacy Logic for Hidden Side Effects"
  2, "Map Idempotency Keys to Legacy Transactions"
  3, "Generate Migration Test Cases"
