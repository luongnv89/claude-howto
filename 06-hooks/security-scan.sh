#!/bin/bash
# Security scan on file write
# Hook: PostToolUse:Write
#
# Scans files for hardcoded secrets, API keys, and credentials.
# Outputs a non-blocking warning via additionalContext when issues are found.
#
# Compatible with: macOS, Linux, Windows (Git Bash)

# Read JSON input from stdin (Claude Code hook protocol)
INPUT=$(cat)

# Extract file_path using sed (compatible with all platforms including Windows Git Bash)
# Avoids grep -P (not available on Windows Git Bash) and python3 dependency
FILE_PATH=$(echo "$INPUT" | sed -n 's/.*"file_path"[[:space:]]*:[[:space:]]*"\([^"]*\)".*/\1/p' | head -1)

if [ -z "$FILE_PATH" ] || [ ! -f "$FILE_PATH" ]; then
  exit 0
fi

# Skip binary files, vendor dirs, and build artifacts
case "$FILE_PATH" in
  *.png|*.jpg|*.jpeg|*.gif|*.svg|*.ico|*.woff|*.woff2|*.ttf|*.eot) exit 0 ;;
  */node_modules/*|*/.git/*|*/dist/*|*/build/*) exit 0 ;;
esac

ISSUES=""

# Check for hardcoded passwords
# Handles both JSON format ("password": "value") and code format (password = 'value')
# Use \\n as separator — it is a valid JSON newline escape and passes through printf safely
if grep -qiE '"password"[[:space:]]*:[[:space:]]*"[^"]+"' "$FILE_PATH" 2>/dev/null; then
  ISSUES="${ISSUES}- WARNING: Potential hardcoded password detected\\n"
elif grep -qiE '(password|passwd|pwd)\s*=\s*'"'"'[^'"'"']+'"'"'' "$FILE_PATH" 2>/dev/null; then
  ISSUES="${ISSUES}- WARNING: Potential hardcoded password detected\\n"
fi

# Check for hardcoded API keys
if grep -qiE '"(api[_-]?key|apikey|access[_-]?token)"[[:space:]]*:[[:space:]]*"[^"]+"' "$FILE_PATH" 2>/dev/null; then
  ISSUES="${ISSUES}- WARNING: Potential hardcoded API key detected\\n"
fi

# Check for hardcoded secrets and tokens
if grep -qiE '(secret|token)\s*=\s*['"'"'"][^'"'"'"]+['"'"'"]' "$FILE_PATH" 2>/dev/null; then
  ISSUES="${ISSUES}- WARNING: Potential hardcoded secret or token detected\\n"
fi

# Check for private keys
if grep -q "BEGIN.*PRIVATE KEY" "$FILE_PATH" 2>/dev/null; then
  ISSUES="${ISSUES}- WARNING: Private key detected\\n"
fi

# Check for AWS keys
if grep -qE "AKIA[0-9A-Z]{16}" "$FILE_PATH" 2>/dev/null; then
  ISSUES="${ISSUES}- WARNING: AWS access key detected\\n"
fi

# Scan with semgrep if available
if command -v semgrep &> /dev/null; then
  semgrep --config=auto "$FILE_PATH" --quiet 2>/dev/null
fi

# Scan with trufflehog if available
if command -v trufflehog &> /dev/null; then
  trufflehog filesystem "$FILE_PATH" --only-verified --quiet 2>/dev/null
fi

# If issues found, output as additionalContext (non-blocking warning)
# Use hookSpecificOutput format required by Claude Code PostToolUse protocol
if [ -n "$ISSUES" ]; then
  # Escape file path for JSON (backslash and double-quote)
  # ISSUES already uses \\n as separator (valid JSON escape) — only escape double-quotes
  SAFE_PATH=$(printf '%s' "$FILE_PATH" | sed 's/\\/\\\\/g; s/"/\\"/g')
  SAFE_ISSUES=$(printf '%s' "$ISSUES" | sed 's/"/\\"/g')
  printf '{"hookSpecificOutput": {"hookEventName": "PostToolUse", "additionalContext": "Security scan found issues in %s:\\n%sPlease review and use environment variables instead."}}' "$SAFE_PATH" "$SAFE_ISSUES"
fi

exit 0
