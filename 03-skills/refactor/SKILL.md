---
name: refactor
description: Systematic code refactoring based on Martin Fowler's methodology. Use when users ask to refactor code, improve code structure, reduce technical debt, clean up legacy code, eliminate code smells, or improve code maintainability. This skill guides through a phased approach with research, planning, and safe incremental implementation.
---

# Code Refactoring Skill

A systematic approach to refactoring code based on Martin Fowler's *Refactoring: Improving the Design of Existing Code* (2nd Edition). This skill emphasizes safe, incremental changes backed by tests.

> "Refactoring is the process of changing a software system in such a way that it does not alter the external behavior of the code yet improves its internal structure." — Martin Fowler

## Core Principles

1. **Behavior Preservation**: External behavior must remain unchanged
2. **Small Steps**: Make tiny, testable changes
3. **Test-Driven**: Tests are the safety net
4. **Continuous**: Refactoring is ongoing, not a one-time event
5. **Collaborative**: User approval required at each phase

## Workflow Overview

```
Phase 1: Research & Analysis
    ↓
Phase 2: Test Coverage Assessment
    ↓
Phase 3: Code Smell Identification
    ↓
Phase 4: Refactoring Plan Creation
    ↓
Phase 5: Incremental Implementation
    ↓
Phase 6: Review & Iteration
```

---

## Phase 1: Research & Analysis

### Objectives
- Understand the codebase structure and purpose
- Identify the scope of refactoring
- Gather context about business requirements

### Questions to Ask User
Before starting, clarify:

1. **Scope**: Which files/modules/functions need refactoring?
2. **Goals**: What problems are you trying to solve? (readability, performance, maintainability)
3. **Constraints**: Are there any areas that should NOT be changed?
4. **Timeline pressure**: Is this blocking other work?
5. **Test status**: Do tests exist? Are they passing?

### Actions
- [ ] Read and understand the target code
- [ ] Identify dependencies and integrations
- [ ] Document current architecture
- [ ] Note any existing technical debt markers (TODOs, FIXMEs)

### Output
Present findings to user:
- Code structure summary
- Identified problem areas
- Initial recommendations
- **Request approval to proceed**

---

## Phase 2: Test Coverage Assessment

### Why Tests Matter
> "Refactoring without tests is like driving without a seatbelt." — Martin Fowler

Tests are the **key enabler** of safe refactoring. Without them, you risk introducing bugs.

### Assessment Steps

1. **Check for existing tests**
   ```bash
   # Look for test files
   find . -name "*test*" -o -name "*spec*" | head -20
   ```

2. **Run existing tests**
   ```bash
   # JavaScript/TypeScript
   npm test

   # Python
   pytest -v

   # Java
   mvn test
   ```

3. **Check coverage (if available)**
   ```bash
   # JavaScript
   npm run test:coverage

   # Python
   pytest --cov=.
   ```

### Decision Point: Ask User

**If tests exist and pass:**
- Proceed to Phase 3

**If tests are missing or incomplete:**
Present options:
1. Write tests first (recommended)
2. Add tests incrementally during refactoring
3. Proceed without tests (risky - requires user acknowledgment)

**If tests are failing:**
- STOP. Fix failing tests before refactoring
- Ask user: Should we fix tests first?

### Test Writing Guidelines (if needed)

For each function being refactored, ensure tests cover:
- Happy path (normal operation)
- Edge cases (empty inputs, null, boundaries)
- Error scenarios (invalid inputs, exceptions)

Use the "red-green-refactor" cycle:
1. Write failing test (red)
2. Make it pass (green)
3. Refactor

---

## Phase 3: Code Smell Identification

### What Are Code Smells?
Symptoms of deeper problems in code. They're not bugs, but indicators that the code could be improved.

### Common Code Smells to Check

See [references/code-smells.md](references/code-smells.md) for the complete catalog.

#### Quick Reference

| Smell | Signs | Impact |
|-------|-------|--------|
| **Long Method** | Methods > 30-50 lines | Hard to understand, test, maintain |
| **Duplicated Code** | Same logic in multiple places | Bug fixes needed in multiple places |
| **Large Class** | Class with too many responsibilities | Violates Single Responsibility |
| **Feature Envy** | Method uses another class's data more | Poor encapsulation |
| **Primitive Obsession** | Overuse of primitives instead of objects | Missing domain concepts |
| **Long Parameter List** | Methods with 4+ parameters | Hard to call correctly |
| **Data Clumps** | Same data items appearing together | Missing abstraction |
| **Switch Statements** | Complex switch/if-else chains | Hard to extend |
| **Speculative Generality** | Code "just in case" | Unnecessary complexity |
| **Dead Code** | Unused code | Confusion, maintenance burden |

### Analysis Steps

1. **Automated Analysis** (if scripts available)
   ```bash
   python scripts/detect-smells.py <file>
   ```

2. **Manual Review**
   - Walk through code systematically
   - Note each smell with location and severity
   - Categorize by impact (Critical/High/Medium/Low)

3. **Prioritization**
   Focus on smells that:
   - Block current development
   - Cause bugs or confusion
   - Affect most-changed code paths

### Output: Smell Report

Present to user:
- List of identified smells with locations
- Severity assessment for each
- Recommended priority order
- **Request approval on priorities**

---

## Phase 4: Refactoring Plan Creation

### Selecting Refactorings

For each smell, select an appropriate refactoring from the catalog.

See [references/refactoring-catalog.md](references/refactoring-catalog.md) for the complete list.

#### Smell-to-Refactoring Mapping

| Code Smell | Recommended Refactoring(s) |
|------------|---------------------------|
| Long Method | Extract Method, Replace Temp with Query |
| Duplicated Code | Extract Method, Pull Up Method, Form Template Method |
| Large Class | Extract Class, Extract Subclass |
| Feature Envy | Move Method, Move Field |
| Primitive Obsession | Replace Primitive with Object, Replace Type Code with Class |
| Long Parameter List | Introduce Parameter Object, Preserve Whole Object |
| Data Clumps | Extract Class, Introduce Parameter Object |
| Switch Statements | Replace Conditional with Polymorphism |
| Speculative Generality | Collapse Hierarchy, Inline Class, Remove Dead Code |
| Dead Code | Remove Dead Code |

### Plan Structure

Use the template at [templates/refactoring-plan.md](templates/refactoring-plan.md).

For each refactoring:
1. **Target**: What code will change
2. **Smell**: What problem it addresses
3. **Refactoring**: Which technique to apply
4. **Steps**: Detailed micro-steps
5. **Risks**: What could go wrong
6. **Rollback**: How to undo if needed

### Phased Approach

**CRITICAL**: Introduce refactoring gradually in phases.

**Phase A: Quick Wins** (Low risk, high value)
- Rename variables for clarity
- Extract obvious duplicate code
- Remove dead code

**Phase B: Structural Improvements** (Medium risk)
- Extract methods from long functions
- Introduce parameter objects
- Move methods to appropriate classes

**Phase C: Architectural Changes** (Higher risk)
- Replace conditionals with polymorphism
- Extract classes
- Introduce design patterns

### Decision Point: Present Plan to User

Before implementation:
- Show complete refactoring plan
- Explain each phase and its risks
- Get explicit approval for each phase
- **Ask**: "Should I proceed with Phase A?"

---

## Phase 5: Incremental Implementation

### The Golden Rule
> "Change → Test → Green? → Commit → Next step"

### Implementation Rhythm

For each refactoring step:

1. **Pre-check**
   - Tests are passing (green)
   - Code compiles

2. **Make ONE small change**
   - Follow the mechanics from the catalog
   - Keep changes minimal

3. **Verify**
   - Run tests immediately
   - Check for compilation errors

4. **If tests pass (green)**
   - Commit with descriptive message
   - Move to next step

5. **If tests fail (red)**
   - STOP immediately
   - Undo the change
   - Analyze what went wrong
   - Ask user if unclear

### Commit Strategy

Each commit should be:
- **Atomic**: One logical change
- **Reversible**: Easy to revert
- **Descriptive**: Clear commit message

Example commit messages:
```
refactor: Extract calculateTotal() from processOrder()
refactor: Rename 'x' to 'customerCount' for clarity
refactor: Remove unused validateOldFormat() method
```

### Progress Reporting

After each sub-phase, report to user:
- Changes made
- Tests still passing?
- Any issues encountered
- **Ask**: "Continue with next batch?"

---

## Phase 6: Review & Iteration

### Post-Refactoring Checklist

- [ ] All tests passing
- [ ] No new warnings/errors
- [ ] Code compiles successfully
- [ ] Behavior unchanged (manual verification)
- [ ] Documentation updated if needed
- [ ] Commit history is clean

### Metrics Comparison

Run complexity analysis before and after:
```bash
python scripts/analyze-complexity.py <file>
```

Present improvements:
- Lines of code change
- Cyclomatic complexity change
- Maintainability index change

### User Review

Present final results:
- Summary of all changes
- Before/after code comparison
- Metrics improvements
- Remaining technical debt
- **Ask**: "Are you satisfied with these changes?"

### Next Steps

Discuss with user:
- Additional smells to address?
- Schedule follow-up refactoring?
- Apply similar changes elsewhere?

---

## Important Guidelines

### When to STOP and Ask

Always pause and consult user when:
- Unsure about business logic
- Change might affect external APIs
- Test coverage is inadequate
- Significant architectural decision needed
- Risk level increases
- You encounter unexpected complexity

### Safety Rules

1. **Never refactor without tests** (unless user explicitly acknowledges risk)
2. **Never make big changes** - break into tiny steps
3. **Never skip the test run** after each change
4. **Never continue if tests fail** - fix or rollback first
5. **Never assume** - when in doubt, ask

### What NOT to Do

- Don't combine refactoring with feature additions
- Don't refactor during production emergencies
- Don't refactor code you don't understand
- Don't over-engineer - keep it simple
- Don't refactor everything at once

---

## Quick Start Example

### Scenario: Long Method with Duplication

**Before:**
```javascript
function processOrder(order) {
  // 150 lines of code with:
  // - Duplicated validation logic
  // - Inline calculations
  // - Mixed responsibilities
}
```

**Refactoring Steps:**

1. **Ensure tests exist** for processOrder()
2. **Extract** validation into validateOrder()
3. **Test** - should pass
4. **Extract** calculation into calculateOrderTotal()
5. **Test** - should pass
6. **Extract** notification into notifyCustomer()
7. **Test** - should pass
8. **Review** - processOrder() now orchestrates 3 clear functions

**After:**
```javascript
function processOrder(order) {
  validateOrder(order);
  const total = calculateOrderTotal(order);
  notifyCustomer(order, total);
  return { order, total };
}
```

---

## References

- [Code Smells Catalog](references/code-smells.md) - Complete list of code smells
- [Refactoring Catalog](references/refactoring-catalog.md) - Refactoring techniques
- [Refactoring Plan Template](templates/refactoring-plan.md) - Planning template

## Scripts

- `scripts/analyze-complexity.py` - Analyze code complexity metrics
- `scripts/detect-smells.py` - Automated smell detection

## Version History

- v1.0.0 (2025-01-15): Initial release with Fowler methodology, phased approach, user consultation points

---

**Last Updated**: August 4, 2026
**Claude Code Version**: 2.1.220
**Sources**:
- https://code.claude.com/docs/en/skills
**Compatible Models**: Claude Fable 5, Claude Opus 5, Claude Sonnet 5, Claude Sonnet 4.6, Claude Opus 4.8, Claude Haiku 4.5
