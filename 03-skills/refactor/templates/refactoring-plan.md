# Refactoring Plan Template

Use this template to document and track your refactoring effort.

---

## Project Information

| Field | Value |
|-------|-------|
| **Project/Module** | [Project name] |
| **Target Files** | [List of files to refactor] |
| **Date Created** | [Date] |
| **Author** | [Name] |
| **Status** | Draft / In Review / Approved / In Progress / Completed |

---

## Executive Summary

### Goals
- [ ] [Primary goal: e.g., Improve readability of payment processing]
- [ ] [Secondary goal: e.g., Reduce code duplication]
- [ ] [Tertiary goal: e.g., Improve testability]

### Constraints
- [ ] [Constraint 1: e.g., Cannot change public API]
- [ ] [Constraint 2: e.g., Must maintain backward compatibility]
- [ ] [Constraint 3: e.g., No changes to database schema]

### Risk Level
- [ ] Low - Minor changes, well-tested code
- [ ] Medium - Moderate changes, some risk
- [ ] High - Significant changes, careful attention needed

---

## Pre-Refactoring Checklist

### Test Coverage Assessment

| Metric | Current | Target | Status |
|--------|---------|--------|--------|
| Unit Test Coverage | __%  | ≥80% | |
| Integration Tests | Yes/No | Yes | |
| All Tests Passing | Yes/No | Yes | |

### Required Before Starting
- [ ] All tests passing
- [ ] Code reviewed and understood
- [ ] Backup/version control in place
- [ ] User approval obtained

---

## Identified Code Smells

### Summary

| # | Smell | Location | Severity | Priority |
|---|-------|----------|----------|----------|
| 1 | [e.g., Long Method] | [file:line] | High | P1 |
| 2 | [e.g., Duplicate Code] | [file:line] | Medium | P2 |
| 3 | [e.g., Feature Envy] | [file:line] | Low | P3 |

### Detailed Analysis

#### Smell #1: [Name]

**Location**: `path/to/file.js:45-120`

**Description**: [Detailed description of the problem]

**Impact**:
- [Impact 1]
- [Impact 2]

**Proposed Solution**: [Brief overview of how to fix]

---

## Refactoring Phases

### Phase A: Quick Wins (Low Risk)

**Objective**: Simple improvements with immediate value

**Estimated Changes**: [X files, Y methods]

**User Approval Required**: Yes / No

| # | Task | File | Refactoring | Status |
|---|------|------|-------------|--------|
| A1 | Rename variable `x` to `userCount` | utils.js:15 | Rename Variable | [ ] |
| A2 | Remove unused `oldHandler()` | api.js:89 | Remove Dead Code | [ ] |
| A3 | Extract duplicate validation | form.js:23,67 | Extract Method | [ ] |

**Rollback Plan**: Revert commits A1-A3

---

### Phase B: Structural Improvements (Medium Risk)

**Objective**: Improve code organization and clarity

**Estimated Changes**: [X files, Y methods]

**User Approval Required**: Yes

**Dependencies**: Phase A must be complete

| # | Task | File | Refactoring | Status |
|---|------|------|-------------|--------|
| B1 | Extract `calculatePrice()` from long method | order.js:45 | Extract Method | [ ] |
| B2 | Introduce `OrderDetails` parameter object | order.js:12 | Introduce Parameter Object | [ ] |
| B3 | Move `formatAddress()` to Address class | customer.js:78 | Move Method | [ ] |

**Rollback Plan**: Revert to post-Phase-A commit

---

### Phase C: Architectural Changes (Higher Risk)

**Objective**: Address deeper structural issues

**Estimated Changes**: [X files, Y methods]

**User Approval Required**: Yes

**Dependencies**: Phases A and B must be complete

| # | Task | File | Refactoring | Status |
|---|------|------|-------------|--------|
| C1 | Replace price switch with polymorphism | pricing.js:30 | Replace Conditional with Polymorphism | [ ] |
| C2 | Extract `NotificationService` class | user.js:100 | Extract Class | [ ] |

**Rollback Plan**: Revert to post-Phase-B commit

---

## Detailed Refactoring Steps

### Task [ID]: [Task Name]

**Smell Addressed**: [Smell name]

**Refactoring Technique**: [Technique name]

**Risk Level**: Low / Medium / High

#### Context

**Before** (Current State):
```javascript
// Paste current code here
```

**After** (Expected State):
```javascript
// Paste expected code here
```

#### Step-by-Step Mechanics

1. [ ] **Step 1**: [Description]
   - Test: Run tests after this step
   - Expected: All tests pass

2. [ ] **Step 2**: [Description]
   - Test: Run tests after this step
   - Expected: All tests pass

3. [ ] **Step 3**: [Description]
   - Test: Run tests after this step
   - Expected: All tests pass

#### Verification

- [ ] All tests passing
- [ ] Behavior unchanged
- [ ] Code compiles
- [ ] No new warnings

#### Commit Message
```
refactor: [Describe the refactoring]
```

---

## Progress Tracking

### Phase Status

| Phase | Status | Started | Completed | Tests Passing |
|-------|--------|---------|-----------|---------------|
| A | Not Started / In Progress / Done | | | |
| B | Not Started / In Progress / Done | | | |
| C | Not Started / In Progress / Done | | | |

### Issues Encountered

| # | Issue | Resolution | Status |
|---|-------|------------|--------|
| 1 | [Description] | [How resolved] | Open / Resolved |

---

## Metrics Comparison

### Before Refactoring

| Metric | File 1 | File 2 | Total |
|--------|--------|--------|-------|
| Lines of Code | | | |
| Cyclomatic Complexity | | | |
| Maintainability Index | | | |
| Number of Methods | | | |
| Avg Method Length | | | |

### After Refactoring

| Metric | File 1 | File 2 | Total | Change |
|--------|--------|--------|-------|--------|
| Lines of Code | | | | |
| Cyclomatic Complexity | | | | |
| Maintainability Index | | | | |
| Number of Methods | | | | |
| Avg Method Length | | | | |

---

## Post-Refactoring Checklist

- [ ] All tests passing
- [ ] No new warnings or errors
- [ ] Code compiles successfully
- [ ] Manual verification completed
- [ ] Documentation updated (if needed)
- [ ] Code reviewed
- [ ] Metrics improved
- [ ] User sign-off obtained

---

## Lessons Learned

### What Went Well
- [Item 1]
- [Item 2]

### What Could Be Improved
- [Item 1]
- [Item 2]

### Recommendations for Future
- [Item 1]
- [Item 2]

---

## Approvals

| Role | Name | Date | Signature |
|------|------|------|-----------|
| Plan Author | | | |
| Technical Lead | | | |
| Product Owner | | | |

---

## Appendix

### A. Related Documentation
- [Link to relevant docs]

### B. Reference Materials
- [Link to code smells catalog]
- [Link to refactoring catalog]

### C. Tools Used
- [Testing framework]
- [Linting tools]
- [Complexity analysis tools]

---

**Last Updated**: August 4, 2026
**Claude Code Version**: 2.1.220
**Sources**:
- https://code.claude.com/docs/en/skills
**Compatible Models**: Claude Fable 5, Claude Opus 5, Claude Sonnet 5, Claude Sonnet 4.6, Claude Opus 4.8, Claude Haiku 4.5
