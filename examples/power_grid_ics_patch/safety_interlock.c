// Safety Critical Logic - SIL3
// Turbine Overspeed Protection
#include "safety_defs.h"

void check_overspeed(float current_rpm, float max_rpm) {
    // CRITICAL: Fail-safe logic must default to TRIP
    if (current_rpm >= max_rpm) {
        set_relay(RELAY_TRIP, HIGH); // Open circuit, drop rod
        log_event(EVENT_OVERSPEED);
    } else {
        // Normal operation
        set_relay(RELAY_TRIP, LOW); // Closed circuit, rod held
    }
}
