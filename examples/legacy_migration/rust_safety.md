# RUST IMPLEMENTATION GUIDELINES - OMNICORP MODERNIZATION

## 1. Type Safety
- NEVER use floating point numbers (`f64`, `f32`) for currency.
- Use the `rust_decimal` crate or an integer-based fixed-point representation (micros).

## 2. Error Handling
- No `unwrap()` or `expect()`. Use `Result` and propagate errors.
- Legacy logic failures should return `LegacyMigrationError::LogicMismatch`.

## 3. Variable Naming
- Use `snake_case`.
- Do NOT use Hungarian notation (e.g., no `fBalance`).
- Do NOT use COBOL-style variable names (e.g., `CALCULATED-INTEREST` -> `calculated_interest`).

## 4. Testing
- Every legacy quirk must have a corresponding unit test case.
- Use property-based testing (`proptest`) to verify rounding behavior against the legacy implementation.
