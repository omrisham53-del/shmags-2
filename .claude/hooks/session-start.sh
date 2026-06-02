#!/bin/bash
set -euo pipefail

TODAY=$(date +%Y-%m-%d)
FILE="$CLAUDE_PROJECT_DIR/today.md"

# Update date fields in today.md on every session start
if [ -f "$FILE" ]; then
  sed -i "s|^# Today - .*|# Today - $TODAY|" "$FILE"
  sed -i "s|^\*\*Date:\*\* .*|**Date:** $TODAY|" "$FILE"
  sed -i "s|^\*\*Updated:\*\* .*|**Updated:** $TODAY|" "$FILE"
fi

# Only git pull in remote (Cowork) sessions - desktop pulls manually
if [ "${CLAUDE_CODE_REMOTE:-}" != "true" ]; then
  exit 0
fi

git -C "$CLAUDE_PROJECT_DIR" pull --ff-only origin master
