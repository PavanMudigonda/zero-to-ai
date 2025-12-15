# Troubleshooting Guide

Common issues and solutions for Zero to AI learning path.

## 📋 Table of Contents

- [Installation Issues](#installation-issues)
- [Environment Problems](#environment-problems)
- [Jupyter Notebook Issues](#jupyter-notebook-issues)
- [Package Import Errors](#package-import-errors)
- [GPU/CUDA Issues](#gpucuda-issues)
- [Memory Issues](#memory-issues)
- [Platform-Specific Issues](#platform-specific-issues)
- [Getting More Help](#getting-more-help)

---

## Installation Issues

### Problem: `pip install` fails with permission errors

**Solution:**
```bash
# Use --user flag
pip install --user -r requirements.txt

# Or use virtual environment (recommended)
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### Problem: `conda` command not found

**Solution:**
```bash
# Install Miniconda
# macOS/Linux:
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
bash Miniconda3-latest-Linux-x86_64.sh

# Or download from https://docs.conda.io/en/latest/miniconda.html
# Then restart your terminal
```

### Problem: UV installation fails

**Solution:**
```bash
# Alternative installation methods
# Using pip:
pip install uv

# Using Homebrew (macOS):
brew install uv

# Manual download from:
# https://github.com/astral-sh/uv/releases
```

---

## Environment Problems

### Problem: Wrong Python version

**Solution:**
```bash
# Check Python version
python --version

# Should be Python 3.9 or higher
# If not, install correct version:

# Using conda:
conda create -n aiml-learning python=3.11
conda activate aiml-learning

# Using pyenv:
pyenv install 3.11.0
pyenv local 3.11.0
```

### Problem: Virtual environment not activating

**Solution:**
```bash
# macOS/Linux:
source .venv/bin/activate

# Windows (Command Prompt):
.venv\Scripts\activate.bat

# Windows (PowerShell):
.venv\Scripts\Activate.ps1

# If PowerShell gives execution policy error:
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### Problem: Environment packages not found after activation

**Solution:**
```bash
# Verify environment is active
which python  # macOS/Linux
where python  # Windows

# Should point to .venv/bin/python or similar
# If not, deactivate and reactivate:
deactivate
source .venv/bin/activate

# Reinstall packages:
pip install -r requirements.txt
```

---

## Jupyter Notebook Issues

### Problem: Jupyter not found

**Solution:**
```bash
# Install Jupyter
pip install jupyter notebook

# Verify installation
jupyter --version

# Launch Jupyter
jupyter notebook
```

### Problem: Kernel not found or wrong kernel

**Solution:**
```bash
# Install ipykernel
pip install ipykernel

# Add current environment to Jupyter
python -m ipykernel install --user --name=aiml-learning --display-name "Python (AI/ML)"

# In Jupyter, select: Kernel > Change Kernel > Python (AI/ML)
```

### Problem: Jupyter kernel keeps dying

**Solutions:**
1. **Reduce memory usage:**
   ```python
   # In your notebook, clear variables
   %reset -f
   
   # Import garbage collector
   import gc
   gc.collect()
   ```

2. **Increase memory limits:**
   ```bash
   # Start Jupyter with more memory
   jupyter notebook --NotebookApp.max_buffer_size=1000000000
   ```

3. **Check logs:**
   ```bash
   # View Jupyter logs
   jupyter notebook --debug
   ```

### Problem: Cannot open notebooks

**Solution:**
```bash
# Try opening specific notebook
jupyter notebook path/to/notebook.ipynb

# If file association broken, reinstall:
pip uninstall jupyter notebook
pip install jupyter notebook
```

---

## Package Import Errors

### Problem: `ModuleNotFoundError: No module named 'X'`

**Solution:**
```bash
# Install missing package
pip install package-name

# For common packages:
pip install numpy pandas matplotlib scikit-learn

# For deep learning:
pip install torch torchvision
pip install tensorflow

# For NLP:
pip install transformers tokenizers

# Install everything:
pip install -r requirements.txt
```

### Problem: Import works in terminal but not in Jupyter

**Solution:**
```bash
# Verify Jupyter is using correct Python
# In Jupyter notebook:
import sys
print(sys.executable)

# Should match your virtual environment
# If not, reinstall kernel:
python -m ipykernel install --user --name=aiml-learning --display-name "Python (AI/ML)"
```

### Problem: Package version conflicts

**Solution:**
```bash
# Create fresh environment
conda create -n aiml-fresh python=3.11
conda activate aiml-fresh

# Install packages one group at a time:
pip install numpy pandas matplotlib scikit-learn
pip install torch torchvision
pip install transformers

# Check for conflicts:
pip check
```

---

## GPU/CUDA Issues

### Problem: PyTorch not using GPU

**Solution:**
```python
import torch

# Check CUDA availability
print(f"CUDA available: {torch.cuda.is_available()}")
print(f"CUDA version: {torch.version.cuda}")
print(f"GPU device: {torch.cuda.get_device_name(0) if torch.cuda.is_available() else 'None'}")

# If False, reinstall PyTorch with CUDA:
# Visit: https://pytorch.org/get-started/locally/
# Select your OS, Package, and CUDA version
```

**Example installation commands:**
```bash
# For CUDA 11.8:
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118

# For CUDA 12.1:
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121

# For CPU only:
pip install torch torchvision torchaudio
```

### Problem: CUDA out of memory

**Solutions:**
```python
# 1. Reduce batch size
batch_size = 8  # Instead of 32

# 2. Use gradient accumulation
# Simulate larger batch size
accumulation_steps = 4

# 3. Clear CUDA cache
import torch
torch.cuda.empty_cache()

# 4. Use mixed precision training
from torch.cuda.amp import autocast, GradScaler

# 5. Use gradient checkpointing
model.gradient_checkpointing_enable()
```

### Problem: Multiple CUDA versions

**Solution:**
```bash
# Check installed CUDA version
nvcc --version

# Check PyTorch CUDA version
python -c "import torch; print(torch.version.cuda)"

# Ensure they match
# Reinstall PyTorch if needed (see above)
```

---

## Memory Issues

### Problem: Jupyter notebook crashes with large datasets

**Solutions:**
```python
# 1. Use chunking for large files
import pandas as pd

# Instead of:
# df = pd.read_csv('large_file.csv')

# Use:
chunks = pd.read_csv('large_file.csv', chunksize=10000)
for chunk in chunks:
    process(chunk)

# 2. Use efficient dtypes
df = pd.read_csv('file.csv', dtype={'column': 'int32'})

# 3. Free memory
del large_object
import gc
gc.collect()
```

### Problem: RAM usage grows over time

**Solution:**
```python
# Monitor memory usage
import psutil
import os

def get_memory_usage():
    process = psutil.Process(os.getpid())
    return process.memory_info().rss / 1024 / 1024  # MB

print(f"Memory usage: {get_memory_usage():.2f} MB")

# Clear variables regularly
%reset -f  # In Jupyter

# Use context managers
with open('file.txt') as f:
    data = f.read()
    # process data
# file automatically closed
```

---

## Platform-Specific Issues

### macOS

#### Problem: SSL certificate errors

**Solution:**
```bash
# Install certificates
/Applications/Python\ 3.x/Install\ Certificates.command

# Or manually:
pip install --upgrade certifi
```

#### Problem: M1/M2 compatibility issues

**Solution:**
```bash
# Use Conda for better M1/M2 support
conda create -n aiml-learning python=3.11
conda activate aiml-learning

# Install packages via conda when possible
conda install numpy pandas scikit-learn
conda install pytorch torchvision -c pytorch
```

### Windows

#### Problem: Long path names

**Solution:**
```bash
# Enable long path support (Windows 10+)
# Run as Administrator in PowerShell:
New-ItemProperty -Path "HKLM:\SYSTEM\CurrentControlSet\Control\FileSystem" -Name "LongPathsEnabled" -Value 1 -PropertyType DWORD -Force

# Or clone to shorter path:
git clone https://github.com/PavanMudigondaTR/zero-to-ai.git C:\ai
```

#### Problem: Visual C++ redistributable missing

**Solution:**
- Download from: https://aka.ms/vs/17/release/vc_redist.x64.exe
- Install and restart computer

### Linux

#### Problem: `python3-dev` missing

**Solution:**
```bash
# Ubuntu/Debian:
sudo apt-get update
sudo apt-get install python3-dev python3-pip

# Fedora/RHEL:
sudo dnf install python3-devel

# Arch:
sudo pacman -S python python-pip
```

---

## Common Error Messages

### `ImportError: DLL load failed`

**Windows Solution:**
```bash
# Install/reinstall Visual C++ Redistributable
# Download from Microsoft
# Reinstall numpy
pip uninstall numpy
pip install numpy
```

### `RuntimeError: CUDA error: out of memory`

**Solution:**
```python
# Reduce batch size
batch_size = batch_size // 2

# Clear CUDA cache
torch.cuda.empty_cache()

# Or use CPU
device = 'cpu'
```

### `SyntaxError: invalid syntax`

**Solution:**
```bash
# Check Python version
python --version

# Ensure using Python 3.9+
# Check for Python 2 vs 3 issues
which python
which python3
```

---

## Getting More Help

If your issue isn't listed here:

1. **Search existing issues**: [GitHub Issues](https://github.com/PavanMudigondaTR/zero-to-ai/issues)
2. **Check discussions**: [GitHub Discussions](https://github.com/PavanMudigondaTR/zero-to-ai/discussions)
3. **Create new issue**: [New Issue](https://github.com/PavanMudigondaTR/zero-to-ai/issues/new)
4. **Community support**: Join our Discord (Coming Soon!)

### When Asking for Help

Include:
- Operating system and version
- Python version (`python --version`)
- Error message (full traceback)
- Steps to reproduce
- What you've already tried

---

## Quick Diagnosis Script

Run this to check your environment:

```python
#!/usr/bin/env python3
"""Quick environment diagnostic script"""

import sys
import platform

print("=" * 50)
print("ENVIRONMENT DIAGNOSTICS")
print("=" * 50)

print(f"\nPython Version: {sys.version}")
print(f"Platform: {platform.platform()}")
print(f"Python Executable: {sys.executable}")

print("\n" + "=" * 50)
print("CHECKING PACKAGES")
print("=" * 50)

packages = [
    'numpy', 'pandas', 'matplotlib', 'scikit-learn',
    'torch', 'transformers', 'jupyter'
]

for package in packages:
    try:
        mod = __import__(package)
        version = getattr(mod, '__version__', 'Unknown')
        print(f"✅ {package}: {version}")
    except ImportError:
        print(f"❌ {package}: NOT INSTALLED")

# Check CUDA
try:
    import torch
    print(f"\n✅ CUDA Available: {torch.cuda.is_available()}")
    if torch.cuda.is_available():
        print(f"   GPU: {torch.cuda.get_device_name(0)}")
except:
    print("\n❌ PyTorch/CUDA check failed")

print("\n" + "=" * 50)
```

Save as `check_env.py` and run: `python check_env.py`

---

**Still stuck?** Don't hesitate to [ask for help](https://github.com/PavanMudigondaTR/zero-to-ai/discussions)!
