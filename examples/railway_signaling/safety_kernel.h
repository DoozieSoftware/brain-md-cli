#ifndef SAFETY_KERNEL_H
#define SAFETY_KERNEL_H

typedef enum { RED, GREEN, YELLOW } SignalState;

// Returns true if state transition is allowed by formal rules
bool verify_interlock(int signal_id, SignalState proposed_state);
void trip_emergency_brake(void);

#endif
