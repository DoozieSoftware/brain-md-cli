MEMORY
{
  FLASH (rx) : ORIGIN = 0x08000000, LENGTH = 1024K
  RAM (xrw)  : ORIGIN = 0x20000000, LENGTH = 128K
}

SECTIONS
{
  .isr_vector :
  {
    . = ALIGN(4);
    KEEP(*(.isr_vector))
  } > FLASH

  .bootloader :
  {
    . = ALIGN(4);
    KEEP(*(.bootloader))
  } > FLASH
  /* CRITICAL: Bootloader resides in first 32KB (0x08000000 - 0x08008000).
     DO NOT WRITE HERE OR DEVICE IS BRICKED. */

  .text :
  {
    . = ALIGN(4);
    *(.text)
    *(.text*)
  } > FLASH
}
