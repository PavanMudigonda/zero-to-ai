#!/bin/bash
set -e

# Installation script for AIML Learning Repository
# Uses UV for fast dependency management

echo "🚀 AIML Learning Repository - Dependency Installation"
echo "======================================================"
echo ""

# Check if UV is installed
if ! command -v uv &> /dev/null; then
    echo "❌ UV is not installed!"
    echo ""
    echo "Installing UV..."
    curl -LsSf https://astral.sh/uv/install.sh | sh
    
    # Add UV to PATH for current session
    export PATH="$HOME/.cargo/bin:$PATH"
    
    echo "✅ UV installed successfully!"
    echo ""
fi

echo "📦 UV version:"
uv --version
echo ""

# Create virtual environment with UV
echo "🔧 Creating virtual environment..."
uv venv .venv
echo "✅ Virtual environment created at .venv/"
echo ""

# Activate virtual environment
echo "🔌 Activating virtual environment..."
source .venv/bin/activate
echo "✅ Virtual environment activated"
echo ""

# Install dependencies using UV
echo "📥 Installing dependencies with UV (this is FAST!)..."
echo ""

# Install main dependencies from pyproject.toml
uv pip install -e .

echo ""
echo "✅ All dependencies installed successfully!"
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
echo "  uv pip install -e '.[dev]'    # pytest, black, flake8, mypy"
echo ""
echo "To start Jupyter:"
echo "  jupyter notebook"
echo ""
echo "Happy learning! 🚀"
