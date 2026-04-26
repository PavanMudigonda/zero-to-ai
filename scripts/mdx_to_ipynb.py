import sys
import json
from pathlib import Path

def convert(mdx_path, ipynb_path):
    mdx = Path(mdx_path)
    if not mdx.exists():
        print(f"Does not exist: {mdx}")
        return

    content = mdx.read_text()
    
    # Strip any next.js frontmatter
    if content.startswith("---"):
        parts = content.split("---", 2)
        if len(parts) >= 3:
            content = parts[2].strip()

    notebook = {
        "cells": [
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": [line + "\n" for line in content.split("\n")]
            }
        ],
        "metadata": {
            "kernelspec": {
                "display_name": "Python 3",
                "language": "python",
                "name": "python3"
            },
            "language_info": {
                "file_extension": ".py",
                "mimetype": "text/x-python",
                "name": "python",
                "version": "3.10.x"
            }
        },
        "nbformat": 4,
        "nbformat_minor": 2
    }
    
    out = Path(ipynb_path)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(notebook, indent=1))
    print(f"Created: {out}")

# 1. 00-course-setup index
convert(
    "/Users/pavanmudigonda/code/zero-to-ai/next-docs/src/app/00-course-setup/page.mdx",
    "/Users/pavanmudigonda/code/zero-to-ai/jupyter-notebooks/00-course-setup.ipynb"
)

# 2. 01_model_landscape
convert(
    "/Users/pavanmudigonda/code/zero-to-ai/next-docs/src/app/00-course-setup/01_model_landscape/page.mdx",
    "/Users/pavanmudigonda/code/zero-to-ai/jupyter-notebooks/00-course-setup/01_model_landscape.ipynb"
)

# 3. 02_troubleshooting
convert(
    "/Users/pavanmudigonda/code/zero-to-ai/next-docs/src/app/00-course-setup/02_troubleshooting/page.mdx",
    "/Users/pavanmudigonda/code/zero-to-ai/jupyter-notebooks/00-course-setup/02_troubleshooting.ipynb"
)

# 4. 01-python index
convert(
    "/Users/pavanmudigonda/code/zero-to-ai/next-docs/src/app/01-python/page.mdx",
    "/Users/pavanmudigonda/code/zero-to-ai/jupyter-notebooks/01-python.ipynb"
)

