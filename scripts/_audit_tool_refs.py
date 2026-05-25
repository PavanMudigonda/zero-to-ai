#!/usr/bin/env python3
import json, glob, re

CHECKS = [
    ("Cursor: stale Grok", re.compile(r'Grok 4\.20')),
    ("Cursor: bare Composer 2", re.compile(r'Composer 2[^.\d]')),
    ("Antigravity URL", re.compile(r'antigravity\.google/docs/get-started(?!ing)')),
    ("Copilot Agents agents-overview", re.compile(r'copilot/agents-overview')),
    ("Claude Code old URL", re.compile(r'code\.claude\.ai/')),
    ("Codex old quickstart", re.compile(r'openai\.com/blog/openai-codex')),
]

hits = []
for nb_path in sorted(glob.glob('jupyter-notebooks/**/*.ipynb', recursive=True)):
    with open(nb_path) as f:
        try:
            nb = json.load(f)
        except Exception:
            continue
    for ci, cell in enumerate(nb.get('cells', [])):
        src = ''.join(cell['source']) if isinstance(cell['source'], list) else cell['source']
        for name, pattern in CHECKS:
            m = pattern.search(src)
            if m:
                lines = src.splitlines()
                hit_line = next((l for l in lines if pattern.search(l)), '')
                hits.append((nb_path, ci, name, hit_line.strip()[:120]))

print("Total hits:", len(hits))
for nb_path, ci, name, line in hits:
    print(f"  [{name}]  {nb_path}  cell {ci}")
    print(f"    {line}")
