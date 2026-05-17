#!/bin/bash
set -euo pipefail

# Only run in remote (web) sessions - desktop handles git pull manually
if [ "${CLAUDE_CODE_REMOTE:-}" != "true" ]; then
  exit 0
fi

git -C "$CLAUDE_PROJECT_DIR" pull --ff-only origin master
