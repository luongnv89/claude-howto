#!/bin/bash
# Security scan on file write
# Hook: PostToolUse:Write

FILE=$1

if [ -z "$FILE" ]; then
  echo "Usage: $0 <file_path>"
  exit 0
fi

echo "🔒 Running security scan on: $FILE"

ISSUES_FOUND=0

# Check for hardcoded passwords
if grep -qE "(password|passwd|pwd)\s*=\s*['\"][^'\"]+['\"]" "$FILE"; then
  echo "⚠️  WARNING: Potential hardcoded password detected in $FILE"
  ISSUES_FOUND=1
fi

# Check for hardcoded API keys
if grep -qE "(api[_-]?key|apikey|access[_-]?token)\s*=\s*['\"][^'\"]+['\"]" "$FILE"; then
  echo "⚠️  WARNING: Potential hardcoded API key detected in $FILE"
  ISSUES_FOUND=1
fi

# Check for hardcoded secrets
if grep -qE "(secret|token)\s*=\s*['\"][^'\"]+['\"]" "$FILE"; then
  echo "⚠️  WARNING: Potential hardcoded secret detected in $FILE"
  ISSUES_FOUND=1
fi

# Check for private keys
if grep -q "BEGIN.*PRIVATE KEY" "$FILE"; then
  echo "⚠️  WARNING: Private key detected in $FILE"
  ISSUES_FOUND=1
fi

# Check for AWS keys
if grep -qE "AKIA[0-9A-Z]{16}" "$FILE"; then
  echo "⚠️  WARNING: AWS access key detected in $FILE"
  ISSUES_FOUND=1
fi

# Scan with semgrep if available
if command -v semgrep &> /dev/null; then
  semgrep --config=auto "$FILE" --quiet 2>/dev/null
fi

# Scan with trufflehog if available
if command -v trufflehog &> /dev/null; then
  trufflehog filesystem "$FILE" --only-verified --quiet 2>/dev/null
fi

if [ $ISSUES_FOUND -eq 0 ]; then
  echo "✅ No security issues found"
fi

# Don't block the operation, just warn
exit 0
