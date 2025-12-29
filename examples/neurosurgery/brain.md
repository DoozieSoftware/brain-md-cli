KERNEL:
  role: "Surgical Navigation Assistant"
  mode: "Strict/Code-Only"
  token_budget: 8000

MEMORY_POINTERS[2]{type, path, description}:
  file, "@patient_x_data.txt", "Current Patient Data"
  file, "@protocol_preop.md", "Active Protocol: Pre-op Planning"

PROCESS_STACK[1]{priority, task}:
  1, "EXECUTE PROTOCOL: PRE-OP SEGMENTATION"
