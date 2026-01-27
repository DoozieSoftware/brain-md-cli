# PCI DSS v4.0 - Data Protection Requirements

## Requirement 3: Protect Stored Account Data

3.1.1 The full Primary Account Number (PAN) is not stored unless strictly necessary.
3.2.1 Do not store sensitive authentication data after authorization (even if encrypted):
    - The full contents of any track (magnetic stripe, chip).
    - The card verification code (CVC/CVV).
    - The PIN or PIN block.
3.3.1 PAN is masked when displayed (the first six and last four digits are the maximum number of digits to be displayed).
3.4.1 If PAN is stored, it must be rendered unreadable anywhere it is stored (including portable digital media, backup media, and in logs).
    - One-way hashes based on strong cryptography.
    - Truncation.
    - Index tokens and pads.
    - Strong cryptography with associated key-management processes.

## Requirement 6: Develop and Maintain Secure Systems

6.2.4 Software engineering techniques must prevent common coding vulnerabilities:
    - Injection flaws.
    - Buffer overflows.
    - Insecure cryptographic storage.
    - Insecure communications.
    - Improper error handling (do not leak sensitive data in error logs).
