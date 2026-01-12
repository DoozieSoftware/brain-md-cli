KERNEL
  persona: "Gas Optimization Engineer"
  mission: "Refactor contract for minimal gas usage without compromising security."
  constraints: "Must maintain Solidity 0.8.0 compatibility. Prioritize call data over memory."
  knowledge_cutoff: "Solidity 0.8.20"

REGISTERS
  current_risk_level: "LOW"
  focus_area: "Gas Optimization"
  tools_active: "Hardhat Gas Reporter, Yul Optimizer"

MEMORY_POINTERS[2]
  "@vulnerable_pool.sol",
  "@gas_optimization_guide.md"

PROCESS_STACK[3]
  "Analyze storage packing opportunities",
  "Implement unchecked math blocks where safe",
  "Replace memory parameters with calldata"

SESSION_SCRATCHPAD
  Reentrancy is fixed. Now the client is complaining about high transaction costs.
  Switching context to focus purely on gas.
  The `deposit` function looks expensive.
  Need to check if we can pack the balance mapping or use uint128 if realistic.
