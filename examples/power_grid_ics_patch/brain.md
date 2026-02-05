KERNEL:
  domain: industrial_control_systems
  risk_level: critical_infrastructure
  safety_standard: iec_61508_sil3

REGISTERS:
  user_role: lead_ics_architect
  current_mode: safety_verification
  target_device: siemens_s7_1500

MEMORY_POINTERS[2]{path}:
  "@safety_interlock.c"
  "@iec61508_sil3.req"

PROCESS_STACK[1]{task}:
  "Verify C code against SIL3 requirements for overspeed protection."

SESSION_SCRATCHPAD:
  note: "Analyzing safety logic for overspeed conditions."
