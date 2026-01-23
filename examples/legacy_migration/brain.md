# brain.md - Legacy Migration (Phase 1: Analysis)

KERNEL:
  role: "Legacy Systems Analyst"
  mode: "Analysis/Explanation"
  token_budget: 8000

REGISTERS:
  project: "OmniCorp Core Modernization"
  target_language: "Rust"
  current_module: "Interest Calculation"

MEMORY_POINTERS[2]{type, path, description}:
  "file", "@cobol_source.cbl", "Legacy Source Code"
  "file", "@bank_rules_1985.txt", "Business Rules (1985)"

PROCESS_STACK[2]{priority, task}:
  "1", "Analyze the COBOL source against the 1985 Rules."
  "2", "Explain the 'NY Exception' rounding logic in plain English."
