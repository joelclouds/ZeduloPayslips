#!/usr/bin/env bash

pushd scripts

# ZeduloPayslips Uninstaller
# Removes application files, configuration, and desktop entries

echo "🗑️  Uninstalling ZeduloPayslips..."

# Get script directory and project root
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(dirname "$SCRIPT_DIR")"

# Remove application data and config
echo "   Removing application data..."
rm -r "$HOME/.zedulopayslips"
rm -r "$HOME/zedulopayslips"  # Remove old data folder if exists

# Remove virtual environment
echo "   Removing virtual environment..."
rm -r "$PROJECT_ROOT/venv"

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

# Optional: Remove system-wide desktop entry (commented out by default)
# if [ -f "/usr/share/applications/zedulopayslips.desktop" ]; then
#     sudo rm "/usr/share/applications/zedulopayslips.desktop"
#     sudo update-desktop-database
# fi

# Remove PyInstaller build artifacts
echo "   Cleaning build artifacts..."
rm -r "$PROJECT_ROOT/build"
rm -r "$PROJECT_ROOT/dist"
rm "$PROJECT_ROOT"/*.spec
rm -r "$PROJECT_ROOT/bin"

# Ask about removing the entire project
echo ""
read -p "❓ Remove the entire project folder? (y/N): " -n 1 -r
echo ""
if [[ $REPLY =~ ^[Yy]$ ]]; then
    echo "   Removing project folder..."
    cd "$HOME"  # Move out of project folder before deleting
    rm -r "$PROJECT_ROOT"
    echo "✅ Project folder removed"
else
    echo "✅ Project folder kept at: $PROJECT_ROOT"
fi

echo ""
echo "✅ ZeduloPayslips has been uninstalled!"

popd
