#!/usr/bin/env python3
"""Find all AI coding tool references across the course."""
import json, glob, re

# Tools to search for (tool_name, url_pattern or name_pattern)
TOOLS = [
    ("aider", re.compile(r'\baider\b', re.I)),
    ("continue.dev", re.compile(r'continue\.dev|continuedev', re.I)),
    ("codeium", re.compile(r'\bcodeium\b', re.I)),
    ("tabnine", re.compile(r'\btabnine\b', re.I)),
    ("cody (sourcegraph)", re.compile(r'\bcody\b.*sourcegraph|sourcegraph.*\bcody\b|\bsourcegraph/cody\b', re.I)),
    ("supermaven", re.compile(r'\bsupermaven\b', re.I)),
    ("devin", re.compile(r'\bdevin\b.*cognition|\bcognition.*devin\b|cognition\.ai', re.I)),
    ("sweep", re.compile(r'\bsweepai\b|\bsweep\.dev\b', re.I)),
    ("opendevin/openhands", re.compile(r'opendevin|openhands', re.I)),
    ("swe-agent", re.compile(r'swe-agent|sweagent', re.I)),
    ("mentat", re.compile(r'\bmentat\b', re.I)),
    ("plandex", re.compile(r'\bplandex\b', re.I)),
    ("devika", re.compile(r'\bdevika\b', re.I)),
    ("windsurf", re.compile(r'\bwindsurf\b', re.I)),
    ("replit agent", re.compile(r'replit.*agent|replit.*ai', re.I)),
    ("bolt.new", re.compile(r'\bbolt\.new\b|\bbolt\.diy\b', re.I)),
    ("lovable", re.compile(r'\blovable\.dev\b|\blovable\b.*ai', re.I)),
    ("v0", re.compile(r'\bv0\.dev\b', re.I)),
    ("stackblitz", re.compile(r'\bstackblitz\b', re.I)),
    ("github copilot workspace", re.compile(r'copilot.*workspace|workspace.*copilot', re.I)),
    ("amazon q", re.compile(r'amazon\s+q\b|amazon.*codewhisperer', re.I)),
    ("jetbrains ai", re.compile(r'jetbrains.*ai\b|jb.*ai\b', re.I)),
    ("llm (simonw)", re.compile(r'\bllm\b.*simonw|simonw.*\bllm\b|llm\.datasette', re.I)),
    ("opencode", re.compile(r'\bopencode\b', re.I)),
    ("mini-swe-agent", re.compile(r'mini.swe', re.I)),
]

results = {}  # tool -> list of (path, cell_idx, snippet)

for nb_path in sorted(glob.glob('jupyter-notebooks/**/*.ipynb', recursive=True)):
    with open(nb_path) as f:
        try: nb = json.load(f)
        except: continue
    for ci, cell in enumerate(nb.get('cells', [])):
        src = ''.join(cell['source']) if isinstance(cell['source'], list) else cell['source']
        for name, pattern in TOOLS:
            if pattern.search(src):
                line = next((l for l in src.splitlines() if pattern.search(l)), '')
                if name not in results:
                    results[name] = []
                results[name].append((nb_path.replace('jupyter-notebooks/', ''), ci, line.strip()[:100]))

print(f"Tools found: {len(results)}\n")
for tool, hits in sorted(results.items()):
    print(f"== {tool} ({len(hits)} hit(s)) ==")
    seen = set()
    for path, ci, line in hits:
        key = path
        if key not in seen:
            seen.add(key)
            print(f"  {path}  cell {ci}")
    print()
