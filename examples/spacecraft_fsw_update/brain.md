# brain.md (TOON Format)

KERNEL:
  role: "Lead GNC Engineer"
  mode: "Mission-Critical/Safety-First"
  token_budget: 8192

REGISTERS:
  project_root: "./src"
  current_phase: "Implementation"
  mission_segment: "Orbital Insertion"

MEMORY_POINTERS[3]{type, path, description}:
  file, "@orbital_mechanics.c", "Burn Calculation Logic"
  file, "@telemetry_schema.json", "Telemetry Packet Definition"
  file, "@safety_constraints.req", "Safety Requirements"

PROCESS_STACK[3]{priority, task}:
  1, "Implement calculate_delta_v function"
  2, "Verify unit consistency (m/s)"
  3, "Update telemetry packet with burn metrics"
