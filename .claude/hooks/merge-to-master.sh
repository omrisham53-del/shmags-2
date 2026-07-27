#!/bin/bash
set -uo pipefail

# Only run in remote (Cowork) sessions -- desktop sessions merge manually.
if [ "${CLAUDE_CODE_REMOTE:-}" != "true" ]; then
  exit 0
fi

REPO="$CLAUDE_PROJECT_DIR"
cd "$REPO" 2>/dev/null || exit 0
git rev-parse --git-dir >/dev/null 2>&1 || exit 0
[ -z "$(git remote 2>/dev/null)" ] && exit 0

current_branch=$(git branch --show-current 2>/dev/null)
[ -z "$current_branch" ] && exit 0
[ "$current_branch" = "master" ] && exit 0

git fetch origin master --quiet 2>/dev/null

# Nothing to merge if this branch has no commits master doesn't have.
ahead=$(git rev-list --count "origin/master..origin/$current_branch" 2>/dev/null || echo 0)
[ "$ahead" -eq 0 ] 2>/dev/null && exit 0

WT_DIR=$(mktemp -d)
cleanup() { git worktree remove -f "$WT_DIR" >/dev/null 2>&1; }
trap cleanup EXIT

if ! git worktree add -q "$WT_DIR" origin/master 2>/dev/null; then
  exit 0
fi

if git -C "$WT_DIR" merge --no-ff -q \
    -m "Merge $current_branch into master (auto, session sync)" \
    "origin/$current_branch" 2>/dev/null; then
  if git -C "$WT_DIR" push origin HEAD:master -q 2>/dev/null; then
    echo "{\"systemMessage\": \"Auto-merged branch '$current_branch' into master and pushed.\"}"
  else
    echo "WARNING: merged '$current_branch' into master locally but the push failed (master may have moved). Merge manually: git fetch origin master && git checkout master && git merge origin/$current_branch && git push origin master" >&2
  fi
else
  git -C "$WT_DIR" merge --abort >/dev/null 2>&1
  echo "WARNING: branch '$current_branch' has $ahead commit(s) not in master, and auto-merge hit conflicts. Merge manually before this work becomes invisible to future sessions: git fetch origin master && git checkout master && git merge origin/$current_branch" >&2
fi

exit 0
