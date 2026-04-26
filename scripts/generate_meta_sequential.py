import os
import json
from pathlib import Path
import re

def get_sort_key(name):
    """Extract numeric prefix for sorting"""
    match = re.match(r'^(\d+)_', name)
    if match:
        return (int(match.group(1)), name)
    return (float('inf'), name)

def clean_title(name):
    """Clean the name for display"""
    # Remove numeric prefixes
    name = re.sub(r'^\d+_', '', name)
    # Replace underscores and hyphens with spaces
    name = name.replace('_', ' ').replace('-', ' ')
    # Capitalize words
    name = ' '.join(word.capitalize() for word in name.split())
    # Shorten common prefixes/suffixes if needed
    name = name.replace('Specializations ', '')
    return name

def main():
    app_dir = Path("/Users/pavanmudigonda/code/zero-to-ai/next-docs/src/app")
    
    for root, dirs, files in os.walk(app_dir):
        # We only generate _meta.ts for directories that contain subdirectories or actual readable files
        # We skip the root app directory to preserve custom _meta.ts or layout
        
        all_items = sorted(dirs + files, key=get_sort_key)
        
        valid_items = []
        for item in all_items:
            # Skip hidden files/dirs and internal Next.js/Nextra files
            if item.startswith('.') or item.startswith('_') or item in ['layout.tsx', 'globals.css', 'favicon.ico', 'next-env.d.ts']:
                continue
                
            item_path = Path(root) / item
            if item_path.is_file():
                # Only include valid nextra page extensions
                if not item.endswith(('.mdx', '.md', '.tsx', '.jsx')):
                    continue
                
            orig_name = item
            if '.' in item:
                # Provide the chunk before the extension as the route segment
                orig_name = item.rsplit('.', 1)[0]
                
            # If the item is itself exactly "page", we don't list it in _meta.ts directly.
            # Nextra assigns the folder's name to the page.mdx inside it automatically
            # if we define the folder route in the PARENT's _meta.ts.
            # However, if we are INSIDE the folder, we don't declare "page": "..." usually, 
            # because Next.js App Router attaches `page.mdx` to the root of the current folder.
            if orig_name in ['page', 'layout', 'demo', 'favicon']:
                continue
                
            valid_items.append((item, orig_name))
            
        if not valid_items:
            continue
            
        # Create meta dictionary
        meta_dict = {}
        for index, (item, route_name) in enumerate(valid_items, 1):
            # Prepend sequential number to clean title
            cleaned = clean_title(route_name)
            meta_dict[route_name] = f"{index}. {cleaned}"
            
        # Write _meta.ts
        if meta_dict:
            meta_path = Path(root) / "_meta.ts"
            
            # If we are at the app root, inject the root page definition
            if Path(root) == app_dir:
                meta_dict = {
                    "page": {
                        "title": "Zero to AI",
                        "display": "hidden"
                    },
                    **meta_dict
                }
                
            with open(meta_path, 'w') as f:
                f.write("export default {\n")
                for key, value in meta_dict.items():
                    # Handle dict values
                    if isinstance(value, dict):
                        f.write(f'  "{key}": {json.dumps(value, indent=4).replace("}", "  }")},\n')
                    else:
                        # Handle keys with hyphens or spaces
                        safe_key = f'"{key}"' if not key.isidentifier() else key
                        # Safe quotes for value
                        safe_value = value.replace('"', '\\"')
                        f.write(f'  {safe_key}: "{safe_value}",\n')
                f.write("}\n")
            print(f"Generated {meta_path}")

if __name__ == '__main__':
    main()
