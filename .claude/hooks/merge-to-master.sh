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

LOG="$REPO/.claude/hooks/sync-log.txt"
log() { echo "$(date -u +%Y-%m-%dT%H:%M:%SZ) $1" >> "$LOG" 2>/dev/null || true; }

# Autosave first, unconditionally. A remote session's sandbox can disappear
# before anyone remembers to run `git commit` -- this makes that moment
# never matter. Every Stop event commits whatever is sitting uncommitted,
# so the only way to lose work is the sandbox dying mid-turn, not a missed
# commit.
if [ -n "$(git status --porcelain 2>/dev/null)" ]; then
  git add -A
  if git commit -q -m "Autosave (uncommitted changes, auto)" 2>/dev/null; then
    log "autosaved uncommitted changes"
  fi
fi

current_branch=$(git branch --show-current 2>/dev/null)
if [ -z "$current_branch" ]; then
  log "WARNING: detached HEAD or no branch, could not sync"
  exit 0
fi

if [ "$current_branch" = "master" ]; then
  # Autosaved (or any other) commits sitting on master still need pushing.
  if ! git push origin master -q 2>/dev/null; then
    log "WARNING: push to master failed"
    echo "WARNING: push to master failed -- work may be stuck in this sandbox only. Check: git status && git log origin/master..master" >&2
  fi
  exit 0
fi

# Push the branch itself before checking what's ahead -- a local commit that
# never reached origin is invisible to the "ahead" check below otherwise.
if ! git push origin "$current_branch" -q 2>/dev/null; then
  log "WARNING: push of branch $current_branch to origin failed"
fi

git fetch origin master --quiet 2>/dev/null

# Nothing to merge if this branch has no commits master doesn't have.
ahead=$(git rev-list --count "origin/master..origin/$current_branch" 2>/dev/null || echo 0)
if [ "$ahead" -eq 0 ] 2>/dev/null; then
  log "branch $current_branch has nothing new to merge"
  exit 0
fi

WT_DIR=$(mktemp -d)
cleanup() { git worktree remove -f "$WT_DIR" >/dev/null 2>&1; }
trap cleanup EXIT

if ! git worktree add -q "$WT_DIR" origin/master 2>/dev/null; then
  log "WARNING: could not create worktree to merge $current_branch"
  exit 0
fi

if git -C "$WT_DIR" merge --no-ff -q \
    -m "Merge $current_branch into master (auto, session sync)" \
    "origin/$current_branch" 2>/dev/null; then
  if git -C "$WT_DIR" push origin HEAD:master -q 2>/dev/null; then
    log "merged and pushed $current_branch into master"
    echo "{\"systemMessage\": \"Auto-merged branch '$current_branch' into master and pushed.\"}"
  else
    log "WARNING: merged $current_branch locally but push to master failed"
    echo "WARNING: merged '$current_branch' into master locally but the push failed (master may have moved). Merge manually: git fetch origin master && git checkout master && git merge origin/$current_branch && git push origin master" >&2
  fi
else
  git -C "$WT_DIR" merge --abort >/dev/null 2>&1
  log "WARNING: merge conflict merging $current_branch, not merged"
  echo "WARNING: branch '$current_branch' has $ahead commit(s) not in master, and auto-merge hit conflicts. Merge manually before this work becomes invisible to future sessions: git fetch origin master && git checkout master && git merge origin/$current_branch" >&2
fi

exit 0
