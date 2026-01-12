package com.bank.core;

import java.math.BigDecimal;

public class TransactionService {
    public void processWithdrawal(BigDecimal balance, BigDecimal amount, String type) {
        if ("S".equals(type)) {
            // TODO: Implement overdraft logic
            if (balance.subtract(amount).compareTo(BigDecimal.ZERO) < 0) {
                throw new InsufficientFundsException();
            }
        }
        // Logic missing for updating balance
    }
}
