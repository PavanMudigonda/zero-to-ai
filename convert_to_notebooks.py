#!/usr/bin/env python3
"""
Convert Python scripts to Jupyter notebooks for step-by-step execution.
"""

import json
import re
import os
from pathlib import Path
from typing import List, Tuple

def parse_python_file(filepath: str) -> List[Tuple[str, str]]:
    """
    Parse a Python file into cells (markdown and code).
    Returns list of (cell_type, content) tuples.
    """
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    cells = []
    
    # Extract module docstring as first markdown cell
    module_doc_match = re.match(r'^"""(.*?)"""', content, re.DOTALL)
    if module_doc_match:
        doc = module_doc_match.group(1).strip()
        title = os.path.basename(filepath).replace('.py', '').replace('_', ' ').title()
        cells.append(('markdown', f"# {title}\n\n{doc}"))
        # Remove the docstring from content
        content = content[module_doc_match.end():].lstrip()
    
    # Split by function definitions
    functions = re.split(r'\n(?=def |class )', content)
    
    for i, func in enumerate(functions):
        func = func.strip()
        if not func:
            continue
        
        # Check if it's imports
        if i == 0 and not func.startswith('def') and not func.startswith('class'):
            # This is the imports section
            cells.append(('markdown', '## Setup\n\nImport required libraries:'))
            cells.append(('code', func))
        elif func.startswith('def '):
            # Extract function name and docstring
            func_match = re.match(r'def\s+(\w+)\([^)]*\):\s*"""(.*?)"""', func, re.DOTALL)
            if func_match:
                func_name = func_match.group(1)
                func_doc = func_match.group(2).strip()
                # Convert function name to title
                title = func_name.replace('_', ' ').replace('example ', 'Example ').title()
                cells.append(('markdown', f"## {title}\n\n{func_doc}"))
                cells.append(('code', func))
            else:
                # No docstring, just add as code
                cells.append(('code', func))
        elif func.startswith('if __name__'):
            # This is the main execution block
            cells.append(('markdown', '## Run All Examples\n\nExecute the main function to run all examples:'))
            cells.append(('code', func))
        else:
            cells.append(('code', func))
    
    return cells

def create_notebook(cells: List[Tuple[str, str]]) -> dict:
    """Create a Jupyter notebook structure from cells."""
    notebook = {
        "cells": [],
        "metadata": {
            "kernelspec": {
                "display_name": "Python 3",
                "language": "python",
                "name": "python3"
            },
            "language_info": {
                "codemirror_mode": {
                    "name": "ipython",
                    "version": 3
                },
                "file_extension": ".py",
                "mimetype": "text/x-python",
                "name": "python",
                "nbconvert_exporter": "python",
                "pygments_lexer": "ipython3",
                "version": "3.9.0"
            }
        },
        "nbformat": 4,
        "nbformat_minor": 5
    }
    
    for cell_type, content in cells:
        cell = {
            "cell_type": cell_type,
            "metadata": {},
            "source": content.split('\n')
        }
        
        if cell_type == "code":
            cell["execution_count"] = None
            cell["outputs"] = []
        
        notebook["cells"].append(cell)
    
    return notebook

def convert_file(input_path: str, output_path: str):
    """Convert a single Python file to Jupyter notebook."""
    print(f"Converting: {input_path}")
    print(f"  Output: {output_path}")
    
    try:
        cells = parse_python_file(input_path)
        notebook = create_notebook(cells)
        
        # Create output directory if needed
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        
        # Write notebook
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(notebook, f, indent=2)
        
        print(f"  ✅ Success! Created {len(cells)} cells")
        return True
    except Exception as e:
        print(f"  ❌ Error: {e}")
        return False

def main():
    """Convert all Python files to notebooks."""
    import sys
    base_dir = Path(sys.argv[1]) if len(sys.argv) > 1 else Path('.')
    
    # Find all Python files
    python_files = []
    for root, dirs, files in os.walk(base_dir):
        # Skip __pycache__ and hidden directories
        dirs[:] = [d for d in dirs if not d.startswith('.') and d != '__pycache__']
        for file in files:
            if file.endswith('.py') and not file.startswith('.') and file != 'convert_to_notebooks.py':
                python_files.append(Path(root) / file)
    
    print(f"Found {len(python_files)} Python files to convert\n")
    print("="*70)
    
    success_count = 0
    failed_count = 0
    
    for py_file in sorted(python_files):
        # Create corresponding notebook path
        nb_file = py_file.with_suffix('.ipynb')
        
        if convert_file(str(py_file), str(nb_file)):
            success_count += 1
        else:
            failed_count += 1
        print()
    
    print("="*70)
    print(f"\nConversion Summary:")
    print(f"  ✅ Successfully converted: {success_count}")
    print(f"  ❌ Failed: {failed_count}")
    print(f"  📊 Total: {len(python_files)}")
    
    if success_count > 0:
        print("\n🎉 Notebooks created! You can now run them step-by-step in Jupyter or VS Code.")
        print("\nTo use:")
        print("  1. Open any .ipynb file in VS Code")
        print("  2. Click 'Run All' or run cells individually")
        print("  3. Install kernels if prompted")

if __name__ == "__main__":
    main()
