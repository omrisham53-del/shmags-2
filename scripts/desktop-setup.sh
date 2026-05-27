#!/bin/bash
# Run this once on your desktop inside the shmags-2 folder.
# Sets up two git shortcuts for your daily workflow.

git config alias.start '!git pull origin master'
git config alias.done '!f() { git add -A && git commit -m "${1:-sync}" && git push origin master; }; f'

echo "Done. Your desktop workflow:"
echo "  git start        — pull latest before you begin"
echo "  git done 'msg'   — commit everything and push when finished"
