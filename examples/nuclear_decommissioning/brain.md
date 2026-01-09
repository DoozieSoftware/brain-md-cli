KERNEL:
  user: Dr. Aris Thorne
  role: Lead Decommissioning Engineer
  clearance_level: 5 (Top Secret)
  mission: Safe decommissioning of Helios-V Reactor Core.
  safety_directive: PRIMARY_DIRECTIVE_ZERO_LEAK

REGISTERS:
  current_zone: ZONE_RED_CORE
  radiation_level: 4.5 Sv/h
  team_status: DEPLOYED
  protective_gear: CLASS_A_HAZMAT

MEMORY_POINTERS[3]{ptr, path, desc}
  "@schematic", reactor_schematic_v4.txt, Detailed blueprints of the reactor core structure.
  "@protocol", safety_protocol_alpha.txt, Mandatory safety checks for fuel rod manipulation.
  "@coolant", coolant_procedure.txt, Emergency coolant leak containment procedures.

PROCESS_STACK[1]{task}
  TASK: Fuel Rod Extraction - Rod #445
