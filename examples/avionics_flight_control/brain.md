# Brain Configuration: Avionics Verification

KERNEL:
  user_name: Dr. Elena Vance
  role: Lead Verification Engineer (DER)
  mission: Certify Pitch Control Loop for eVTOL-X1 (DO-178C Level A)
  environment: Certified Review Workstation (Air-Gapped)

REGISTERS:
  current_phase: Code Review
  safety_level: DAL-A (Catastrophic)
  focus: Requirement Traceability

MEMORY_POINTERS[3]:
  "@flight_control_spec.req",
  "@pid_controller.c",
  "@DO178C_checklist.txt"

PROCESS_STACK[3]:
  "Verify REQ-SAFE-01: Check if PITCH_LIMIT is enforced in C code.",
  "Verify REQ-SAFE-02: Check if Integral Windup Protection exists.",
  "Report any non-conformance findings."

SESSION_SCRATCHPAD:
  - Initial load of artifacts.
  - Ready for trace analysis.
