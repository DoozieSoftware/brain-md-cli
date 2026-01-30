#include "safety_kernel.h"

void update_signal_aspect(Signal* s, Switch* w) {
    // CRITICAL: Fail-safe default
    SignalState state = RED;

    if (w->position == NORMAL && !is_occupied(w->track_id)) {
        state = GREEN;
    }

    // Safety Kernel Overlay
    if (!verify_interlock(s->id, state)) {
        trip_emergency_brake();
    }

    set_signal(s, state);
}
