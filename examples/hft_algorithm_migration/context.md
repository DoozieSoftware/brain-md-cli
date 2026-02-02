# context.md - Live Session State
# Generated from brain.md by 'brain boot' command
# Created: 2026-02-02 23:41:36
#
# This is your live RAM - edit freely during the session.
# Changes are auto-compiled when using 'brain watch'.
#
# === KERNEL (AI Configuration) ===
KERNEL:
  domain: "fpga_hft"
  language: "vhdl"
  framework: "xilinx_vivado"

# === REGISTERS (Session Variables) ===
REGISTERS:
  goal: "AUDIT"
  source_lang: "cpp"
  target_lang: "vhdl"
  latency_constraint: "200ns"
  audit_standard: "REGULATION_NMS"

# === MEMORY_POINTERS (External References) ===
MEMORY_POINTERS[3]{path}:
  "@legacy_strategy.cpp"
  "@regulation_nms.txt"
  "@compliance_checklist.md"

# === PROCESS_STACK[3] (Task Queue) ===
PROCESS_STACK[3]{task}:
  "Scan legacy_strategy.cpp for trade-through violations."
  "Verify timestamp precision against Regulation NMS requirements."
  "Fill out compliance_checklist.md based on findings."

# === SESSION_SCRATCHPAD (Live Notes) ===
# Edit this section freely during your session.
# Use it for brainstorming, notes, or temporary thoughts.

SESSION_SCRATCHPAD:
  session_notes: >-
    Pivot to Audit.
    Concern: Rule 611 compliance.

  todo_list:
    - "First thing to do"
    - "Second thing to do"

  current_focus: >-
    Auditing for Reg NMS.

# === END OF CONTEXT ===
# To recompile: brain compile context.md
# To watch changes: brain watch context.md
