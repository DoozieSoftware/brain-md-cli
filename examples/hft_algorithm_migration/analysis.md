# Analysis: Why State Flushing is Safer

In this High-Frequency Trading scenario, a "State Flush" via `brain-md` provided a critical safety mechanism that a standard chat window cannot.

## The Danger of Chat History
If we had continued in a chat window:
1. **Context Drag**: The LLM would still have "VHDL Translation" in its context window. It might try to "audit" the code by suggesting VHDL fixes, which is not what we want.
2. **Conflicting Constraints**: The `risk_limits.json` (removed in the pivot) might have conflicted with `regulation_nms.txt`. The LLM might have tried to balance them. By removing the risk limits, we forced it to prioritize Regulation NMS.
3. **Hallucination Risk**: The LLM might have hallucinated a "compliant VHDL module" instead of actually auditing the C++ source.

## The Power of Context as RAM
By editing `context.md`:
1. **Zero-Day Focus**: The LLM woke up in `audit_payload.txt` with *only* the mandate to audit. It had no "memory" of ever trying to translate the code.
2. **Precision**: We explicitly loaded the exact regulatory text needed (`Rule 611`).
3. **Audit Trail**: The `context.md` file itself serves as a record of *exactly* what the AI was looking at during the audit phase. This is invaluable for human auditors later.
