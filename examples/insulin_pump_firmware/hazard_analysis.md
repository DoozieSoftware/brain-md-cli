# Hazard Analysis: Pump Motor Failure Modes

| Hazard ID | Description | Severity | Mitigation |
|-----------|-------------|----------|------------|
| HZ-01 | Motor Runaway (Stuck High) | Catastrophic | Independent hardware watchdog disconnects power. |
| HZ-02 | Encoder Failure (No Feedback) | Critical | Max runtime timer in software. |
| HZ-03 | Occlusion Sensor False Positive | Major | Debounce logic (100ms) required. |
