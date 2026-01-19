# Smart Contract Audit Checklist v2.1

## Critical Severity
- [ ] **Reentrancy**: Check for Check-Effects-Interactions pattern violation.
- [ ] **Access Control**: Verify `onlyOwner` or similar modifiers on sensitive functions.
- [ ] **Integer Overflow/Underflow**: (Less relevant in 0.8+ but check for `unchecked` blocks).

## High Severity
- [ ] **Front-Running**: Can a miner manipulate the transaction order?
- [ ] **Denial of Service**: Unbounded loops or reliance on external calls.

## Gas Optimization
- [ ] **Storage Layout**: Pack variables to fit in 256-bit slots.
- [ ] **Memory vs Calldata**: Use `calldata` for read-only array arguments.
- [ ] **Loops**: Avoid loops in state-changing functions if possible.
