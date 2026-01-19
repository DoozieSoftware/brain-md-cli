# context.md - Live Session State
# Generated from brain.md by 'brain boot' command
# Created: 2023-10-27 10:00:00
#
# This is your live RAM - edit freely during the session.
# Changes are auto-compiled when using 'brain watch'.
#

# === KERNEL (AI Configuration) ===
KERNEL:
  persona: "0xSentinel"
  role: "Senior Smart Contract Auditor"
  mission: "Identify critical vulnerabilities in DeFi protocols"
  strict_mode: "true"

# === REGISTERS (Session Variables) ===
REGISTERS:
  client: "DeFi Nova"
  contract_scope: "LiquidityPool.sol"
  current_phase: "Gas Optimization"
  risk_tolerance: "Zero"

# === MEMORY_POINTERS (External References) ===
MEMORY_POINTERS[3]{type, path, context}:
  "source_code", "@LiquidityPool.sol", "Main contract under audit"
  "dependency", "@ReentrancyGuard.sol", "Inherited security module"
  "reference", "@evm_opcodes.txt", "Gas cost reference"

# === PROCESS_STACK (Task Queue) ===
PROCESS_STACK[2]{priority, task}:
  "1", "Optimize 'distributeRewards' to batch storage writes"
  "2", "Calculate gas savings for packing 'ReentrancyGuard' state"

# === SESSION_SCRATCHPAD (Live Notes) ===
# Edit this section freely during your session.
# Use it for brainstorming, notes, or temporary thoughts.

SESSION_SCRATCHPAD:
  session_notes: >-
    PHASE 1 FINDINGS:
    - Critical reentrancy in withdraw(). Needs nonReentrant modifier.
    - Owner can drain funds if compromised (centralization risk).

    Now switching to Gas Opt. The loop in distributeRewards is expensive (SSTORE).

  todo_list:
    - "Draft report for reentrancy"
    - "Benchmark loop gas cost"

  current_focus: >-
    Minimizing SSTORE operations in the reward loop.

# === END OF CONTEXT ===
# To recompile: brain compile context.md
# To watch changes: brain watch context.md
