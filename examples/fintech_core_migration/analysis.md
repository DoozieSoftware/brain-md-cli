# Analysis: The Power of State Flushing

## The Scenario
We shifted from a "Migration Implementation" phase to an "Emergency Rollback" phase in seconds.

## Why "Context is RAM" is Safer here:

1.  **Zero Context Drift**:
    In a traditional chat, the LLM would still have "implementing new features" in its working memory. It might try to suggest a fix that preserves the new code while we are trying to kill it. By flushing the state, we ensure the LLM is *only* focused on the rollback.

2.  **Verbatim Accuracy**:
    We swapped `idempotency_strategy.md` for `reconciliation_script.py`. The LLM now sees the exact code responsible for the error. In a long chat window, code pasted 30 messages ago is often "summarized" or "compressed" by the model, leading to hallucinated function names. Here, it is fresh and exact.

3.  **Cognitive Load Management (Token Efficiency)**:
    We removed the `idempotency_strategy.md` file. It is irrelevant during a fire. We don't want the LLM to waste reasoning capacity checking if our rollback script complies with idempotency rules that don't apply to emergency SQL dumps.

4.  **Enforced Protocol**:
    The `PROCESS_STACK` explicitly lists "Notify Compliance Team". In a panic, humans forget steps. The `brain.md` enforces the procedure.
