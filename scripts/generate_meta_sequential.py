import os
import json
from pathlib import Path
import re

def get_sort_key(name):
    match = re.match(r'^(\d+)[_-]', name)
    if match:
        return (int(match.group(1)), name)
    return (float('inf'), name)

def clean_title(name):
    name = re.sub(r'^\d+[_-]', '', name)
    name = name.replace('_', ' ').replace('-', ' ')
    name = ' '.join(word.capitalize() for word in name.split())
    name = name.replace('Specializations ', '')
    return name

def has_valid_page(directory):
    for root, dirs, files in os.walk(directory):
        dirs[:] = [d for d in dirs if not (d.startswith('.') or d.startswith('_'))]
        files = [f for f in files if not (f.startswith('.') or f.startswith('_'))]
        for f in files:
            if f in ('page.mdx', 'page.md', 'page.tsx', 'page.jsx'):
                return True
    return False

def main():
    app_dir = Path("/Users/pavanmudigonda/code/zero-to-ai/next-docs/src/app")
    top_level_routes = []
    
    for root, dirs, files in os.walk(app_dir):
        all_items = sorted(dirs + files, key=get_sort_key)
        
        valid_items = []
        for item in all_items:
            if item.startswith('.') or item.startswith('_') or item in ['layout.tsx', 'globals.css', 'favicon.ico', 'next-env.d.ts']:
                continue
                
            item_path = Path(root) / item
            
            if item_path.is_file():
                if not item in ('page.mdx', 'page.md', 'page.tsx', 'page.jsx'):
                    continue
            elif item_path.is_dir():
                if not has_valid_page(item_path):
                    continue
                    
            orig_name = item
            if item_path.is_file() and '.' in item:
                orig_name = item.rsplit('.', 1)[0]
                
            if orig_name in ['layout', 'demo', 'favicon']:
                continue
                
            if orig_name == 'page':
                continue
                
            valid_items.append((item, orig_name))
            
        if not valid_items:
            continue
            
        is_root = Path(root) == app_dir
            
        meta_dict = {}
        for index, (item, route_name) in enumerate(valid_items, 1):
            cleaned = clean_title(route_name)
            formatted_title = f"{index}. {cleaned}"
            meta_dict[route_name] = formatted_title
            
            if is_root:
                top_level_routes.append({"title": formatted_title, "href": f"/{route_name}"})
            
        if meta_dict:
            meta_path = Path(root) / "_meta.ts"
            
            if is_root:
                meta_dict = {
                    "index": {
                        "title": "Home"
                    },
                    **meta_dict
                }
                
            with open(meta_path, 'w') as f:
                f.write("export default {\n")
                for key, value in meta_dict.items():
                    if isinstance(value, dict):
                        f.write(f'  "{key}": {json.dumps(value, indent=4)}\n')
                    else:
                        safe_key = f'"{key}"' if not key.isidentifier() else key
                        safe_value = value.replace('"', '\\"')
                        f.write(f'  {safe_key}: "{safe_value}",\n')
                f.write("}\n")
            print(f"Generated {meta_path}")

    cards_mdx = "\n<Cards num={3}>\n"
    for r in top_level_routes:
        cards_mdx += f'  <Cards.Card title="{r["title"]}" href="{r["href"]}" arrow />\n'
    cards_mdx += "</Cards>\n"

    page_mdx_path = app_dir / "page.mdx"
    if page_mdx_path.exists():
        with open(page_mdx_path, "r") as f:
            content = f.read()
        new_content = re.sub(r'<Cards[\s\S]*?<\/Cards>', cards_mdx.strip(), content)
        with open(page_mdx_path, "w") as f:
            f.write(new_content)
        print("Updated page.mdx with the latest categories.")

if __name__ == '__main__':
    main()
