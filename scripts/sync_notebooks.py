import os
import shutil
from pathlib import Path

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
            target_dir = app_dir / rel_path.parent / rel_path.stem
            target_dir.mkdir(parents=True, exist_ok=True)
            
            target_file = target_dir / file
            # Copy the notebook file over
            shutil.copy2(src_file, target_file)
            
            # Generate the `page.mdx` wrapper
            mdx_file = target_dir / 'page.mdx'
            mdx_content = f"""---
title: "{rel_path.stem}"
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
