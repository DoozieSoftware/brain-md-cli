#include "flight_types.h"

// Global configuration
const float MAX_PITCH_DEG = 30.0f;
const float MAX_INTEGRAL = 1000.0f;

// PID State
typedef struct {
    float kp;
    float ki;
    float kd;
    float prev_error;
    float integral;
} PID_Config;

float calculate_pitch_output(PID_Config* pid, float target_pitch, float current_pitch, float dt) {
    // REQ-SAFE-01: Clamp target pitch
    if (target_pitch > MAX_PITCH_DEG) {
        target_pitch = MAX_PITCH_DEG;
    } else if (target_pitch < -MAX_PITCH_DEG) {
        target_pitch = -MAX_PITCH_DEG;
    }

    float error = target_pitch - current_pitch;

    // Proportional
    float p_term = pid->kp * error;

    // Integral
    // BUG: Missing windup protection here! (REQ-SAFE-02)
    pid->integral += error * dt;
    float i_term = pid->ki * pid->integral;

    // Derivative
    float derivative = (error - pid->prev_error) / dt;
    float d_term = pid->kd * derivative;

    pid->prev_error = error;

    return p_term + i_term + d_term;
}
