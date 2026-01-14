#ifndef ORBITAL_MECHANICS_LIB_H
#define ORBITAL_MECHANICS_LIB_H

typedef struct {
    double q0, q1, q2, q3; // Quaternion
} Attitude;

typedef struct {
    double x, y, z;
} Vector3;

// ACS Control Modes
#define MODE_IDLE 0
#define MODE_DETUMBLE 1
#define MODE_POINTING 2
#define MODE_SAFE 99

// Hardware Identifiers
#define ACTUATOR_RW_X 0x01
#define ACTUATOR_RW_Y 0x02
#define ACTUATOR_RW_Z 0x03
#define ACTUATOR_MTQ_BARS 0x04

/**
 * Calculates the required torque to detumble the spacecraft.
 * @param current_rates Current angular velocity readings from gyro
 * @param target_rates Desired angular velocity (usually 0)
 * @return Vector3 Torque command in body frame
 */
Vector3 calculate_b_dot_control(Vector3 current_rates, Vector3 magnetic_field_b);

#endif // ORBITAL_MECHANICS_LIB_H
