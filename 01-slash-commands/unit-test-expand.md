---
name: Expand Unit Tests
description: Increase test coverage by targeting untested branches and edge cases
tags: testing, coverage, unit-tests
---

# Expand Unit Tests

Expand existing unit tests adapted to project's testing framework:

1. **Analyze coverage**: Run coverage report to identify untested branches, edge cases, and low-coverage areas
2. **Identify gaps**: Review code for logical branches, error paths, boundary conditions, null/empty inputs
3. **Write tests** using project's framework:
   - Jest/Vitest/Mocha (JavaScript/TypeScript)
   - pytest/unittest (Python)
   - Go testing/testify (Go)
   - Rust test framework (Rust)
4. **Target specific scenarios**:
   - Error handling and exceptions
   - Boundary values (min/max, empty, null)
   - Edge cases and corner cases
   - State transitions and side effects
5. **Verify improvement**: Run coverage again, confirm measurable increase

Present new test code blocks only. Follow existing test patterns and naming conventions.

---
**Last Updated**: April 2026
