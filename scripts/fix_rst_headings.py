#!/usr/bin/env python3
"""Strip RST-style ==== heading decorations from scikit-learn notebook markdown cells.

Pattern detected:
  # Short Title
  
  ========...========
  Actual descriptive title
  ========...========
  
  Body text...

This converts the RST overline/underline title to a markdown ## heading:
  # Short Title
  
  ## Actual descriptive title
  
  Body text...

Also handles --- and ~~~ RST underlines.
"""

import json
import re
import sys
from pathlib import Path


def fix_rst_headings_in_cell(source_lines):
    """Fix RST-style headings in a list of notebook cell source lines."""
    result = []
    i = 0
    changed = False
    while i < len(source_lines):
        line = source_lines[i]
        stripped = line.rstrip("\n")
        
        # Detect RST overline pattern: ====...==== / Title / ====...====
        if re.match(r'^[=~\-]{4,}\s*$', stripped):
            # Look ahead: next line should be title, line after should be same decoration
            if (i + 2 < len(source_lines) and
                    not re.match(r'^[=~\-]{4,}\s*$', source_lines[i+1].rstrip("\n")) and
                    source_lines[i+1].strip()):
                title_line = source_lines[i+1]
                after_stripped = source_lines[i+2].rstrip("\n") if i+2 < len(source_lines) else ""
                
                if re.match(r'^[=~\-]{4,}\s*$', after_stripped):
                    # Full overline/underline pattern - replace with ## heading
                    title_text = title_line.strip().rstrip("\n")
                    result.append(f"## {title_text}\n")
                    i += 3  # Skip overline, title, underline
                    changed = True
                    continue
                else:
                    # Just underline pattern (decoration above title, no matching below)
                    # Keep as-is but this case is rare
                    pass
            
            # Check if it's an underline-only pattern: Title / ====...====
            if i > 0 and result:
                prev = result[-1].rstrip("\n")
                if prev.strip() and not re.match(r'^#+\s', prev) and not re.match(r'^[=~\-]{4,}\s*$', prev):
                    # Previous line was a title, this is just an underline
                    title_text = result[-1].strip().rstrip("\n")
                    result[-1] = f"## {title_text}\n"
                    i += 1  # Skip the underline
                    changed = True
                    continue
        
        result.append(line)
        i += 1
    
    return result, changed


def fix_notebook(filepath):
    """Fix RST headings in a single notebook file."""
    with open(filepath, "r", encoding="utf-8") as f:
        nb = json.load(f)
    
    modified = False
    for cell in nb["cells"]:
        if cell["cell_type"] == "markdown":
            source = cell["source"]
            # Handle both string and list-of-lines formats
            if isinstance(source, str):
                lines = [l + "\n" for l in source.split("\n")]
                # Remove trailing \n from last line
                if lines:
                    lines[-1] = lines[-1].rstrip("\n")
                new_lines, changed = fix_rst_headings_in_cell(lines)
                if changed:
                    cell["source"] = "".join(new_lines)
                    modified = True
            else:
                new_source, changed = fix_rst_headings_in_cell(source)
                if changed:
                    cell["source"] = new_source
                    modified = True
    
    if modified:
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(nb, f, indent=1, ensure_ascii=False)
            f.write("\n")
    
    return modified


def main():
    base = Path("02-data-science/5-scikit-learn")
    if not base.exists():
        print(f"Directory not found: {base}")
        sys.exit(1)
    
    notebooks = sorted(base.rglob("*.ipynb"))
    fixed = 0
    for nb_path in notebooks:
        if fix_notebook(nb_path):
            print(f"  Fixed: {nb_path}")
            fixed += 1
    
    print(f"\nDone. Fixed {fixed}/{len(notebooks)} notebooks.")


if __name__ == "__main__":
    main()
