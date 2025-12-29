# brain.md (TOON Format)

KERNEL:
  role: "Senior Architect"
  mode: "Strict/Code-Only"
  token_budget: 4000

REGISTERS:
  project_root: "./src"
  current_phase: "Migration"

MEMORY_POINTERS[2]{type, path, description}:
  file, "@agents.md", "Team Persona Definitions"
  file, "@schema.sql", "Database Structure"

PROCESS_STACK[3]{priority, task}:
  1, "Analyze Schema for Indexing"
  2, "Draft Migration Script"
  3, "Update Documentation"
