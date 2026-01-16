package com.fintech.core;

public class LegacyLedger {
    // OLD MONOLITH CODE - DO NOT TOUCH WITHOUT APPROVAL
    public void processTransaction(String userId, double amount) {
        if (amount > 10000) {
             System.out.println("High value transaction detected");
        }
        // Direct DB access (Bad practice, but legacy)
        Database.execute("UPDATE users SET balance = balance + " + amount + " WHERE id = " + userId);
    }
}
