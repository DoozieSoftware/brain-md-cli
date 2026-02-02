#ifndef MARKET_DATA_SCHEMA_H
#define MARKET_DATA_SCHEMA_H

#include <cstdint>

struct MarketDataPacket {
    uint32_t symbol_id;
    uint32_t bid_price; // Scaled by 10^4
    uint32_t ask_price; // Scaled by 10^4
    uint32_t timestamp_ns;
};

#endif
