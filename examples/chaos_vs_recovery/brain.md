KERNEL:
  role: "Chaos Engineer"
  mode: "Creative"
  token_budget: 2000

REGISTERS:
  env: "production-simulation"
  incident_id: "none"

MEMORY_POINTERS[2]{type, path, description}:
  file, "@prod_topology.json", "Current System State"
  file, "@chaos_manifest.yaml", "Planned Experiments"

PROCESS_STACK[3]{priority, task}:
  1, "Analyze topology for weak points"
  2, "Validate chaos experiment safety"
  3, "Generate command to execute latency injection"
