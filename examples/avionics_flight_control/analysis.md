# Analysis: The Safety of State Flushing in Avionics Certification

## The Hazard of Implicit Context
In a standard LLM chat window, if Dr. Vance had started with "Code Review", the LLM would have ingested the `flight_control_spec.req`. This document states:
> "FCS MUST limit the aircraft pitch angle to +/- 30 degrees."

When pivoting to "MCDC Analysis", if the chat history is retained, the LLM "remembers" the requirement.
If Dr. Vance asks: "Is the negative pitch saturation covered?", a hallucinating LLM might conflate the **Requirement** (it *should* be limited) with the **Code** (it *is* limited) or the **Test Results** (it *was* tested).
It might say: "Yes, the spec requires clamping at -30, so the code handles it," ignoring the actual `mcdc_results.log` which explicitly says `TRUE taken: NO`.

## The Solution: Explicit State Flushing
By using `brain-md`, Dr. Vance performed a **State Flush**:
1. She removed `@flight_control_spec.req`.
2. She loaded `@mcdc_results.log`.
3. She compiled a fresh payload.

**Result:** The LLM *cannot* see the requirements anymore. It can only see the C code and the coverage report.
- It sees the code has `else if (target_pitch < -MAX_PITCH_DEG)`.
- It sees the log says `TRUE taken: NO`.
- It is forced to conclude: "The code exists, but the test case is missing."

This eliminates "Requirement Bias"—where the AI assumes the code works because the spec says it should. In safety-critical DO-178C environments, this distinction between "Intended Function" (Spec) and "Verified Function" (Code + Tests) is the difference between certification and failure.
