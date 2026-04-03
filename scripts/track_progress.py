import os
import re

def compute_progress():
    workspace_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    checklist_path = os.path.join(workspace_root, 'docs', 'checklist.md')
    
    if not os.path.exists(checklist_path):
        print("docs/checklist.md not found. To track progress, create a checklist.md with task items like '- [ ] Task 1' and '- [x] Task 2'")
        return
        
    with open(checklist_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    total_tasks = len(re.findall(r'- \[[ xX]\]', content))
    completed_tasks = len(re.findall(r'- \[[xX]\]', content))
    
    if total_tasks == 0:
        print("No tasks found in checklist.md.")
        return
        
    percentage = (completed_tasks / total_tasks) * 100
    bar_length = 40
    filled_length = int(bar_length * completed_tasks // total_tasks)
    bar = '█' * filled_length + '░' * (bar_length - filled_length)
    
    print("\n🚀 ZERO TO AI - PROGRESS TRACKER 🚀")
    print("-" * 50)
    print(f"Progress: [{bar}] {percentage:.1f}%")
    print(f"Tasks:    {completed_tasks} / {total_tasks} completed")
    print("-" * 50)
    print("Keep up the great work!\n")

if __name__ == "__main__":
    compute_progress()
