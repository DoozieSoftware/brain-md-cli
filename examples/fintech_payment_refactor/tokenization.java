package com.fincore.vault;

import java.util.UUID;
import com.fincore.logging.SecureLogger;

/**
 * Handles PAN tokenization.
 * CRITICAL: This class handles raw PANs. Changes must be reviewed by Security.
 */
public class TokenizerService {

    private final SecureLogger logger = new SecureLogger(TokenizerService.class);

    public String tokenize(String pan) {
        if (pan == null || pan.length() < 13) {
            throw new IllegalArgumentException("Invalid PAN length");
        }

        // Validate Luhn Checksum
        if (!luhnCheck(pan)) {
             // ERROR: Never log the PAN in the error message!
             logger.error("Invalid PAN checksum detected.");
             throw new SecurityException("Invalid PAN");
        }

        String token = generateToken();
        saveToVault(token, pan); // Encrypts before write

        // Audit log - MASKED PAN ONLY
        logger.info("Token generated for PAN ending in " + pan.substring(pan.length() - 4));

        return token;
    }

    private String generateToken() {
        return "TOK_" + UUID.randomUUID().toString();
    }

    // Mock Vault save
    private void saveToVault(String token, String pan) {
        // Implementation hidden
    }

    private boolean luhnCheck(String pan) {
        // Mock implementation
        return true;
    }
}
