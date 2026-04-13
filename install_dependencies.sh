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

INSTALL_AI_DEV_TOOLS="${INSTALL_AI_DEV_TOOLS:-0}"

# Manage dependencies entirely using uv sync (Handles venv creation and locking)
echo "🔧 Syncing workspace dependencies with uv sync (this is FAST!)..."
uv sync --python 3.11

if [[ -f package.json ]]; then
    if command -v npm &> /dev/null; then
        echo "📦 Installing Node-based developer tools from package.json..."
        npm install
        echo "✅ Node-based developer tools installed"
        echo ""
    else
        echo "⚠️  npm not found. Skipping Node-based developer tools (for example OpenCode)."
        echo "   Install Node.js and rerun 'npm install' if you want those CLIs locally."
        echo ""
    fi
fi

if [[ "$INSTALL_AI_DEV_TOOLS" == "1" ]]; then
    if [[ -f requirements-ai-dev-tools.txt ]]; then
        if command -v python3.12 &> /dev/null; then
            echo "🧰 Creating dedicated AI developer tools environment (.venv-ai-dev-tools)..."
            uv venv --python 3.12 .venv-ai-dev-tools
            uv pip install --python .venv-ai-dev-tools/bin/python -r requirements-ai-dev-tools.txt
            echo "✅ Dedicated AI developer tools environment created"
            echo ""
        else
            echo "⚠️  INSTALL_AI_DEV_TOOLS=1 was set, but python3.12 is not available."
            echo "   Skipping dedicated OpenHands environment setup."
            echo ""
        fi
    fi
fi

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
echo "To install the dedicated AI developer tools environment (OpenHands on Python 3.12):"
echo "  INSTALL_AI_DEV_TOOLS=1 ./install_dependencies.sh"
echo ""
echo "To start Jupyter:"
echo "  uv run jupyter notebook"
echo ""
echo "Happy learning! 🚀"
