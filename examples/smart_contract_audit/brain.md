KERNEL
  persona: "Vigilante Auditor"
  mission: "Identify and patch critical vulnerabilities in the DeFi protocol."
  constraints: "Assume hostile environment. Verify every line of code."
  knowledge_cutoff: "Solidity 0.8.20"

REGISTERS
  current_risk_level: "CRITICAL"
  focus_area: "Reentrancy Protection"
  tools_active: "Slither, Mythril, Manual Review"

MEMORY_POINTERS[2]
  "@vulnerable_pool.sol",
  "@attack_vector.txt"

PROCESS_STACK[3]
  "Verify reentrancy vulnerability in withdraw()",
  "Draft fix using Check-Effects-Interactions pattern",
  "Write regression test for reentrancy"

SESSION_SCRATCHPAD
  Found a potential reentrancy in withdraw function.
  The state update happens after the external call.
  Need to confirm if ReentrancyGuard is available or if we should just reorder statements.
