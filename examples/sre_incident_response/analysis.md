# Analysis: SRE Incident Response - The Value of "State Flush"

## The Problem: Context Drift in High Stress
In a traditional chat interface, an SRE might paste logs, then ask for diagnosis, then paste more logs, then ask for a query. The chat history becomes a soup of:
1.  Old hypotheses ("Maybe it's the network?")
2.  Stale logs (from 20 minutes ago)
3.  Conversational fluff ("Can you check X?", "Sure, here is X").

When the SRE decides to **Failover**, the LLM still has all that "Network Hypothesis" noise in its context window. It might hallucinate a solution that tries to fix the network instead of executing the failover, or worse, reference an IP address from an earlier log snippet that is no longer relevant.

## The Solution: Explicit Context Loading
With `brain-md`, we performed a **Hard Pivot**:
1.  **Diagnosis Phase**: The LLM only saw the `incident_report` and `runbook_diagnose`. Its entire universe was "Find the problem".
2.  **Mitigation Phase**: We explicitly **unloaded** the diagnosis runbook and **loaded** the `runbook_failover`. We changed the `REGISTERS` to `status: MITIGATING`.

## Why this is Safer
*   **Zero Noise**: The LLM cannot be "confused" by the previous diagnosis attempts. It only knows: "I am in Mitigation mode, here is the Failover Runbook."
*   **Determinism**: If we need to rollback, we can reload the "Diagnosis" state file exactly as it was.
*   **Token Efficiency**: We aren't paying for tokens to re-read the conversation about the network hypothesis.

## Conclusion
For "Vivid Use Cases" like SRE War Rooms, **Context is RAM**. You wouldn't want your production database to have random data in RAM from a previous process. Why would you want your AI assistant to have random chat history when executing a failover?
