#include <stdint.h>
#include "stm32f4xx.h"

// TODO: Implement safe flash write
void flash_write_safe(uint32_t address, uint8_t* data, uint32_t length) {
    // 1. Check address against bootloader boundary

    // 2. Unlock flash

    // 3. Program

    // 4. Lock flash
}
