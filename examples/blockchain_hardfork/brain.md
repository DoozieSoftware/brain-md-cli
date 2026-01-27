# brain.md (TOON Format)

KERNEL:
  role: "Core Protocol Maintainer"
  mode: "Strict/Code-Only"
  token_budget: 8000
  focus: "Implementation"

REGISTERS:
  project_root: "./src"
  current_phase: "Hard Fork Implementation"
  target_block: 12500000

MEMORY_POINTERS[2]{type, path, description}:
  file, "@consensus_engine.rs", "Current Consensus Logic"
  file, "@EIP-7777.md", "Hard Fork Specification"

PROCESS_STACK[3]{priority, task}:
  1, "Implement EIP-7777 logic in consensus engine"
  2, "Add unit tests for fork boundary"
  3, "Update chain parameters"
