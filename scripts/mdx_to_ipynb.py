import sys
import json
import argparse
from pathlib import Path

def mdx_to_ipynb(mdx_path, ipynb_path):
    mdx = Path(mdx_path)
    if not mdx.exists():
        print(f"Error: {mdx} does not exist.")
        return

    content = mdx.read_text(encoding="utf-8")
    
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
    out.write_text(json.dumps(notebook, indent=1), encoding="utf-8")
    print(f"Successfully converted MDX to IPYNB: {out}")

def ipynb_to_mdx(ipynb_path, mdx_path):
    ipynb = Path(ipynb_path)
    if not ipynb.exists():
        print(f"Error: {ipynb} does not exist.")
        return

    notebook = json.loads(ipynb.read_text(encoding="utf-8"))
    
    mdx_content = []
    
    for cell in notebook.get("cells", []):
        source = "".join(cell.get("source", []))
        if not source.strip():
            continue
            
        if cell["cell_type"] == "markdown":
            mdx_content.append(source)
        elif cell["cell_type"] == "code":
            mdx_content.append(f"```python\n{source}\n```")
            
        mdx_content.append("\n\n")
        
    out = Path(mdx_path)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text("".join(mdx_content).strip() + "\n", encoding="utf-8")
    print(f"Successfully converted IPYNB to MDX: {out}")

def main():
    parser = argparse.ArgumentParser(description="Convert between MDX and IPYNB formats")
    parser.add_argument("input_file", help="Input file path (.mdx or .ipynb)")
    parser.add_argument("output_file", nargs='?', help="Output file path (optional, will auto-generate if omitted)")
    
    args = parser.parse_args()
    
    input_path = Path(args.input_file)
    
    if args.output_file:
        output_path = Path(args.output_file)
    else:
        if input_path.suffix.lower() == '.mdx':
            output_path = input_path.with_suffix('.ipynb')
        elif input_path.suffix.lower() == '.ipynb':
            output_path = input_path.with_suffix('.mdx')
        else:
            print("Error: Input file must be .mdx or .ipynb")
            sys.exit(1)
            
    if input_path.suffix.lower() == '.mdx' and output_path.suffix.lower() == '.ipynb':
        mdx_to_ipynb(input_path, output_path)
    elif input_path.suffix.lower() == '.ipynb' and output_path.suffix.lower() == '.mdx':
        ipynb_to_mdx(input_path, output_path)
    else:
        print("Error: Unsupported conversion direction. Must be .mdx -> .ipynb or .ipynb -> .mdx")
        sys.exit(1)

if __name__ == "__main__":
    main()
