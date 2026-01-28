#include <stdint.h>
#include "pid.h"

// SAFETY CRITICAL: LEVEL A
// DO-178C COMPLIANT

float compute_elevator_command(float pitch_error, float dt) {
    // PID constants derived from aerodynamic model V3.2
    const float Kp = 1.5f;
    const float Ki = 0.05f;
    const float Kd = 0.2f;

    static float integral = 0.0f;
    static float prev_error = 0.0f;

    integral += pitch_error * dt;

    // Anti-windup clamping (Requirement REQ-SAFE-002)
    if (integral > 10.0f) integral = 10.0f;
    if (integral < -10.0f) integral = -10.0f;

    float derivative = (pitch_error - prev_error) / dt;

    float output = (Kp * pitch_error) + (Ki * integral) + (Kd * derivative);

    prev_error = pitch_error;

    // Output limiting (Requirement REQ-SAFE-001)
    if (output > 25.0f) return 25.0f;
    if (output < -25.0f) return -25.0f;

    return output;
}
