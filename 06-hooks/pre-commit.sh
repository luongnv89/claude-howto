#!/bin/bash
# Run tests before commit
# Hook: PreCommit

echo "🧪 Running tests before commit..."

# Check if package.json exists (Node.js project)
if [ -f "package.json" ]; then
  if grep -q "\"test\":" package.json; then
    npm test
    if [ $? -ne 0 ]; then
      echo "❌ Tests failed! Commit blocked."
      exit 1
    fi
  fi
fi

# Check if pytest is available (Python project)
if [ -f "pytest.ini" ] || [ -f "setup.py" ]; then
  if command -v pytest &> /dev/null; then
    pytest
    if [ $? -ne 0 ]; then
      echo "❌ Tests failed! Commit blocked."
      exit 1
    fi
  fi
fi

# Check if go.mod exists (Go project)
if [ -f "go.mod" ]; then
  go test ./...
  if [ $? -ne 0 ]; then
    echo "❌ Tests failed! Commit blocked."
    exit 1
  fi
fi

# Check if Cargo.toml exists (Rust project)
if [ -f "Cargo.toml" ]; then
  cargo test
  if [ $? -ne 0 ]; then
    echo "❌ Tests failed! Commit blocked."
    exit 1
  fi
fi

echo "✅ All tests passed! Proceeding with commit."
exit 0
