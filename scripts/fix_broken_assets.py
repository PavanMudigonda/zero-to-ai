import sys
import re
from pathlib import Path

BROKEN_KEYWORDS = [
    "PDSH-cover-small.png",
    "euroscipy_2016_logo.png",
    "keras-logo-small.jpg",
    "attachment:image.png",
    "numpy_indexing.png"
]

def fix_html_file(file_path):
    try:
        content = file_path.read_text(encoding='utf-8')
    except:
        return False
        
    has_broken = False
    for kw in BROKEN_KEYWORDS:
        if kw in content:
            has_broken = True
            break
            
    if not has_broken:
        return False

    old_content = content
    # Remove img tags containing broken keywords
    for kw in BROKEN_KEYWORDS:
        # Regex to match <img ... src="...kw..." ... >
        # This is a bit simplified but usually works for generated HTML
        pattern = r'<img[^>]*src="[^"]*' + re.escape(kw) + r'[^"]*"[^>]*>'
        content = re.sub(pattern, '', content)
        
        # Also clean up orphaned <p></p> or empty figure tags that might result
        # Sphinx usually wraps images in a figure or p
        content = re.sub(r'<p>\s*</p>', '', content)
        content = re.sub(r'<figure[^>]*>\s*</figure>', '', content)

    if old_content != content:
        file_path.write_text(content, encoding='utf-8')
        return True
    return False

def main(build_dir):
    site_path = Path(build_dir)
    print(f"Scanning {site_path} for broken assets...")
    count = 0
    for html_file in site_path.rglob("*.html"):
        if fix_html_file(html_file):
            count += 1
            
    print(f"Fixed broken assets in {count} files.")

if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "site")
