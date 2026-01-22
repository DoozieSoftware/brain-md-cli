#pragma once
#include <string>

enum class Side { BUY, SELL };

struct Tick {
    std::string symbol;
    double price;
    long timestamp;
};

// Zero-copy networking interface
// WARNING: Not thread-safe. Must only be called from the main event loop.
void submit_order(const std::string& symbol, Side side, int quantity);
