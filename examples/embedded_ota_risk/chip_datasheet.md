# STM32F4 Flash Programming Manual

## 3.4 Flash Program/Erase Parallelism
The parallelism must be configured before starting a program/erase operation.
...
**WARNING**: If a flash erase operation is interrupted by a power failure or watchdog reset, the sector will remain corrupted.

## 3.5 Protection
...
**Sector 0 (16KB) contains the factory bootloader.**
**Sector 1 (16KB) contains the user bootloader.**

**DANGER**: Writing to Sector 0 or 1 requires unlocking the OPTCR register. ACCIDENTAL WRITES WILL RENDER THE DEVICE UNBOOTABLE.
