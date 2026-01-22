#include <atomic>
#include <array>
#include "exchange_connectivity.h"

// RingBuffer implementation for lock-free order processing
// CRITICAL: Memory ordering must be sequential consistent for the tail pointer
template<typename T, size_t Size>
class RingBuffer {
    std::array<T, Size> buffer;
    std::atomic<size_t> head{0};
    std::atomic<size_t> tail{0};

public:
    bool push(const T& item) {
        size_t current_tail = tail.load(std::memory_order_relaxed);
        size_t next_tail = (current_tail + 1) % Size;
        if (next_tail == head.load(std::memory_order_acquire)) {
            return false; // Full
        }
        buffer[current_tail] = item;
        tail.store(next_tail, std::memory_order_release);
        return true;
    }
};

void on_tick(const Tick& tick) {
    // Strategy logic here
    if (tick.price > 100.0) {
        // Latency sensitive path
        submit_order(tick.symbol, Side::SELL, 100);
    }
}
