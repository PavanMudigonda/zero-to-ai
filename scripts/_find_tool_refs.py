#!/usr/bin/env python3
import json, glob, re

# Find every notebook that mentions any of the 5 tools (beyond cell 0 titles)
TOOLS = re.compile(
    r'GitHub Copilot|VS Code Copilot|Claude Code|code\.claude\.com|'
    r'Cursor IDE|cursor\.com/docs|OpenAI Codex|developers\.openai\.com/codex|'
    r'Google Antigravity|antigravity\.google',
    re.IGNORECASE
)

results = {}
for nb_path in sorted(glob.glob('jupyter-notebooks/**/*.ipynb', recursive=True)):
    with open(nb_path) as f:
        try:
            nb = json.load(f)
        except Exception:
            continue
    for ci, cell in enumerate(nb.get('cells', [])):
        src = ''.join(cell['source']) if isinstance(cell['source'], list) else cell['source']
        if TOOLS.search(src):
            nb_short = nb_path.replace('jupyter-notebooks/', '')
            if nb_short not in results:
                results[nb_short] = []
            results[nb_short].append(ci)

print(f"Notebooks referencing the 5 tools: {len(results)}")
for nb_path, cells in results.items():
    print(f"  {nb_path}  (cells: {cells})")
