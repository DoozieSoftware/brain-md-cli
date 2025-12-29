# Driver Prompt Specification

## Purpose

The Driver Prompt is a standardized natural language prefix that teaches the AI how to interpret the TOON payload. It precedes every compiled context injection.

---

## Standard Driver Prompt

```
SYSTEM RESET. FORMAT=TOON. `>>>` denotes raw file content. EXECUTE `PROCESS_STACK`.
```

---

## Components

| Component | Purpose |
|-----------|---------|
| `SYSTEM RESET` | Signals context boundary, reduces bleed from prior conversation |
| `FORMAT=TOON` | Declares the payload format |
| `>>>` denotes raw file content | Teaches heredoc interpretation |
| `EXECUTE PROCESS_STACK` | Directs AI to prioritize tasks in order |

---

## Variations

### Strict Mode
```
SYSTEM RESET. FORMAT=TOON. STRICT MODE: Code only, no explanations. `>>>` = raw file. EXECUTE `PROCESS_STACK`.
```

### Creative Mode
```
SYSTEM RESET. FORMAT=TOON. CREATIVE MODE: Explore freely within constraints. `>>>` = raw file. EXECUTE `PROCESS_STACK`.
```

### Analysis Mode
```
SYSTEM RESET. FORMAT=TOON. ANALYSIS MODE: Review and report, no modifications. `>>>` = raw file. EXECUTE `PROCESS_STACK`.
```

---

## Implementation

The compiler prepends the driver prompt automatically. The mode can be derived from `KERNEL.mode` if specified.
