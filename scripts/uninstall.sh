#!/usr/bin/env bash

pushd scripts &> /dev/null 2>&1

# ZeduloPayslips Uninstaller
# Removes application files, configuration, and desktop entries

echo "🗑️  Uninstalling ZeduloPayslips..."

# Remove application data and config
echo "   Removing application data..."
rm -rf "$HOME/.zedulopayslips" &> /dev/null
rm -rf "$HOME/zedulopayslips" &> /dev/null

# Remove desktop entry (user space)
echo "   Removing desktop entry..."
DESKTOP_FILE="$HOME/.local/share/applications/zedulopayslips.desktop"
if [ -f "$DESKTOP_FILE" ]; then
    rm "$DESKTOP_FILE"
    echo "   Desktop entry removed"

    # Update desktop database
    update-desktop-database "$HOME/.local/share/applications" 2>/dev/null || true
else
    echo "   No desktop entry found"
fi

echo "✅ ZeduloPayslips has been uninstalled!"

popd &> /dev/null
