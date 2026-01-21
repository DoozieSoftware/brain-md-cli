#ifndef INTERRUPT_VECTOR_H
#define INTERRUPT_VECTOR_H

// Priority Levels (0 = Highest, 15 = Lowest)
#define PRIORITY_WATCHDOG    0
#define PRIORITY_OCCLUSION   1
#define PRIORITY_MOTOR_ENC   2
#define PRIORITY_USER_BTN    10

void ISR_Watchdog(void);
void ISR_Occlusion(void);
void ISR_MotorEncoder(void);

#endif
