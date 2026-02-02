KERNEL:
  domain: "fpga_hft"
  language: "vhdl"
  framework: "xilinx_vivado"

REGISTERS:
  goal: "TRANSLATE"
  source_lang: "cpp"
  target_lang: "vhdl"
  latency_constraint: "200ns"

MEMORY_POINTERS[3]{path}:
  "@legacy_strategy.cpp"
  "@market_data_schema.h"
  "@risk_limits.json"

PROCESS_STACK[3]{task}:
  "Analyze legacy_strategy.cpp for integer width assumptions."
  "Map C++ structs to VHDL std_logic_vector signals."
  "Generate VHDL entity for on_market_update."

SESSION_SCRATCHPAD:
  |
  Notes:
  - Watch out for the static int position variable. Needs a register in VHDL.
  - Price delta calculation needs signed arithmetic.
