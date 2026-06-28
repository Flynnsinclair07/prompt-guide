#!/usr/bin/env bash
# Manual run wrapper — prep whatever is in the inbox right now.
#
#   ./run.sh                 # prep previous month's receipts
#   ./run.sh --month 2026-05 # prep a specific month label
#   ./run.sh --dry-run       # show what would happen, write nothing
#   ./run.sh --crop          # also try to crop to receipt bounds
set -euo pipefail
TOOLDIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
exec python3 "$TOOLDIR/prep_receipts.py" "$@"
