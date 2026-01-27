# BRAIN CONF: Fintech Audit Mode

KERNEL:
  version: "2.1"
  security_level: "HIGH"
  compliance_standard: "PCI-DSS-v4"

REGISTERS:
  CURRENT_TASK: "AUDIT_CODEBASE"
  RISK_TOLERANCE: "ZERO"
  RESTRICTED_KEYWORDS: ["System.out", "print", "log", "stacktrace"]

MEMORY_POINTERS[2]:
"@pci_dss_requirements.md"
"@tokenization.java"

PROCESS_STACK[3]:
"REVIEW_CODE_AGAINST_REQUIREMENT_3"
"CHECK_FOR_LOGGING_LEAKS"
"VERIFY_LUHN_VALIDATION"
