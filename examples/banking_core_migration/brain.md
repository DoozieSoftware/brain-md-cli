KERNEL:
  user: "Chief Architect (Legacy Migration)"
  mission: "Safely port critical banking logic from COBOL to Java while ensuring zero regression."

REGISTERS:
  MODE: "TRANSLATION"
  STRICTNESS: "HIGH"
  FRAMEWORK: "Spring Boot 3.0"

MEMORY_POINTERS[3]:
  "@legacy_transaction.cbl"
  "@modern_service.java"
  "@sox_compliance.txt"

PROCESS_STACK[3]:
  "Analyze the COBOL logic for hidden side effects."
  "Identify discrepancies in the Java implementation."
  "Propose a refactor that strictly adheres to the SOX compliance rules."

SESSION_SCRATCHPAD:
  |
  The legacy system allows negative balances for Checking accounts but NOT Savings.
  The Java code seems to miss the Checking account logic entirely.
