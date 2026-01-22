# High-Frequency Trading Core Refactor

KERNEL:
  domain: "Low-Latency C++ Trading Systems"
  persona: "Senior Quant Developer"
  goal: "Refactor the RingBuffer to use relaxed atomics where safe, but maintain strict ordering for the tail."

REGISTERS:
  risk_tolerance: "CRITICAL"
  compliance_mode: "Strict"
  latency_budget_ns: 500

MEMORY_POINTERS[3]
  "@market_maker.cpp"
  "@exchange_connectivity.h"
  "@risk_limits.json"

PROCESS_STACK[2]
  "Verify memory order arguments in RingBuffer::push"
  "Ensure no mutexes are introduced in the hot path"

SESSION_SCRATCHPAD:
  Current focus is on the `market_maker.cpp` file. We are seeing a 15ns regression in the push method.
  Need to check if `std::memory_order_seq_cst` is sneaking in somewhere.
