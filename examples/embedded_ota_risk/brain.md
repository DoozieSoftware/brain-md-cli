KERNEL:
  role: "Embedded Systems Lead"
  mode: "Analysis/Planning"
  token_budget: 2000

REGISTERS:
  target_mcu: "STM32F407"
  firmware_version: "2.1.0"
  risk_level: "EXTREME"

MEMORY_POINTERS[2]{type, path, description}:
  file, "@linker_script.ld", "Memory layout and constraints"
  file, "@chip_datasheet.md", "Critical hardware safety rules"

PROCESS_STACK[2]{priority, task}:
  1, "Analyze memory map for safe OTA partition boundaries"
  2, "Define flash write constraints to prevent bricking"
