import os
import re

def create_readme_template(folder_name):
    title = folder_name.replace('-', ' ').title()
    # Remove the leading numbers for the title
    title = re.sub(r'^\d+\s', '', title)
    
    return f"""# {title}

## 🎯 Learning Objectives
- [ ] Objective 1
- [ ] Objective 2
- [ ] Objective 3

## ⏱️ Time Estimate
- **Expected time:** 2-4 hours

## 📚 Prerequisites
- Completion of previous modules.
- Basic understanding of [Concept].

## 🛠️ Deliverables
- [ ] Completed notebooks.
- [ ] Mini-project or practical implementation.

## 📖 Resources
- [Resource 1](link)
- [Resource 2](link)
"""

def main():
    workspace_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    
    # regex to match folder names like 00-course-setup, 01-python, etc.
    pattern = re.compile(r'^\d{2}-.*')
    
    folders_updated = 0
    folders_skipped = 0
    
    for item in sorted(os.listdir(workspace_root)):
        item_path = os.path.join(workspace_root, item)
        if os.path.isdir(item_path) and pattern.match(item):
            readme_path = os.path.join(item_path, 'README.md')
            if not os.path.exists(readme_path):
                with open(readme_path, 'w') as f:
                    f.write(create_readme_template(item))
                print(f"✅ Created README.md in {item}/")
                folders_updated += 1
            else:
                print(f"⏭️  Skipped {item}/ (README.md already exists)")
                folders_skipped += 1
                
    print(f"\nSummary: Created {folders_updated} READMEs, Skipped {folders_skipped} Existing READMEs.")

if __name__ == "__main__":
    main()
