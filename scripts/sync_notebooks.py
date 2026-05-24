import os
import re
import shutil
from pathlib import Path

TITLE_OVERRIDES = {
    'ai': 'AI',
    'ml': 'ML',
    'llm': 'LLM',
    'llms': 'LLMs',
    'rag': 'RAG',
    'mlops': 'MLOps',
    'nlp': 'NLP',
    'api': 'API',
    'apis': 'APIs',
    'sdk': 'SDK',
    'mcp': 'MCP',
    'rl': 'RL',
    'lora': 'LoRA',
    'qlora': 'QLoRA',
    'vscode': 'VS Code',
    'openai': 'OpenAI',
    'ide': 'IDE',
    'ides': 'IDEs',
}

PHRASE_OVERRIDES = {
    'Debugging Troubleshooting': 'Debugging & Troubleshooting',
    'AI Safety Redteaming': 'AI Safety & Red Teaming',
    'AI Powered Dev Tools': 'AI-Powered Dev Tools',
    'AI Hardware LLM Validation': 'AI Hardware & LLM Validation',
    'Low Code AI Tools': 'Low-Code AI Tools',
    'Real Time Streaming': 'Real-Time Streaming',
    'Time Series Analysis': 'Time-Series Analysis',
}


def clean_title(name: str) -> str:
    words = name.replace('_', ' ').replace('-', ' ').split()
    cleaned_words = []

    for word in words:
        override = TITLE_OVERRIDES.get(word.lower())
        if override:
            cleaned_words.append(override)
            continue

        cleaned_words.append(word.capitalize())

    title = ' '.join(cleaned_words)
    number_prefix_match = re.match(r'^(\d+)\s+(.*)$', title)

    if not number_prefix_match:
        return PHRASE_OVERRIDES.get(title, title)

    number_prefix, remainder = number_prefix_match.groups()
    return f"{number_prefix} {PHRASE_OVERRIDES.get(remainder, remainder)}"


def is_generated_notebook_wrapper(page_path: Path, notebook_file_name: str) -> bool:
    if not page_path.exists():
        return True

    contents = page_path.read_text()
    return (
        "import DynamicNotebook from '@/components/DynamicNotebook';" in contents
        and f"import nb from './{notebook_file_name}';" in contents
        and '<DynamicNotebook ipynb={nb} />' in contents
    )


def get_target_dir(app_dir: Path, rel_path: Path) -> Path:
    canonical_dir = app_dir / rel_path.parent
    page_path = canonical_dir / 'page.mdx'

    if rel_path.parent.name == rel_path.stem and is_generated_notebook_wrapper(page_path, rel_path.name):
        return canonical_dir

    return canonical_dir / rel_path.stem

def sync_notebooks():
    repo_root = Path(__file__).parent.parent.resolve()
    jupyter_dir = repo_root / "jupyter-notebooks"
    app_dir = repo_root / "next-docs" / "src" / "app"

    if not jupyter_dir.exists():
        print(f"Source directory {jupyter_dir} does not exist.")
        return

    synced_dirs = set()

    for root, _, files in os.walk(jupyter_dir):
        for file in files:
            if not file.endswith('.ipynb'):
                continue
                
            src_file = Path(root) / file
            rel_path = src_file.relative_to(jupyter_dir)
            
            # The target app directory for this notebook
            target_dir = get_target_dir(app_dir, rel_path)
            target_dir.mkdir(parents=True, exist_ok=True)
            
            target_file = target_dir / file
            # Copy the notebook file over
            shutil.copy2(src_file, target_file)
            
            # Generate the `page.mdx` wrapper
            mdx_file = target_dir / 'page.mdx'
            mdx_content = f"""---
title: \"{clean_title(rel_path.stem)}\"
---

import DynamicNotebook from '@/components/DynamicNotebook';
import nb from './{file}';

<DynamicNotebook ipynb={{nb}} />
"""
            # Always overwrite to ensure exact sync
            with open(mdx_file, 'w') as f:
                f.write(mdx_content)
                
            synced_dirs.add(str(target_dir))

    print(f"Successfully synced {len(synced_dirs)} notebooks from jupyter-notebooks/ to next-docs/src/app/!")
    print("Run `python3 scripts/generate_meta_sequential.py` to update the Nextra routing maps.")

if __name__ == '__main__':
    sync_notebooks()
