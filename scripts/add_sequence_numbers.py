import os
import re
import glob
from pathlib import Path

def main():
    curr_dirs = sorted(glob.glob("[0-3][0-9]-*"))
    rename_map = {}
    FILE_PATT = re.compile(r'^(\d+)[_\-]?(.*)$')

    for d in curr_dirs:
        p = Path(d)
        if not p.is_dir(): continue
        
        files = []
        for f in p.iterdir():
            if f.is_file() and f.suffix in ['.md', '.ipynb'] and not f.name.startswith('README'):
                files.append(f)
        
        def sort_key(f):
            # Special case for core files
            if 'START_HERE' in f.name:
                return (-2, 0, f.name)
            if 'intro' in f.name.lower() or 'quickstart' in f.name.lower():
                # We still consider them early, but keep their numeric sort if they have one
                # Actually let's just rely on existing numbers, then string sort
                pass
            m = FILE_PATT.match(f.name)
            # If it's START_HERE, force it to the very top.
            if m:
                return (0, int(m.group(1)), f.name)
            return (1, 0, f.name)
        
        files.sort(key=sort_key)
        
        counter = 1
        for f in files:
            # Special handle for 00_START_HERE.ipynb
            if 'START_HERE' in f.name:
                m = FILE_PATT.match(f.name)
                base = m.group(2) if m else f.name
                new_name = f"00_{base.lstrip('_')}"
                if new_name != f.name:
                    rename_map[str(f)] = str(f.parent / new_name)
                continue
                
            m = FILE_PATT.match(f.name)
            if m:
                base_name = m.group(2)
            else:
                base_name = f.name
            
            base_name = base_name.lstrip('_').lstrip('-')
            
            new_name = f"{counter:02d}_{base_name}"
            counter += 1
                
            if new_name != f.name:
                new_path = f.parent / new_name
                rename_map[str(f)] = str(new_path)

    for old, new in list(rename_map.items())[:20]:
        print(f"{old} -> {new}")
    print(f"Total renames planned: {len(rename_map)}")

if __name__ == '__main__':
    main()
