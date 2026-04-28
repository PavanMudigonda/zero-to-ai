import sys
import json
import argparse
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent.resolve()
DOCS_APP_DIR = REPO_ROOT / "next-docs" / "src" / "app"
NOTEBOOKS_DIR = REPO_ROOT / "jupyter-notebooks"


def strip_frontmatter(content):
    if content.startswith("---"):
        parts = content.split("---", 2)
        if len(parts) >= 3:
            return parts[2].strip()
    return content.strip()


def is_dynamic_notebook_wrapper(content):
    return "import DynamicNotebook" in content and "<DynamicNotebook ipynb={nb}" in content


def build_cells_from_mdx(content):
    cells = []
    current_markdown = []
    in_fence = False
    fence_language = ""
    current_code = []

    def flush_markdown():
        if not current_markdown:
            return
        if not any(line.strip() for line in current_markdown):
            current_markdown.clear()
            return
        cells.append(
            {
                "cell_type": "markdown",
                "metadata": {"language": "markdown"},
                "source": current_markdown.copy(),
            }
        )
        current_markdown.clear()

    def flush_code():
        if not current_code:
            return
        cells.append(
            {
                "cell_type": "code",
                "metadata": {"language": fence_language or "text"},
                "source": current_code.copy(),
            }
        )
        current_code.clear()

    for raw_line in content.splitlines():
        line = raw_line + "\n"
        stripped = raw_line.strip()

        if stripped.startswith("```"):
            if in_fence:
                flush_code()
                in_fence = False
                fence_language = ""
            else:
                flush_markdown()
                in_fence = True
                fence_language = stripped[3:].strip()
            continue

        if in_fence:
            current_code.append(line)
        else:
            current_markdown.append(line)

    if in_fence:
        current_markdown.extend([f"```{fence_language}\n", *current_code])
        current_code.clear()

    flush_markdown()
    return cells or [{"cell_type": "markdown", "metadata": {"language": "markdown"}, "source": [content + "\n"]}]


def notebook_payload_from_mdx(content):
    return {
        "cells": build_cells_from_mdx(content),
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


def mdx_to_ipynb(mdx_path, ipynb_path):
    mdx = Path(mdx_path)
    if not mdx.exists():
        print(f"Error: {mdx} does not exist.")
        return

    content = strip_frontmatter(mdx.read_text(encoding="utf-8"))
    notebook = notebook_payload_from_mdx(content)
    
    out = Path(ipynb_path)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(notebook, indent=1), encoding="utf-8")
    print(f"Successfully converted MDX to IPYNB: {out}")


def iter_non_wrapper_mdx_paths(base_dir):
    for mdx_path in sorted(base_dir.rglob("page.mdx")):
        content = mdx_path.read_text(encoding="utf-8")
        if is_dynamic_notebook_wrapper(content):
            continue
        yield mdx_path


def sync_section_from_docs(section_name):
    docs_section_dir = DOCS_APP_DIR / section_name
    notebooks_section_dir = NOTEBOOKS_DIR / section_name

    if not docs_section_dir.exists():
        print(f"Error: {docs_section_dir} does not exist.")
        return 1

    converted = 0

    for mdx_path in iter_non_wrapper_mdx_paths(docs_section_dir):
        rel_dir = mdx_path.parent.relative_to(DOCS_APP_DIR)
        notebook_name = f"{mdx_path.parent.name}.ipynb"
        ipynb_path = NOTEBOOKS_DIR / rel_dir / notebook_name
        mdx_to_ipynb(mdx_path, ipynb_path)
        converted += 1

    print(f"Converted {converted} MDX pages from {docs_section_dir} into notebooks under {notebooks_section_dir}.")
    return 0


def sync_all_docs_to_notebooks():
    converted = 0

    for mdx_path in iter_non_wrapper_mdx_paths(DOCS_APP_DIR):
        rel_dir = mdx_path.parent.relative_to(DOCS_APP_DIR)
        notebook_name = f"{mdx_path.parent.name}.ipynb"
        ipynb_path = NOTEBOOKS_DIR / rel_dir / notebook_name
        mdx_to_ipynb(mdx_path, ipynb_path)
        converted += 1

    print(f"Converted {converted} MDX pages from {DOCS_APP_DIR} into notebooks under {NOTEBOOKS_DIR}.")
    return 0

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
    parser.add_argument("--sync-all", dest="sync_all", action="store_true", help="Sync all non-wrapper page.mdx files from next-docs/src/app into jupyter-notebooks")
    parser.add_argument("--sync-section", dest="sync_section", help="Sync all non-wrapper page.mdx files from next-docs/src/app/<section> into jupyter-notebooks/<section>")
    parser.add_argument("input_file", nargs='?', help="Input file path (.mdx or .ipynb)")
    parser.add_argument("output_file", nargs='?', help="Output file path (optional, will auto-generate if omitted)")
    
    args = parser.parse_args()

    if args.sync_all:
        sys.exit(sync_all_docs_to_notebooks())

    if args.sync_section:
        sys.exit(sync_section_from_docs(args.sync_section))

    if not args.input_file:
        parser.error("the following arguments are required: input_file")
    
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
