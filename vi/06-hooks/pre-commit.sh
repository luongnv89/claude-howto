#!/bin/bash
# Run tests before commit
# Hook: PreToolUse (matcher: Bash) - checks if the command is a git commit
# Note: There is no "PreCommit" hook event. Use PreToolUse with a Bash matcher
# and inspect the command to detect git commit operations.
#
# Mã thoát: 2 chặn lệnh gọi tool và hiển thị stderr làm lý do chặn.
# Bất kỳ giá trị khác 0 nào khác đều là lỗi KHÔNG chặn — commit vẫn tiếp tục.
# Nguồn: https://code.claude.com/docs/en/hooks

echo "🧪 Running tests before commit..."

# Check if package.json exists (Node.js project)
if [ -f "package.json" ]; then
  if grep -q "\"test\":" package.json; then
    npm test
    if [ $? -ne 0 ]; then
      echo "❌ Tests failed! Commit blocked." >&2
      exit 2
    fi
  fi
fi

# Check if pytest is available (Python project)
if [ -f "pytest.ini" ] || [ -f "setup.py" ]; then
  if command -v pytest &> /dev/null; then
    pytest
    if [ $? -ne 0 ]; then
      echo "❌ Tests failed! Commit blocked." >&2
      exit 2
    fi
  fi
fi

# Check if go.mod exists (Go project)
if [ -f "go.mod" ]; then
  go test ./...
  if [ $? -ne 0 ]; then
    echo "❌ Tests failed! Commit blocked." >&2
    exit 2
  fi
fi

# Check if Cargo.toml exists (Rust project)
if [ -f "Cargo.toml" ]; then
  cargo test
  if [ $? -ne 0 ]; then
    echo "❌ Tests failed! Commit blocked." >&2
    exit 2
  fi
fi

echo "✅ All tests passed! Proceeding with commit."
exit 0
