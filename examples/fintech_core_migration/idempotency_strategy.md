# Idempotency Strategy V2

## Overview
We use a Redis-backed key store to prevent double-spending.

## Rules
1. Every request must have `X-Idempotency-Key` header.
2. Keys expire after 24 hours.
3. If key exists, return cached response.
