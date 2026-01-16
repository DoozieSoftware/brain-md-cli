# Runbook: Primary Failover Procedure (Postgres/Patroni)

WARNING: DATA LOSS RISK. AUTHORIZATION REQUIRED.

1. Verify Replica Health (`patronictl list`).
2. Stop the Primary (`sudo systemctl stop postgresql`).
3. Promote the healthiest Replica (`patronictl failover --force`).
4. Update connection string in Vault/Consul (if not automated).
5. Verify new Primary is accepting writes.
