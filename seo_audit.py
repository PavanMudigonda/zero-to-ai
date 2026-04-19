import os
import re
from pathlib import Path

# Paths to scan
scan_dirs = ['docs', 'curriculum']

# Regexes
empty_alt_text_re = re.compile(r'!\[\]\([^)]+\)')
bad_link_text_re = re.compile(r'\[(here|click here|link|this|more)\]\([^)]+\)', re.IGNORECASE)
h1_re = re.compile(r'^#\s+(.+)$', re.MULTILINE)

issues = {
    'empty_alt_text': [],
    'bad_link_text': [],
    'missing_h1': [],
    'non_descriptive_urls': []
}

def is_descriptive(filename):
    # Check if filename is just numbers or very short and non-descriptive
    name = Path(filename).stem
    if name.isdigit() or (len(name) < 3 and name.lower() not in ['ds', 'rl', 'ai']):
        return False
    return True

total_files = 0

for d in scan_dirs:
    for root, dirs, files in os.walk(d):
        for f in files:
            if f.endswith('.md'):
                total_files += 1
                filepath = os.path.join(root, f)
                
                # Check URL / filename
                if not is_descriptive(f):
                    issues['non_descriptive_urls'].append(filepath)
                
                with open(filepath, 'r', encoding='utf-8') as file:
                    content = file.read()
                    
                    if empty_alt_text_re.search(content):
                        issues['empty_alt_text'].append(filepath)
                        
                    if bad_link_text_re.search(content):
                        issues['bad_link_text'].append(filepath)
                        
                    if not h1_re.search(content):
                        issues['missing_h1'].append(filepath)

print(f"Scanned {total_files} markdown files.")
print("====== SEO Audit Results ======")
print(f"Missing or Empty Image Alt Text: {len(issues['empty_alt_text'])} files")
if len(issues['empty_alt_text']) > 0:
    for i in issues['empty_alt_text'][:5]: print(f" - {i}")
    if len(issues['empty_alt_text']) > 5: print("   ...")

print(f"\nPoor/'Click Here' Link Text: {len(issues['bad_link_text'])} files")
if len(issues['bad_link_text']) > 0:
    for i in issues['bad_link_text'][:5]: print(f" - {i}")
    if len(issues['bad_link_text']) > 5: print("   ...")
    
print(f"\nMissing H1 (Used for Page <title>): {len(issues['missing_h1'])} files")
if len(issues['missing_h1']) > 0:
    for i in issues['missing_h1'][:5]: print(f" - {i}")
    if len(issues['missing_h1']) > 5: print("   ...")

print(f"\nNon-Descriptive Filenames/URLs: {len(issues['non_descriptive_urls'])} files")
if len(issues['non_descriptive_urls']) > 0:
    for i in issues['non_descriptive_urls'][:5]: print(f" - {i}")
    if len(issues['non_descriptive_urls']) > 5: print("   ...")

