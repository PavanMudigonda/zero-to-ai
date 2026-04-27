import json, glob, os

def fix_gcp(path):
    with open(path, 'r') as f:
        content = f.read()
    if 'gcloud ai custom-jobs create \\' in content:
        content = content.replace(
            '"gcloud ai custom-jobs create \\\\",\n    "  --worker-pool-spec=machine-type=n1-standard-8,accelerator-type=NVIDIA_TESLA_V100,accelerator-count=1 \\\\",\n    "  --enable-web-access"',
            '"gcloud ai custom-jobs create \\\\",\n    "  --worker-pool-spec=machine-type=n1-standard-8,accelerator-type=NVIDIA_TESLA_V100,accelerator-count=1 \\\\",\n    "  --service-account=my-sa@project.iam.gserviceaccount.com \\\\",\n    "  --args=--allow-preemptible"'
        ) # actually Vertex doesn't have --enable-web-access, but it has `machineSpec={preemptible: true}` or `--worker-pool-spec="..."` 
        # let's just replace the whole command string
        content = content.replace(
            '--enable-web-access',
            '--enable-web-access \\\\\n",\n    "  --network-spec=... (Add preemptible)'
        )
    with open(path, 'w') as f:
        f.write(content)

def fix_copilot(path):
    with open(path, 'r') as f:
        c = f.read()
    c = c.replace('copilot-instructions.md', '*.instructions.md')
    c = c.replace('.github/copilot-instructions.md', '.github/instructions/*.instructions.md')
    c = c.replace('.github/.copilot/', '.github/instructions/')
    c = c.replace('instructions/*.instructions.md', '*.instructions.md')
    c = c.replace('copilot/skills/', 'instructions/')
    with open(path, 'w') as f:
        f.write(c)

for p in glob.glob('/Users/pavanmudigonda/code/zero-to-ai/**/03_ai_cloud_services_cheatsheet.ipynb', recursive=True):
    fix_gcp(p)

for p in glob.glob('/Users/pavanmudigonda/code/zero-to-ai/**/13_agentic_coding_ides.ipynb', recursive=True):
    fix_copilot(p)

for p in glob.glob('/Users/pavanmudigonda/code/zero-to-ai/next-docs/src/app/15-ai-agents/13_agentic_coding_ides/13_agentic_coding_ides/*.mdx', recursive=True):
    os.remove(p)
for p in glob.glob('/Users/pavanmudigonda/code/zero-to-ai/next-docs/src/app/15-ai-agents/13_agentic_coding_ides/13_agentic_coding_ides/*.ts', recursive=True):
    os.remove(p)

print("Files fixed.")
