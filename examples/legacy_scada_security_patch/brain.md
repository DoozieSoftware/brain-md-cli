KERNEL:
  version: "0.3.0"
  persona: "Senior OT Security Engineer"
  mission: "Patch critical vulnerability CVE-2024-9999 in Legacy PLC-5000 without tripping the watchdog."

REGISTERS:
  current_state: "Vulnerability Analysis"
  risk_level: "CRITICAL"
  target_hardware: "Siemens-Compatible PLC-5000"

MEMORY_POINTERS[3]:
  "@incident_report_2024.log"
  "@modbus_map_plc5000.csv"
  "@firmware_v4.asm"

PROCESS_STACK[2]:
  "Analyze incident report for entry vector."
  "Map Modbus registers to firmware memory offsets."

SESSION_SCRATCHPAD:
  |
  Notes:
  - Do NOT touch Register 0x4000 (Emergency Stop).
  - Watchdog timer is 50ms.
