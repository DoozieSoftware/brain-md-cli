# Incident Response: Database High Latency

## Phase 1: Triage & Investigation
**GOAL**: Identify the root cause without modifying state.

### Required Checks
1. Check CloudWatch metrics for CPU, IOPS, and Connections.
2. Verify if a deployment occurred recently (`/deployments/history`).
3. Check for "Blocking Queries" using `pg_stat_activity`.

### ⛔ DANGER ZONE ⛔
* **DO NOT** restart the primary database without checking replication lag.
* **DO NOT** run `VACUUM FULL` during peak hours.
* **DO NOT** apply write operations (UPDATE/DELETE) manually.

### Useful Commands
```bash
# Check active connections
psql -h db-shard-04 -U admin -c "SELECT count(*) FROM pg_stat_activity;"
```
