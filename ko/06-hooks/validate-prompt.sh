#!/bin/bash
# Validate user prompts
# Hook: UserPromptSubmit
#
# Reads the user prompt from stdin JSON and blocks dangerous operations.
#
# Compatible with: macOS, Linux, Windows (Git Bash)

# Read JSON input from stdin (Claude Code hook protocol)
INPUT=$(cat)

# Extract the prompt text from JSON input
# Claude Code sends UserPromptSubmit with field "user_prompt" (falls back to "prompt")
PROMPT=$(echo "$INPUT" | sed -n 's/.*"user_prompt"[[:space:]]*:[[:space:]]*"\([^"]*\)".*/\1/p' | head -1)
if [ -z "$PROMPT" ]; then
  PROMPT=$(echo "$INPUT" | sed -n 's/.*"prompt"[[:space:]]*:[[:space:]]*"\([^"]*\)".*/\1/p' | head -1)
fi

if [ -z "$PROMPT" ]; then
  exit 0
fi

# Check for dangerous operations
DANGEROUS_PATTERNS=(
  "rm -rf /"
  "delete database"
  "drop database"
  "format disk"
  "dd if="
)

for pattern in "${DANGEROUS_PATTERNS[@]}"; do
  if echo "$PROMPT" | grep -qi "$pattern"; then
    printf '{"decision": "block", "reason": "Dangerous operation detected: %s"}' "$pattern"
    exit 0
  fi
done

# Check for production deployments
if echo "$PROMPT" | grep -qiE "(deploy|push).*production"; then
  if [ ! -f ".deployment-approved" ]; then
    echo '{"decision": "block", "reason": "Production deployment requires approval. Create .deployment-approved file to proceed."}'
    exit 0
  fi
fi

# Check for required context in certain operations
if echo "$PROMPT" | grep -qi "refactor"; then
  if [ ! -d "tests" ] && [ ! -d "test" ]; then
    printf '{"additionalContext": "Warning: Refactoring without tests may be risky. Consider writing tests first."}'
  fi
fi

exit 0
