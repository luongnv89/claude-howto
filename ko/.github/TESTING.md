# Testing Guide

This document describes the testing infrastructure for Claude How To.

## Overview

The project uses GitHub Actions to automatically run tests on every push and pull request. Tests cover:

- **Unit Tests**: Python tests using pytest
- **Code Quality**: Linting and formatting with Ruff
- **Security**: Vulnerability scanning with Bandit
- **Type Checking**: Static type analysis with mypy
- **Build Verification**: EPUB generation test

## Running Tests Locally

### Prerequisites

```bash
# Install uv (fast Python package manager)
pip install uv

# Or on macOS with Homebrew
brew install uv
```

### Setup Environment

```bash
# Clone the repository
git clone https://github.com/luongnv89/claude-howto.git
cd claude-howto

# Create virtual environment
uv venv

# Activate it
source .venv/bin/activate  # macOS/Linux
# or
.venv\Scripts\activate     # Windows

# Install development dependencies
uv pip install -r requirements-dev.txt
```

### Run Tests

```bash
# Run all unit tests
pytest scripts/tests/ -v

# Run tests with coverage
pytest scripts/tests/ -v --cov=scripts --cov-report=html

# Run specific test file
pytest scripts/tests/test_build_epub.py -v

# Run specific test function
pytest scripts/tests/test_build_epub.py::test_function_name -v

# Run tests in watch mode (requires pytest-watch)
ptw scripts/tests/
```

### Run Linting

```bash
# Check code formatting
ruff format --check scripts/

# Auto-fix formatting issues
ruff format scripts/

# Run linter
ruff check scripts/

# Auto-fix linter issues
ruff check --fix scripts/
```

### Run Security Scan

```bash
# Run Bandit security scan
bandit -c pyproject.toml -r scripts/ --exclude scripts/tests/

# Generate JSON report
bandit -c pyproject.toml -r scripts/ --exclude scripts/tests/ -f json -o bandit-report.json
```

### Run Type Checking

```bash
# Check types with mypy
mypy scripts/ --ignore-missing-imports --no-implicit-optional
```

## GitHub Actions Workflow

### Triggered On

- **Push** to `main` or `develop` branches (when scripts change)
- **Pull Request** to `main` (when scripts change)
- Manual workflow dispatch

### Jobs

#### 1. Unit Tests (pytest)

- **Runs on**: Ubuntu latest
- **Python versions**: 3.10, 3.11, 3.12
- **What it does**:
  - Installs dependencies from `requirements-dev.txt`
  - Runs pytest with coverage reporting
  - Uploads coverage to Codecov
  - Archives test results and coverage HTML

**Outcome**: If any test fails, the workflow fails (critical)

#### 2. Code Quality (Ruff)

- **Runs on**: Ubuntu latest
- **Python version**: 3.11
- **What it does**:
  - Checks code formatting with `ruff format`
  - Runs linter with `ruff check`
  - Reports issues but doesn't fail the workflow

**Outcome**: Non-blocking (warning only)

#### 3. Security Scan (Bandit)

- **Runs on**: Ubuntu latest
- **Python version**: 3.11
- **What it does**:
  - Scans for security vulnerabilities
  - Generates JSON report
  - Uploads report as artifact

**Outcome**: Non-blocking (warning only)

#### 4. Type Checking (mypy)

- **Runs on**: Ubuntu latest
- **Python version**: 3.11
- **What it does**:
  - Performs static type analysis
  - Reports type mismatches
  - Helps catch bugs early

**Outcome**: Non-blocking (warning only)

#### 5. Build EPUB

- **Runs on**: Ubuntu latest
- **Depends on**: pytest, lint, security (all must pass)
- **What it does**:
  - Builds the EPUB file using `scripts/build_epub.py`
  - Verifies the EPUB was created successfully
  - Uploads EPUB as artifact

**Outcome**: If build fails, the workflow fails (critical)

#### 6. Summary

- **Runs on**: Ubuntu latest
- **Depends on**: All other jobs
- **What it does**:
  - Generates workflow summary
  - Lists all artifacts
  - Reports overall status

## Writing Tests

### Test Structure

Tests should be placed in `scripts/tests/` with names like `test_*.py`:

```python
# scripts/tests/test_example.py
import pytest
from scripts.example_module import some_function

def test_basic_functionality():
    """Test that some_function works correctly."""
    result = some_function("input")
    assert result == "expected_output"

def test_error_handling():
    """Test that some_function handles errors gracefully."""
    with pytest.raises(ValueError):
        some_function("invalid_input")

@pytest.mark.asyncio
async def test_async_function():
    """Test async functions."""
    result = await async_function()
    assert result is not None
```

### Test Best Practices

- **Use descriptive names**: `test_function_returns_correct_value()`
- **One assertion per test** (when possible): Easier to debug failures
- **Use fixtures** for reusable setup: See `scripts/tests/conftest.py`
- **Mock external services**: Use `unittest.mock` or `pytest-mock`
- **Test edge cases**: Empty inputs, None values, errors
- **Keep tests fast**: Avoid sleep() and external I/O
- **Use pytest markers**: `@pytest.mark.slow` for slow tests

### Fixtures

Common fixtures are defined in `scripts/tests/conftest.py`:

```python
# Use fixtures in your tests
def test_something(tmp_path):
    """tmp_path fixture provides temporary directory."""
    test_file = tmp_path / "test.txt"
    test_file.write_text("content")
    assert test_file.read_text() == "content"
```

## Coverage Reports

### Local Coverage

```bash
# Generate coverage report
pytest scripts/tests/ --cov=scripts --cov-report=html

# Open the coverage report in your browser
open htmlcov/index.html
```

### Coverage Goals

- **Minimum coverage**: 80%
- **Branch coverage**: Enabled
- **Focus areas**: Core functionality and error paths

## Pre-commit Hooks

The project uses pre-commit hooks to run checks automatically before commits:

```bash
# Install pre-commit hooks
pre-commit install

# Run hooks manually
pre-commit run --all-files

# Skip hooks for a commit (not recommended)
git commit --no-verify
```

Configured hooks in `.pre-commit-config.yaml`:
- Ruff formatter
- Ruff linter
- Bandit security scanner
- YAML validation
- File size checks
- Merge conflict detection

## Troubleshooting

### Tests Pass Locally but Fail in CI

Common causes:
1. **Python version difference**: CI uses 3.10, 3.11, 3.12
2. **Missing dependencies**: Update `requirements-dev.txt`
3. **Platform differences**: Path separators, environment variables
4. **Flaky tests**: Tests that depend on timing or order

Solution:
```bash
# Test with the same Python versions
uv python install 3.10 3.11 3.12

# Test with clean environment
rm -rf .venv
uv venv
uv pip install -r requirements-dev.txt
pytest scripts/tests/
```

### Bandit Reports False Positives

Some security warnings may be false positives. Configure in `pyproject.toml`:

```toml
[tool.bandit]
exclude_dirs = ["scripts/tests"]
skips = ["B101"]  # Skip assert_used warning
```

### Type Checking Too Strict

Relax type checking for specific files:

```python
# Add at the top of file
# type: ignore

# Or for specific lines
some_dynamic_code()  # type: ignore
```

## Continuous Integration Best Practices

1. **Keep tests fast**: Each test should complete in <1 second
2. **Don't test external APIs**: Mock external services
3. **Test in isolation**: Each test should be independent
4. **Use clear assertions**: `assert x == 5` not `assert x`
5. **Handle async tests**: Use `@pytest.mark.asyncio`
6. **Generate reports**: Coverage, security, type checking

## Resources

- [pytest Documentation](https://docs.pytest.org/)
- [Ruff Documentation](https://docs.astral.sh/ruff/)
- [Bandit Documentation](https://bandit.readthedocs.io/)
- [mypy Documentation](https://mypy.readthedocs.io/)
- [GitHub Actions Documentation](https://docs.github.com/en/actions)

## Contributing Tests

When submitting a PR:

1. **Write tests** for new functionality
2. **Run tests locally**: `pytest scripts/tests/ -v`
3. **Check coverage**: `pytest scripts/tests/ --cov=scripts`
4. **Run linting**: `ruff check scripts/`
5. **Security scan**: `bandit -r scripts/ --exclude scripts/tests/`
6. **Update documentation** if tests change

Tests are required for all PRs! 🧪

---

For questions or issues with testing, open a GitHub issue or discussion.
