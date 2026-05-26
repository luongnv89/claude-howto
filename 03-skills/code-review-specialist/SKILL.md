---
name: code-review-specialist
description: Comprehensive code review with security, performance, and quality analysis. Use when users ask to review code, analyze code quality, evaluate pull requests, or mention code review, security analysis, or performance optimization.
---

# Code Review Skill

This skill provides comprehensive code review capabilities focusing on:

1. **Security Analysis**
   - Authentication/authorization issues
   - Data exposure risks
   - Injection vulnerabilities
   - Cryptographic weaknesses
   - Sensitive data logging

2. **Performance Review**
   - Algorithm efficiency (Big O analysis)
   - Memory optimization
   - Database query optimization
   - Caching opportunities
   - Concurrency issues

3. **Code Quality**
   - SOLID principles
   - Design patterns
   - Naming conventions
   - Documentation
   - Test coverage

4. **Maintainability**
   - Code readability
   - Function size (should be < 50 lines)
   - Cyclomatic complexity
   - Dependency management
   - Type safety

## Reference Files

This skill includes supporting files that you should read when performing reviews:

- **`templates/review-checklist.md`** — Structured checklist covering security, performance, quality, and testing. Read this file and use it as a guide to ensure no category is missed during review.
- **`templates/finding-template.md`** — Standard template for documenting individual findings with severity, location, code examples, and impact analysis. Read this file and use its format when reporting issues.
- **`scripts/analyze-metrics.py`** — Python script that calculates code metrics (function count, class count, average line length, complexity score). Run this on the file under review to gather quantitative data.
- **`scripts/compare-complexity.py`** — Python script that compares cyclomatic and cognitive complexity between two versions of a file. Run this with the before and after versions when reviewing refactoring changes.

## Review Template

For each piece of code reviewed, provide:

### Summary
- Overall quality assessment (1-5)
- Key findings count
- Recommended priority areas

### Critical Issues (if any)
- **Issue**: Clear description
- **Location**: File and line number
- **Impact**: Why this matters
- **Severity**: Critical/High/Medium
- **Fix**: Code example

### Findings by Category

#### Security (if issues found)
List security vulnerabilities with examples

#### Performance (if issues found)
List performance problems with complexity analysis

#### Quality (if issues found)
List code quality issues with refactoring suggestions

#### Maintainability (if issues found)
List maintainability problems with improvements

## Version History

- v1.0.0 (2024-12-10): Initial release with security, performance, quality, and maintainability analysis
