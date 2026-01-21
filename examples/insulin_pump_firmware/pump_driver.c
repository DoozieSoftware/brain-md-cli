#include "pump_driver.h"
#include "interrupt_vector.h"

// WARNING: Direct hardware access. Ensure interrupts are disabled during critical sections.

volatile uint32_t *MOTOR_CTRL_REG = (uint32_t *)0x40001000;
volatile uint32_t *ENCODER_COUNT = (uint32_t *)0x40001004;

void deliver_bolus(float units) {
    if (units > 10.0) {
        // ERROR: Safety violation
        trigger_alarm(ALARM_OVERDOSE_PREVENTION);
        return;
    }

    // Convert units to stepper ticks
    uint32_t ticks = (uint32_t)(units * TICKS_PER_UNIT);

    disable_interrupts();
    *MOTOR_CTRL_REG = (ticks | ENABLE_MOTOR_MASK);
    while (*ENCODER_COUNT < ticks) {
        // Busy wait for completion
    }
    *MOTOR_CTRL_REG = DISABLE_MOTOR_MASK;
    enable_interrupts();
}
