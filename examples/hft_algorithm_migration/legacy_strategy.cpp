#include "market_data_schema.h"
#include <iostream>

// Legacy strategy for ARB
// WARNING: This code assumes 32-bit architecture for some calculations.
// MIGRATION NOTE: Verify all int usage for FPGA widths.

void on_market_update(const MarketDataPacket& packet) {
    static int position = 0;
    int price_delta = packet.ask_price - packet.bid_price;

    // Simple momentum logic
    if (price_delta > 100) {
        // RACE CONDITION RISK: 'position' read/write not atomic if multi-threaded
        if (position < 1000) {
             position += 100;
             std::cout << "BUY Signal. New Pos: " << position << std::endl;
        }
    }
}
