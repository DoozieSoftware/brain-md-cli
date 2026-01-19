# Incident Response: Database Remediation

## Phase 2: Action & Recovery
**GOAL**: Restore service health.

### Protocol: Failover
If the primary is unresponsive or overloaded due to locking:

1. **Drain Traffic**: Remove `db-shard-04` from the write pool if possible.
2. **Kill Blockers**: Terminate sessions holding locks > 30s.
   ```sql
   SELECT pg_terminate_backend(pid);
   ```
3. **Promote Replica**: If primary is dead, promote `db-shard-04-read-1`.

### ⚠️ EXECUTION SAFETY ⚠️
* Verify you are connected to the CORRECT host.
* Double-check the region is `us-east-1`.
* Announce actions in `#sre-war-room` before execution.
