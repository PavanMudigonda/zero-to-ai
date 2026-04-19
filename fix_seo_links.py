import os
import re

scan_dirs = ['curriculum']
bad_link_text_re = re.compile(r'\[(here|click here|link|this|more)\]\(([^)]+)\)', re.IGNORECASE)

for d in scan_dirs:
    for root, dirs, files in os.walk(d):
        for f in files:
            if f.endswith('.md'):
                filepath = os.path.join(root, f)
                with open(filepath, 'r', encoding='utf-8') as file:
                    content = file.read()
                
                if bad_link_text_re.search(content):
                    # For simplicity, we'll replace "[here](url)" with "[this resource](url)"
                    # or similar, but ideally we contextualize. 
                    # Let's just flag exactly what they are so we can fix them precisely.
                    print(f"File: {filepath}")
                    for match in bad_link_text_re.finditer(content):
                        print(f"  Match: {match.group(0)}")
