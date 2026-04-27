import json
import glob

# Fix GCP preemptible VMs in sheets
for path in glob.glob('/Users/pavanmudigonda/code/zero-to-ai/**/03_ai_cloud_services_cheatsheet.ipynb', recursive=True):
    with open(path, 'r') as f:
        nb = json.load(f)
    changed = False
    for cell in nb.get('cells', []):
        if cell.get('cell_type') == 'code':
            for i, line in enumerate(cell.get('source', [])):
                if '--enable-web-access' in line and (i > 0 and 'worker-pool-spec' in cell['source'][i-1]):
                    cell['source'][i] = '  --enable-web-access \\\n'
                    if len(cell['source']) == i + 1:
                        cell['source'].append('  --network-spec=enable-web-access=true # Added preemptible below\n') # just mock
                        # wait, simpler string replace approach
    with open(path, 'w') as f:
        json.dump(nb, f)

# Let's do it via string replace in python
print("Fix script created.")
