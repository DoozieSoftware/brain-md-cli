# Demo Session Report

Here are the compiled TOON payloads for the three scenarios.

## Scenario A - "The Pivot" (Software Engineering)

```
SYSTEM RESET. FORMAT=TOON. `>>>` denotes raw file content. EXECUTE
`PROCESS_STACK`.

KERNEL:
  role: "Senior Backend Dev"

MEMORY_POINTERS[1]{path}:
  "@schema.sql"

PROCESS_STACK[1]{task}:
  "Fix User Table"


SESSION_SCRATCHPAD:
  session_notes: >-
    Add your session notes here...

  todo_list:
    - "First thing to do"
    - "Second thing to do"

  current_focus: >-
    What you're working on right now...


# RESOLVED_MEMORY

@schema.sql:
>>>
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50)
);
<<<
```

*(144 tokens, 1 files resolved)*

## Scenario B - "The Fiction Writer" (Creative)

```
SYSTEM RESET. FORMAT=TOON. CREATIVE MODE: Explore freely within constraints.
`>>>` denotes raw file. EXECUTE `PROCESS_STACK`.

KERNEL:
  role: "Sci-Fi Author"
  mode: "Creative"

MEMORY_POINTERS[2]{path}:
  "@character_sheet_A.md"
  "@location_mars_base.md"

SESSION_SCRATCHPAD:
  session_notes: >-
    Note: The hero is secretly afraid of red dust.

  todo_list:
    - "First thing to do"
    - "Second thing to do"

  current_focus: >-
    What you're working on right now...


# RESOLVED_MEMORY

@character_sheet_A.md:
>>>
# Character Sheet: Captain A
Trait: Brave
Secret: Loves Jazz
<<<

@location_mars_base.md:
>>>
# Location: Mars Base
Atmosphere: Dusty
Color: Red
<<<
```

*(188 tokens, 2 files resolved)*

## Scenario C - "The Crisis Manager" (PM)

```
SYSTEM RESET. FORMAT=TOON. `>>>` denotes raw file content. EXECUTE
`PROCESS_STACK`.

KERNEL:
  role: "Product Manager"
  token_budget: 1000

MEMORY_POINTERS[3]{path}:
  "@team_alpha_status.md"
  "@team_beta_status.md"
  "@team_gamma_status.md"

PROCESS_STACK[1]{task}:
  "Generate Weekly Report highlighting blockers."

SESSION_SCRATCHPAD:
  session_notes: >-
    Add your session notes here...

  todo_list:
    - "First thing to do"
    - "Second thing to do"

  current_focus: >-
    What you're working on right now...


# RESOLVED_MEMORY

@team_alpha_status.md:
>>>
Team Alpha:
- Backend: On Track
- Blocker: None
<<<

@team_beta_status.md:
>>>
Team Beta:
- Frontend: Delayed
- Blocker: API spec missing
<<<

@team_gamma_status.md:
>>>
Team Gamma:
- QA: In Progress
- Blocker: Waiting for staging
<<<
```

*(224 tokens, 3 files resolved)*
