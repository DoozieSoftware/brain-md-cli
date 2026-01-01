# ORBITAL INSERTION BURN PROTOCOL (ALPHA)

## 1. PRE-BURN CHECKLIST
- Verify Attitude Control System (ACS) stability < 0.05 deg/s error.
- Confirm Deep Space Network (DSN) uplink lock.
- Isolate RCS Quad 3 if thermal warning persists.

## 2. BURN EXECUTION
- Target Delta-V: 650 m/s
- Burn Duration: 420.5 seconds
- Main Engine: TRITON-X
- Throttle Profile:
    - 0-10s: 10% (Chilldown/Settling)
    - 10-410s: 100%
    - 410-420.5s: 10% (Shutdown transient)

## 3. ABORT CRITERIA
- Chamber pressure deviation > 5%
- Attitude deviation > 2 degrees
- Any RED level alarm from ECLSS
