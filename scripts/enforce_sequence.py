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
                
        if not files:
            continue
            
        def get_rank(f):
            name_lower = f.name.lower()
            if 'start_here' in name_lower:
                return -3, 0
            if 'intro' in name_lower or 'overview' in name_lower or 'concept' in name_lower:
                return -2, 0
            if 'quickstart' in name_lower or 'setup' in name_lower:
                return -1, 0
                
            m = FILE_PATT.match(f.name)
            if m:
                return 0, int(m.group(1))
                
            return 1, 0

        files.sort(key=lambda x: (get_rank(x), x.name))
        
        counter = 1
        for f in files:
            m = FILE_PATT.match(f.name)
            if m:
                base_name = m.group(2)
            else:
                base_name = f.name
                
            base_name = base_name.lstrip('_').lstrip('-')
            
            # Format cleanly to 2 digits
            new_name = f"{counter:02d}_{base_name}"
            counter += 1
            
            if new_name != f.name:
                rename_map[str(f)] = str(f.parent / new_name)

    print(f"Planning to rename {len(rename_map)} files...")
    
    # DO THE RENAME
    for old_path, new_path in rename_map.items():
        os.rename(old_path, new_path)
        
    print("Files renamed locally. Updating internal links...")
    
    # Recursively update any reference to the old filename
    # We sort by length descending to prevent partial replacements overlapping
    sorted_renames = sorted(rename_map.items(), key=lambda x: len(Path(x[0]).name), reverse=True)
    all_docs = list(Path('.').rglob('*.md')) + list(Path('.').rglob('*.ipynb'))
    
    changed_count = 0
    for doc in all_docs:
        current_path = Path(rename_map.get(str(doc), str(doc)))
        if not current_path.exists():
            continue
            
        try:
            content = current_path.read_text(encoding='utf-8')
        except UnicodeDecodeError:
            continue
            
        new_content = content
        for old_p, new_p in sorted_renames:
            old_name = Path(old_p).name
            new_name = Path(new_p).name
            
            pattern = r'(?<=[\/(\["\']| )' + re.escape(old_name) + r'(?=[)\]"\']| |#|$)'
            new_content = re.sub(pattern, new_name, new_content)
            
        if content != new_content:
            current_path.write_text(new_content, encoding='utf-8')
            changed_count += 1
            
    print(f"Updated internal links across {changed_count} files.")

if __name__ == '__main__':
    main()
