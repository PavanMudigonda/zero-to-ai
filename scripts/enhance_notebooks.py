#!/usr/bin/env python3
"""
Enhance Jupyter notebooks: clear outputs and add detailed markdown explanations.

Usage:
    # Process a single notebook
    python scripts/enhance_notebooks.py path/to/notebook.ipynb

    # Process a directory
    python scripts/enhance_notebooks.py 03-maths/

    # Clear outputs only (no AI explanations)
    python scripts/enhance_notebooks.py --clear-only path/to/dir/

    # Dry run (show what would be changed)
    python scripts/enhance_notebooks.py --dry-run path/to/dir/
"""

import json
import os
import sys
import time
import glob
import argparse
import logging
from pathlib import Path
from typing import Optional

try:
    import anthropic
except ImportError:
    anthropic = None

try:
    from openai import OpenAI
except ImportError:
    OpenAI = None

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
    datefmt="%H:%M:%S",
)
log = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------
MODEL = os.environ.get("ANTHROPIC_MODEL", "anthropic/claude-haiku-4-5-20251001")
MAX_RETRIES = 3
RETRY_DELAY = 5  # seconds
MIN_MARKDOWN_LENGTH = 120  # chars — below this, we consider it "terse" and worth enhancing

SYSTEM_PROMPT = """You are enhancing Jupyter notebooks for a comprehensive AI/ML learning curriculum called "Zero to AI".

Your task: Given a code cell and its surrounding context, write a detailed markdown explanation that should PRECEDE the code cell.

Requirements for each explanation:
1. **What it does**: Clear description of what the code accomplishes
2. **Why it matters**: Why this concept/technique is important in ML/AI
3. **How it works**: Mathematical intuition or algorithmic explanation where applicable
4. **Practical connection**: How this connects to real-world ML applications

Format rules:
- Use a ### heading if it's a new concept, otherwise use bold text for the topic
- Include LaTeX math notation where helpful (using $...$ for inline, $$...$$ for block)
- Keep it 2-5 sentences for simple operations, 1-2 paragraphs for complex concepts
- Don't repeat the code — explain the thinking behind it
- Use analogies when they help build intuition
- Reference the specific functions/methods being used (e.g., "np.dot computes...")
- If there's an existing markdown cell that's too brief, REPLACE it entirely with a better version

Do NOT:
- Add code fences or code blocks
- Include cell markers or metadata
- Start with "This cell..." — be more natural
- Add emoji unless the notebook already uses them
- Include "## Explanation" or similar meta-headers

Return ONLY the markdown text. Nothing else."""


def get_client():
    """Create API client using available env vars. Supports both Anthropic and OpenAI-compatible endpoints."""
    api_key = os.environ.get("ANTHROPIC_AUTH_TOKEN") or os.environ.get(
        "ANTHROPIC_API_KEY"
    )
    base_url = os.environ.get("ANTHROPIC_BASE_URL") or os.environ.get(
        "OPENAI_BASE_URL"
    )
    if not api_key:
        raise RuntimeError("No ANTHROPIC_AUTH_TOKEN or ANTHROPIC_API_KEY found")

    # Try OpenAI-compatible client first (works with LiteLLM proxies)
    if OpenAI is not None and base_url:
        log.info(f"Using OpenAI-compatible client with base_url={base_url}")
        return ("openai", OpenAI(api_key=api_key, base_url=base_url))

    # Fall back to Anthropic native client
    if anthropic is not None:
        kwargs = {"api_key": api_key}
        if base_url:
            kwargs["base_url"] = base_url
        return ("anthropic", anthropic.Anthropic(**kwargs))

    raise RuntimeError("Neither openai nor anthropic Python package is installed")


def clear_outputs(nb: dict) -> int:
    """Clear all cell outputs and execution counts. Returns count of cleared cells."""
    cleared = 0
    for cell in nb.get("cells", []):
        if cell.get("cell_type") == "code":
            if cell.get("outputs") or cell.get("execution_count") is not None:
                cell["outputs"] = []
                cell["execution_count"] = None
                cleared += 1
    return cleared


def get_cell_source(cell: dict) -> str:
    """Get source text from a cell."""
    src = cell.get("source", "")
    if isinstance(src, list):
        return "".join(src)
    return src


def is_terse_markdown(cell: dict) -> bool:
    """Check if a markdown cell is too brief to be a good explanation."""
    src = get_cell_source(cell).strip()
    # Remove heading markers for length check
    text = src.lstrip("#").strip()
    # It's terse if it's very short OR just a heading with no body
    if len(text) < MIN_MARKDOWN_LENGTH:
        return True
    # Check if it's ONLY headings (no explanatory text)
    lines = [l.strip() for l in src.split("\n") if l.strip()]
    if all(l.startswith("#") or l.startswith("---") for l in lines):
        return True
    return False


def build_notebook_context(nb: dict) -> str:
    """Build a context string from the entire notebook."""
    parts = []
    for i, cell in enumerate(nb.get("cells", [])):
        ctype = cell.get("cell_type", "unknown")
        src = get_cell_source(cell)
        if src.strip():
            parts.append(f"[Cell {i} ({ctype})]:\n{src}")
    return "\n\n".join(parts)


def needs_explanation(cells: list, idx: int) -> tuple[bool, Optional[int]]:
    """
    Check if code cell at idx needs a new/better explanation.
    Returns (needs_new, enhance_idx):
      - (True, None) = needs a brand new markdown cell inserted before
      - (True, int)  = existing markdown at enhance_idx needs improvement
      - (False, None) = already has adequate explanation
    """
    if idx == 0:
        return True, None

    prev = cells[idx - 1]
    if prev.get("cell_type") != "markdown":
        return True, None

    if is_terse_markdown(prev):
        return True, idx - 1

    return False, None


def generate_explanation(
    client_tuple,
    code_source: str,
    notebook_context: str,
    notebook_title: str,
    existing_markdown: str = "",
) -> str:
    """Generate a detailed markdown explanation for a code cell."""
    client_type, client = client_tuple

    user_msg = f"Notebook: {notebook_title}\n\n"
    user_msg += f"Full notebook context:\n{notebook_context[:8000]}\n\n"
    user_msg += f"Code cell to explain:\n```python\n{code_source}\n```\n\n"
    if existing_markdown:
        user_msg += f"Existing (insufficient) explanation to improve upon:\n{existing_markdown}\n\n"
    user_msg += "Write a detailed markdown explanation for this code cell."

    for attempt in range(MAX_RETRIES):
        try:
            if client_type == "openai":
                resp = client.chat.completions.create(
                    model=MODEL,
                    max_tokens=1024,
                    messages=[
                        {"role": "system", "content": SYSTEM_PROMPT},
                        {"role": "user", "content": user_msg},
                    ],
                )
                return resp.choices[0].message.content.strip()
            else:
                resp = client.messages.create(
                    model=MODEL,
                    max_tokens=1024,
                    system=SYSTEM_PROMPT,
                    messages=[{"role": "user", "content": user_msg}],
                )
                return resp.content[0].text.strip()
        except Exception as e:
            if attempt < MAX_RETRIES - 1:
                log.warning(f"API error (attempt {attempt+1}): {e}. Retrying...")
                time.sleep(RETRY_DELAY * (attempt + 1))
            else:
                log.error(f"Failed after {MAX_RETRIES} attempts: {e}")
                raise


def make_markdown_cell(source: str) -> dict:
    """Create a new markdown cell."""
    return {
        "cell_type": "markdown",
        "metadata": {},
        "source": source.split("\n")
        if "\n" in source
        else [source],
    }


def fix_source_format(cell: dict):
    """Ensure source is a list of strings (lines) with proper newlines."""
    src = cell.get("source", "")
    if isinstance(src, str):
        lines = src.split("\n")
        # Add newline to all lines except the last
        cell["source"] = [
            line + "\n" if i < len(lines) - 1 else line
            for i, line in enumerate(lines)
        ]


def enhance_notebook(
    nb_path: str,
    client: Optional[anthropic.Anthropic] = None,
    clear_only: bool = False,
    dry_run: bool = False,
) -> dict:
    """
    Enhance a single notebook: clear outputs and add explanations.
    Returns stats dict.
    """
    stats = {"path": nb_path, "cleared": 0, "added": 0, "enhanced": 0, "errors": 0}

    with open(nb_path, "r") as f:
        nb = json.load(f)

    # Pass 1: Clear outputs
    stats["cleared"] = clear_outputs(nb)

    if clear_only:
        if not dry_run:
            with open(nb_path, "w") as f:
                json.dump(nb, f, indent=1, ensure_ascii=False)
                f.write("\n")
        return stats

    # Pass 2: Add/enhance explanations
    if client is None:
        client = get_client()

    notebook_title = Path(nb_path).stem
    context = build_notebook_context(nb)
    cells = nb.get("cells", [])

    # Work backwards so insertions don't shift indices
    insertions = []  # (index, action, existing_idx)

    for i, cell in enumerate(cells):
        if cell.get("cell_type") != "code":
            continue
        code_src = get_cell_source(cell).strip()
        if not code_src:
            continue  # Skip empty cells
        # Skip cells that are ONLY comments (no actual code)
        code_lines = [l for l in code_src.split("\n") if l.strip() and not l.strip().startswith("#")]
        if not code_lines:
            continue

        needs_new, enhance_idx = needs_explanation(cells, i)
        if needs_new:
            insertions.append((i, "insert" if enhance_idx is None else "enhance", enhance_idx))

    if dry_run:
        stats["added"] = sum(1 for _, a, _ in insertions if a == "insert")
        stats["enhanced"] = sum(1 for _, a, _ in insertions if a == "enhance")
        return stats

    # Process in reverse order to preserve indices
    for code_idx, action, enhance_idx in reversed(insertions):
        code_src = get_cell_source(cells[code_idx])
        existing_md = ""
        if action == "enhance" and enhance_idx is not None:
            existing_md = get_cell_source(cells[enhance_idx])

        try:
            explanation = generate_explanation(
                client, code_src, context, notebook_title, existing_md
            )

            if action == "insert":
                new_cell = make_markdown_cell(explanation)
                fix_source_format(new_cell)
                cells.insert(code_idx, new_cell)
                stats["added"] += 1
            else:
                cells[enhance_idx]["source"] = explanation.split("\n")
                fix_source_format(cells[enhance_idx])
                stats["enhanced"] += 1

            # Small delay to respect rate limits
            time.sleep(0.5)

        except Exception as e:
            log.error(f"Error processing cell {code_idx} in {nb_path}: {e}")
            stats["errors"] += 1

    # Save
    with open(nb_path, "w") as f:
        json.dump(nb, f, indent=1, ensure_ascii=False)
        f.write("\n")

    return stats


def find_notebooks(path: str) -> list[str]:
    """Find all .ipynb files in path, excluding checkpoints and venv."""
    p = Path(path)
    if p.is_file() and p.suffix == ".ipynb":
        return [str(p)]

    results = []
    for nb in sorted(p.rglob("*.ipynb")):
        nb_str = str(nb)
        if any(skip in nb_str for skip in [
            ".ipynb_checkpoints", ".venv", "node_modules",
            "/curriculum/", "/docs/generated/", "/site/"
        ]):
            continue
        results.append(nb_str)
    return results


def main():
    parser = argparse.ArgumentParser(description="Enhance Jupyter notebooks")
    parser.add_argument("path", help="Notebook file or directory to process")
    parser.add_argument("--clear-only", action="store_true",
                        help="Only clear outputs, don't add explanations")
    parser.add_argument("--dry-run", action="store_true",
                        help="Show what would be changed without modifying files")
    args = parser.parse_args()

    notebooks = find_notebooks(args.path)
    if not notebooks:
        log.error(f"No notebooks found at {args.path}")
        sys.exit(1)

    log.info(f"Found {len(notebooks)} notebooks to process")

    client = None if args.clear_only else get_client()

    total_stats = {"cleared": 0, "added": 0, "enhanced": 0, "errors": 0}

    for i, nb_path in enumerate(notebooks, 1):
        rel = os.path.relpath(nb_path)
        log.info(f"[{i}/{len(notebooks)}] Processing: {rel}")

        try:
            stats = enhance_notebook(
                nb_path, client,
                clear_only=args.clear_only,
                dry_run=args.dry_run,
            )
            for k in total_stats:
                total_stats[k] += stats.get(k, 0)

            log.info(
                f"  -> cleared={stats['cleared']} added={stats['added']} "
                f"enhanced={stats['enhanced']} errors={stats['errors']}"
            )
        except Exception as e:
            log.error(f"  -> FAILED: {e}")
            total_stats["errors"] += 1

    log.info("=" * 60)
    log.info(f"DONE. Processed {len(notebooks)} notebooks.")
    log.info(f"  Outputs cleared: {total_stats['cleared']}")
    log.info(f"  Explanations added: {total_stats['added']}")
    log.info(f"  Explanations enhanced: {total_stats['enhanced']}")
    log.info(f"  Errors: {total_stats['errors']}")


if __name__ == "__main__":
    main()
