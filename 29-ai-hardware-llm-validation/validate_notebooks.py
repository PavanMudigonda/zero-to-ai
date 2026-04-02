#!/usr/bin/env python3
"""Lightweight validator for notebook structure and Python code cells."""

from __future__ import annotations

import ast
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent


def validate_notebook(path: Path) -> list[str]:
    errors: list[str] = []

    try:
        notebook = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        return [f"{path.name}: invalid JSON ({exc})"]

    nbformat = notebook.get("nbformat")
    if not isinstance(nbformat, int) or nbformat < 4:
        errors.append(f"{path.name}: expected nbformat >= 4, found {nbformat!r}")

    cells = notebook.get("cells")
    if not isinstance(cells, list):
        return [f"{path.name}: missing or invalid 'cells' list"]

    for index, cell in enumerate(cells):
        if cell.get("cell_type") != "code":
            continue

        if "outputs" not in cell:
            errors.append(f"{path.name}: code cell {index} missing 'outputs'")
        if "execution_count" not in cell:
            errors.append(f"{path.name}: code cell {index} missing 'execution_count'")

        source = cell.get("source", [])
        if isinstance(source, list):
            source_text = "".join(source)
        elif isinstance(source, str):
            source_text = source
        else:
            errors.append(f"{path.name}: code cell {index} has invalid 'source' type")
            continue

        try:
            ast.parse(source_text)
        except SyntaxError as exc:
            errors.append(f"{path.name}: code cell {index} syntax error ({exc})")

    return errors


def main() -> int:
    notebook_paths = sorted(ROOT.glob("*.ipynb"))
    if not notebook_paths:
        print("No notebooks found.")
        return 1

    failures: list[str] = []
    for path in notebook_paths:
        failures.extend(validate_notebook(path))

    if failures:
        print("Notebook validation failed:")
        for failure in failures:
            print(f"  - {failure}")
        return 1

    print(f"Validated {len(notebook_paths)} notebooks successfully.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
