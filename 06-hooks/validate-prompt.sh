#!/bin/bash
# Validate user prompts
# Hook: UserPromptSubmit

# Read prompt from stdin
PROMPT=$(cat)

echo "🔍 Validating prompt..."

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
    echo "❌ Blocked: Dangerous operation detected: $pattern"
    exit 1
  fi
done

# Check for production deployments
if echo "$PROMPT" | grep -qiE "(deploy|push).*production"; then
  if [ ! -f ".deployment-approved" ]; then
    echo "❌ Blocked: Production deployment requires approval"
    echo "Create .deployment-approved file to proceed"
    exit 1
  fi
fi

# Check for required context in certain operations
if echo "$PROMPT" | grep -qi "refactor"; then
  if [ ! -f "tests/" ] && [ ! -f "test/" ]; then
    echo "⚠️  Warning: Refactoring without tests may be risky"
  fi
fi

echo "✅ Prompt validation passed"
exit 0
