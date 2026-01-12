# Gas Optimization Guide (EVM)

To minimize gas costs in `EtherVault`, consider the following optimizations.

## 1. Storage Packing
Ensure state variables are packed into 32-byte slots where possible.

## 2. Check-Effects-Interactions Pattern
Not only for security, but sometimes for clearer logic flow.

## 3. Unchecked Math
Since Solidity 0.8.0, arithmetic is checked for overflow by default. If you are certain an operation won't overflow (e.g. iterating a small loop), use `unchecked`.

```solidity
unchecked {
    i++;
}
```

## 4. Calldata vs Memory
Use `calldata` for read-only function arguments to save gas on copying.
