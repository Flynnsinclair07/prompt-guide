#!/usr/bin/env bash
# Install the monthly launchd job for the Concur receipt prep tool (macOS).
#
#   ./install.sh                 # install + load the job
#   ./install.sh --uninstall     # unload + remove the job
set -euo pipefail

LABEL="com.user.concur-receipt-prep"
TOOLDIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
TEMPLATE="$TOOLDIR/$LABEL.plist"
TARGET="$HOME/Library/LaunchAgents/$LABEL.plist"
PYTHON="$(command -v python3)"

if [[ "${1:-}" == "--uninstall" ]]; then
    launchctl unload "$TARGET" 2>/dev/null || true
    rm -f "$TARGET"
    echo "Uninstalled $LABEL."
    exit 0
fi

mkdir -p "$HOME/Library/LaunchAgents" "$HOME/expenses/dad/inbox" "$HOME/expenses/dad/outbox"

# Substitute placeholders into the user's LaunchAgents copy.
sed -e "s|__USER__|$USER|g" \
    -e "s|__TOOLDIR__|$TOOLDIR|g" \
    -e "s|__PYTHON__|$PYTHON|g" \
    "$TEMPLATE" > "$TARGET"

launchctl unload "$TARGET" 2>/dev/null || true
launchctl load "$TARGET"

echo "Installed $LABEL -> runs 1st of each month @ 09:00."
echo "Plist: $TARGET"
echo
echo "When it finishes it posts a native macOS notification (Notification Center)."
echo "Test it now with:  launchctl start $LABEL   (then check ~/expenses/dad/prep.log)"
