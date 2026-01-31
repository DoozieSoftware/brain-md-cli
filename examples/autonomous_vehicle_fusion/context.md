# context.md - Live Session State
# Generated from brain.md by 'brain boot' command
# Created: 2026-01-31 23:48:34
#
# This is your live RAM - edit freely during the session.
# Changes are auto-compiled when using 'brain watch'.
#
# === KERNEL (AI Configuration) ===
KERNEL:
  role: "Senior Perception Engineer"
  mode: "Analysis"
  token_budget: 8000
  domain: "Autonomous Vehicles"

# === REGISTERS (Session Variables) ===
REGISTERS:
  platform: "NVIDIA Drive Orin"
  sensor_suite: "Lidar(Velodyne)+Camera(OnSemi)"
  cuda_version: "11.4"
  safety_level: "ASIL-D"
  current_phase: "Verification"

# === MEMORY_POINTERS (External References) ===
MEMORY_POINTERS[3]{type, path, description}:
  "file", "@fusion_kernel.cu", "CUDA implementation of projection logic"
  "file", "@calibration_extrinsics.yaml", "Sensor extrinsic matrices"
  "file", "@iso26262_safety_goals.req", "Safety requirements"

# === PROCESS_STACK (Task Queue) ===
PROCESS_STACK[2]{priority, task}:
  "1", "Verify fusion_kernel.cu against SG-03 (Memory Corruption)"
  "2", "Generate FMEA report for ghost object scenarios (SG-01)"

# === SESSION_SCRATCHPAD (Live Notes) ===
# Edit this section freely during your session.
# Use it for brainstorming, notes, or temporary thoughts.

SESSION_SCRATCHPAD:
  session_notes: >-
    Shifted focus to safety analysis.
    Concerns about memory bounds in the kernel.

  todo_list:
    - "Check bounds checking"
    - "Validate ASIL-D compliance"

  current_focus: >-
    Safety Audit

# === END OF CONTEXT ===
# To recompile: brain compile context.md
# To watch changes: brain watch context.md
