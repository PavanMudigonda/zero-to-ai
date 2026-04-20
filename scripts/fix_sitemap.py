import sys
import xml.etree.ElementTree as ET
from pathlib import Path

def fix_sitemap(build_dir):
    sitemap_path = Path(build_dir) / 'sitemap.xml'
    if not sitemap_path.exists():
        print(f"No sitemap found at {sitemap_path}")
        return
        
    ET.register_namespace('', "http://www.sitemaps.org/schemas/sitemap/0.9")
    tree = ET.parse(sitemap_path)
    root = tree.getroot()
    namespace = '{http://www.sitemaps.org/schemas/sitemap/0.9}'
    
    for url in root.findall(f'.//{namespace}url'):
        loc = url.find(f'{namespace}loc')
        if loc is not None and loc.text:
            new_text = loc.text
            # Remove .html extension
            if new_text.endswith('.html'):
                new_text = new_text[:-5]
            # Remove trailing README or index
            if new_text.endswith('/README'):
                new_text = new_text[:-6]
            if new_text.endswith('/index'):
                new_text = new_text[:-5]
            # If the site root is just 'index', remove it
            if new_text.endswith('zero-to-ai.dev/index'):
                new_text = new_text[:-5]
            loc.text = new_text

    tree.write(sitemap_path, xml_declaration=True, encoding='utf-8', method='xml')
    print("Sitemap URLs cleaned for extensionless hosting.")

if __name__ == '__main__':
    fix_sitemap(sys.argv[1] if len(sys.argv) > 1 else 'site')
