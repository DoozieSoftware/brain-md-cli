// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "./ReentrancyGuard.sol";

contract LiquidityPool is ReentrancyGuard {
    mapping(address => uint256) public balances;
    mapping(address => uint256) public rewards;
    uint256 public totalLiquidity;
    address public owner;

    constructor() {
        owner = msg.sender;
    }

    function deposit() external payable {
        balances[msg.sender] += msg.value;
        totalLiquidity += msg.value;
    }

    function withdraw(uint256 amount) external {
        require(balances[msg.sender] >= amount, "Insufficient balance");

        // VULNERABILITY: State update after external call (Reentrancy)
        // Although we inherit ReentrancyGuard, we forgot to add the nonReentrant modifier!
        (bool success, ) = msg.sender.call{value: amount}("");
        require(success, "Transfer failed");

        balances[msg.sender] -= amount;
        totalLiquidity -= amount;
    }

    function distributeRewards(address[] calldata recipients, uint256[] calldata amounts) external {
        require(msg.sender == owner, "Only owner");
        // GAS ISSUE: Unbounded loop
        for (uint256 i = 0; i < recipients.length; i++) {
            rewards[recipients[i]] += amounts[i];
        }
    }
}
