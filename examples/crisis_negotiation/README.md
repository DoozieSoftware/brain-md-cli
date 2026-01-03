# Vivid Use Case: Crisis Negotiation (The "Silver Creek" Incident)

## Philosophy: Context is RAM
In high-stakes environments, "Context Drift" is dangerous. A long chat history can lead an LLM to hallucinate past concessions or confuse current tactical phases. `brain-md` solves this by treating context as a mutable, explicit state file.

## The Scenario
**Persona:** Dr. Aris Thorne, Lead Crisis Negotiator.
**Subject:** Elias Vane ("Subject 9"), a paranoid schizophrenic network architect holding 4 hostages in a server farm.
**Risk:** If the Negotiator (AI) confuses the "Active Listening" phase with the "Tactical" phase, or forgets a specific demand, the Subject detonates.

## Workflow

### Phase 1: Negotiation
We load `psych_profile.txt`, `demands_live.txt`, and `negotiation_protocol.md`.
The AI is strictly bound to "Active Listening". It cannot make promises not in the file.

### Phase 2: The Pivot (Tactical Breach)
The Subject breaches the firewall. Negotiation has failed.
Instead of telling the AI "Forget what I said, now we are attacking", which is prone to leakage, we **rewrite the RAM**.
We edit `context.md`:
1.  **KERNEL**: Change goal from "De-escalate" to "Distract".
2.  **POINTERS**: Swap `negotiation_protocol.md` for `tactical_breach.txt`.
3.  **STACK**: Change instructions to "Stall" and "Ignore Demands".

## Why "State Flush" is Safer
In a traditional chat, the "history" contains the previous instructions to "Build Rapport". The LLM has to "unlearn" them via a new prompt ("Ignore previous instructions"). This is "soft state" and is fragile.
With `brain-md`, we perform a "hard state" switch. The "Rapport" instructions are physically removed from the context. The AI *cannot* be influenced by them because they no longer exist in its universe.
