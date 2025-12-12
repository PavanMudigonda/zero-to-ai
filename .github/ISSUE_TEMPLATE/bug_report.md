---
name: Bug Report
about: Report an error in a notebook, code, or documentation
title: '[BUG] '
labels: bug
assignees: ''
---

## 🐛 Bug Description

A clear and concise description of what the bug is.

## 📍 Location

**Phase**: [e.g., 5-neural-networks]
**Notebook**: [e.g., 04_attention_mechanism.ipynb]
**Cell Number**: [e.g., Cell 7]

## 🔄 Steps to Reproduce

Steps to reproduce the behavior:

1. Open notebook '...'
2. Run cell '...'
3. Execute code '...'
4. See error

## ❌ Error Message

```
Paste the complete error message here
```

## ✅ Expected Behavior

A clear and concise description of what you expected to happen.

## 📊 Actual Behavior

What actually happened instead.

## 🖥️ Environment

- **OS**: [e.g., macOS 14.0, Ubuntu 22.04, Windows 11]
- **Python Version**: [e.g., 3.11.5]
- **Jupyter**: [e.g., JupyterLab 4.0.0, VS Code with Jupyter extension]
- **Key Package Versions**: [e.g., torch==2.1.0, transformers==4.36.0]

You can get this info by running:
```python
import sys
import torch
import transformers

print(f"Python: {sys.version}")
print(f"PyTorch: {torch.__version__}")
print(f"Transformers: {transformers.__version__}")
```

## 🔍 Additional Context

Add any other context about the problem here:
- Screenshots (if applicable)
- Related issues or notebooks
- When the bug started appearing
- Workarounds you've tried

## ✅ Checklist

- [ ] I have checked existing issues to avoid duplicates
- [ ] I have tried running with the latest dependencies from requirements.txt
- [ ] I have activated the virtual environment (.venv)
- [ ] I have included the complete error message
- [ ] I have specified the exact notebook and cell where the error occurs

## 💡 Suggested Fix (Optional)

If you have ideas on how to fix this bug, please share them here.
