# Incident Mitigation: Payment Gateway Latency

## Severity: CRITICAL
## Owner: SRE-Team-A

### Trigger
Alert: `PaymentGatewayLatency > 2s` for 5 minutes.

### Steps
1. **Verify Database Health**:
   Check `user-db-primary` CPU and Connection Count.
   `aws rds describe-db-instances --db-instance-identifier user-db-primary`

2. **Drain Traffic**:
   Shift traffic to `us-west-2` via Route53.
   `aws route53 change-resource-record-sets --hosted-zone-id Z12345 --change-batch file://drain-east.json`

3. **Scale Service**:
   Increase task count to 10.
   `aws ecs update-service --cluster prod --service payment-gateway --desired-count 10`

4. **Rollback Recent Deployments**:
   If a deployment occurred in the last hour, rollback immediately.
