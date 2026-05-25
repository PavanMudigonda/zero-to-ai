import os
import shutil
from pathlib import Path
from utils import clean_title

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
            
            target_dir = get_target_dir(app_dir, rel_path)
            target_dir.mkdir(parents=True, exist_ok=True)
            
            target_file = target_dir / file
            shutil.copy2(src_file, target_file)
            
            mdx_file = target_dir / 'page.mdx'
            mdx_content = f"""---
title: "{clean_title(rel_path.stem)}"
---

import DynamicNotebook from '@/components/DynamicNotebook';
import nb from './{file}';

<DynamicNotebook ipynb={{nb}} />
"""
            mdx_file.write_text(mdx_content, encoding='utf-8')
            synced_dirs.add(str(target_dir))

    print(f"Successfully synced {len(synced_dirs)} notebooks from jupyter-notebooks/ to next-docs/src/app/!")
    print("Run `python3 scripts/generate_meta_sequential.py` to update the Nextra routing maps.")

    # Copy cheat sheet PNGs into next-docs/public/cheatsheets/
    cheatsheets_src = repo_root / "jupyter-notebooks" / "32-cheatsheets" / "ai-ml"
    cheatsheets_dst = repo_root / "next-docs" / "public" / "cheatsheets"
    copied_pngs = 0
    if cheatsheets_src.exists():
        cheatsheets_dst.mkdir(parents=True, exist_ok=True)
        for png in cheatsheets_src.rglob("*.png"):
            dest = cheatsheets_dst / png.name
            shutil.copy2(png, dest)
            copied_pngs += 1
        print(f"Copied {copied_pngs} cheat sheet PNG(s) to next-docs/public/cheatsheets/")
        print("  Served at /cheatsheets/<filename>.png on the static site.")

if __name__ == '__main__':
    sync_notebooks()
