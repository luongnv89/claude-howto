#!/bin/bash
# Auto-format code before writing
# Hook: PreToolUse:Write

FILE=$1

if [ -z "$FILE" ]; then
  echo "Usage: $0 <file_path>"
  exit 1
fi

# Detect file type and format accordingly
case "$FILE" in
  *.js|*.jsx|*.ts|*.tsx)
    if command -v prettier &> /dev/null; then
      echo "Formatting JavaScript/TypeScript file: $FILE"
      prettier --write "$FILE"
    fi
    ;;
  *.py)
    if command -v black &> /dev/null; then
      echo "Formatting Python file: $FILE"
      black "$FILE"
    fi
    ;;
  *.go)
    if command -v gofmt &> /dev/null; then
      echo "Formatting Go file: $FILE"
      gofmt -w "$FILE"
    fi
    ;;
  *.rs)
    if command -v rustfmt &> /dev/null; then
      echo "Formatting Rust file: $FILE"
      rustfmt "$FILE"
    fi
    ;;
  *.java)
    if command -v google-java-format &> /dev/null; then
      echo "Formatting Java file: $FILE"
      google-java-format -i "$FILE"
    fi
    ;;
esac

exit 0
