#!/bin/bash
set -euo pipefail

# Installation script for AIML Learning Repository
# Uses UV for fast dependency management

echo "🚀 AIML Learning Repository - Dependency Installation"
echo "======================================================"
echo ""

# Ensure common user-level binary paths are available in this shell.
export PATH="$HOME/.cargo/bin:$HOME/.local/bin:$PATH"

# Check if UV is installed
if ! command -v uv &> /dev/null; then
    echo "❌ UV is not installed!"
    echo ""
    echo "Installing UV..."

    if command -v curl &> /dev/null; then
        if curl -LsSf https://astral.sh/uv/install.sh | sh; then
            echo "✅ UV installed via Astral install script"
        else
            echo "⚠️  Astral install script failed (likely network/SSL)."
            echo "   Falling back to pip user install..."
            python3 -m pip install --user uv
        fi
    elif command -v wget &> /dev/null; then
        if wget -qO- https://astral.sh/uv/install.sh | sh; then
            echo "✅ UV installed via Astral install script"
        else
            echo "⚠️  Astral install script failed (likely network/SSL)."
            echo "   Falling back to pip user install..."
            python3 -m pip install --user uv
        fi
    else
        echo "⚠️  Neither curl nor wget found. Installing UV via pip user install..."
        python3 -m pip install --user uv
    fi

    # Re-export PATH in case installer added uv after shell start.
    export PATH="$HOME/.cargo/bin:$HOME/.local/bin:$PATH"

    if ! command -v uv &> /dev/null; then
        echo "❌ UV installation failed. Please check network/SSL settings and retry."
        exit 1
    fi

    echo "✅ UV installed successfully!"
    echo ""
fi

echo "📦 UV version:"
uv --version
echo ""

# Manage dependencies entirely using uv sync (Handles venv creation and locking)
echo "🔧 Syncing workspace dependencies with uv sync (this is FAST!)..."
uv sync --python 3.11

# Activate virtual environment
echo "🔌 Activating virtual environment..."
source .venv/bin/activate
echo "✅ Virtual environment activated"
echo ""

echo "✅ All dependencies installed successfully and uv.lock updated!"
echo ""

# Print installed packages
echo "📋 Installed packages:"
uv pip list | head -20
echo "..."
echo ""

echo "🎉 Setup complete!"
echo ""
echo "To activate the environment in the future, run:"
echo "  source .venv/bin/activate"
echo ""
echo "To install optional dev dependencies:"
echo "  uv sync --all-extras    # Includes pytest, black, flake8, mypy"
echo ""
echo "To start Jupyter:"
echo "  uv run jupyter notebook"
echo ""
echo "Happy learning! 🚀"
