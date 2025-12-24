# Change: Fix Context Usage Hook Token Calculation

## Why

The context-usage hook (Stop event) always reports 0 tokens because of a bug in line 68 of `context-usage.py`:

```python
estimated_tokens = estimate_tokens(str(total_chars))
```

This converts the integer `total_chars` (e.g., `156789`) to a string `"156789"` and then calculates tokens from that 6-character string, resulting in `6 // 4 = 1` token instead of `156789 // 4 = ~39,197` tokens.

**Current behavior:**
```
Stop says: Context: ~0/200,000 tokens (100.0% remaining)
```

**Expected behavior:**
```
Stop says: Context: ~39,197/200,000 tokens (80.4% remaining)
```

## What

Fix the token calculation bug in the context-usage.py example hook:
1. Remove the erroneous `str()` conversion
2. Calculate estimated tokens directly from character count

## Scope

- **Files affected:**
  - `06-hooks/README.md` - Update the example code
  - User's `~/.claude/hooks/context-usage.py` - Not managed by this repo, but fix will be documented

## Out of Scope

- Improving transcript parsing logic
- Adding more sophisticated token estimation
- Adding new hook features

## Risks

- **Low:** Simple bug fix with clear expected behavior
- Users who copied the broken example will need to update their hook manually
