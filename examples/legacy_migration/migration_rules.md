# Migration Rules - Level 1 (Strict)

1. **NO FLOATS**: All currency calculations must use `big.Int` or `decimal.Decimal` libraries. Standard `float64` is strictly forbidden.
2. **Rounding**: COBOL `ROUNDED` implies "Round Half Up". Ensure the target implementation mimics this exactly.
3. **Variable Names**: Maintain mapping to original COBOL variable names in comments.
