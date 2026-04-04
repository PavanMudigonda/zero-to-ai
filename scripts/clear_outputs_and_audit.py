#!/usr/bin/env python3
"""
Clear all cell outputs from Jupyter notebooks and audit for missing explanations.

This script:
1. Clears all cell outputs from every .ipynb file in the workspace
2. Identifies code cells that lack a preceding markdown explanation cell
"""

import json
import os
import sys
from pathlib import Path


def clear_outputs(notebook_path: str) -> tuple[bool, int]:
    """Clear all cell outputs from a notebook. Returns (changed, cells_cleared)."""
    with open(notebook_path, "r", encoding="utf-8") as f:
        nb = json.load(f)

    cells_cleared = 0
    changed = False

    for cell in nb.get("cells", []):
        if cell.get("cell_type") == "code":
            if cell.get("outputs") and len(cell["outputs"]) > 0:
                cell["outputs"] = []
                cells_cleared += 1
                changed = True
            if cell.get("execution_count") is not None:
                cell["execution_count"] = None
                changed = True

    if changed:
        with open(notebook_path, "w", encoding="utf-8") as f:
            json.dump(nb, f, indent=1, ensure_ascii=False)
            f.write("\n")

    return changed, cells_cleared


def audit_explanations(notebook_path: str) -> list[dict]:
    """Find code cells that lack a preceding markdown explanation."""
    with open(notebook_path, "r", encoding="utf-8") as f:
        nb = json.load(f)

    cells = nb.get("cells", [])
    issues = []

    for i, cell in enumerate(cells):
        if cell.get("cell_type") != "code":
            continue

        source = "".join(cell.get("source", []))
        # Skip empty code cells or cells with only comments/imports
        if not source.strip():
            continue

        # Check if preceding cell is a markdown cell with meaningful content
        has_explanation = False
        if i > 0:
            prev = cells[i - 1]
            if prev.get("cell_type") == "markdown":
                md_source = "".join(prev.get("source", []))
                # Check if markdown has enough content (more than just a heading)
                md_lines = [l.strip() for l in md_source.split("\n") if l.strip()]
                # Consider it explained if there's at least a heading + some text
                # or at least 2 non-empty lines
                if len(md_lines) >= 2 or (len(md_lines) == 1 and len(md_lines[0]) > 50):
                    has_explanation = True

        if not has_explanation:
            # Get first 80 chars of code for context
            code_preview = source.strip()[:80].replace("\n", " ")
            issues.append({
                "cell_index": i,
                "code_preview": code_preview,
            })

    return issues


def main():
    workspace = Path("/Users/pavanmudigonda/code/zero-to-ai")
    notebooks = sorted(workspace.rglob("*.ipynb"))

    # Exclude checkpoints and build artifacts
    notebooks = [
        nb for nb in notebooks
        if ".ipynb_checkpoints" not in str(nb)
        and "site/" not in str(nb)
        and "node_modules/" not in str(nb)
        and ".venv/" not in str(nb)
    ]

    print(f"Found {len(notebooks)} notebooks\n")

    # Phase 1: Clear outputs
    print("=" * 60)
    print("PHASE 1: Clearing cell outputs")
    print("=" * 60)
    total_cleared = 0
    notebooks_modified = 0
    for nb_path in notebooks:
        try:
            changed, cleared = clear_outputs(str(nb_path))
            if changed:
                notebooks_modified += 1
                total_cleared += cleared
                rel = nb_path.relative_to(workspace)
                print(f"  Cleared {cleared} outputs: {rel}")
        except (json.JSONDecodeError, KeyError) as e:
            print(f"  ERROR: {nb_path.relative_to(workspace)}: {e}")

    print(f"\nSummary: Cleared outputs in {notebooks_modified} notebooks ({total_cleared} cells total)")

    # Phase 2: Audit explanations
    print("\n" + "=" * 60)
    print("PHASE 2: Auditing for missing explanations")
    print("=" * 60)
    notebooks_needing_work = {}
    total_issues = 0
    for nb_path in notebooks:
        try:
            issues = audit_explanations(str(nb_path))
            if issues:
                rel = str(nb_path.relative_to(workspace))
                notebooks_needing_work[rel] = issues
                total_issues += len(issues)
        except (json.JSONDecodeError, KeyError):
            pass

    print(f"\nFound {total_issues} code cells without adequate explanations across {len(notebooks_needing_work)} notebooks\n")

    # Print summary sorted by number of issues
    for nb_rel, issues in sorted(notebooks_needing_work.items(), key=lambda x: -len(x[1])):
        print(f"  [{len(issues)} cells] {nb_rel}")

    # Write detailed report
    report_path = workspace / "scripts" / "audit_report.json"
    with open(report_path, "w") as f:
        json.dump(notebooks_needing_work, f, indent=2)
    print(f"\nDetailed report saved to: scripts/audit_report.json")


if __name__ == "__main__":
    main()
