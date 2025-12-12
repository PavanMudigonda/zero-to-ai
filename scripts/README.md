# Progress Tracking Scripts

Utilities for tracking your learning progress across 732 notebooks.

## Quick Start

### View Current Progress
```bash
python scripts/view_progress.py
```

Shows a visual dashboard with:
- Overall completion percentage
- Progress by phase
- Visual progress bars

### Mark Notebooks Complete
```bash
# Mark a notebook as complete
python scripts/track_progress.py complete 3 tiktoken_example.ipynb

# Mark as incomplete
python scripts/track_progress.py incomplete 3 tiktoken_example.ipynb
```

### Export Progress Report
```bash
# Export to markdown
python scripts/track_progress.py export PROGRESS.md
```

## File Structure

- **progress_tracker.json** - Stores your progress data
- **scripts/track_progress.py** - Main tracking CLI
- **scripts/view_progress.py** - Visual progress dashboard

## Usage Examples

### Example 1: Starting Your Journey
```bash
# View initial progress
python scripts/view_progress.py

# Complete first notebook
python scripts/track_progress.py complete 3 tiktoken_example.ipynb

# Check updated progress
python scripts/view_progress.py
```

### Example 2: Track Daily Progress
```bash
# Morning: Check where you left off
python scripts/view_progress.py

# During study: Mark completed notebooks
python scripts/track_progress.py complete 4 embeddings_intro.ipynb
python scripts/track_progress.py complete 4 semantic_similarity.ipynb

# Evening: Export weekly report
python scripts/track_progress.py export weekly_report.md
```

## Progress Tracker CLI

```
python scripts/track_progress.py [command] [args]

Commands:
  (no args)                          Show progress dashboard
  show                               Show progress dashboard  
  complete PHASE NOTEBOOK            Mark notebook as complete
  incomplete PHASE NOTEBOOK          Mark notebook as incomplete
  export [FILE]                      Export progress to markdown

Examples:
  python scripts/track_progress.py complete 10 01_basic_prompting.ipynb
  python scripts/track_progress.py export MY_PROGRESS.md
```

## Phase Numbers

Use these phase numbers when marking progress:

- 0 = Glossary
- 1 = Python & Data Science
- 2 = Mathematics for ML
- 3 = Tokenization
- 4 = Embeddings
- 5 = Neural Networks
- 6 = Vector Databases
- 7 = RAG Systems
- 8 = MLOps
- 9 = Specializations
- 10 = Prompt Engineering
- 11 = LLM Fine-tuning
- 12 = Multimodal AI
- 13 = Local LLMs

## Customization

Edit `progress_tracker.json` to:
- Add custom phases
- Track additional metadata
- Set learning goals
- Track streaks and milestones

## Tips

1. **Be Consistent**: Update progress daily for accurate tracking
2. **Export Weekly**: Generate reports to review your pace
3. **Set Goals**: Aim for X notebooks per week
4. **Celebrate Milestones**: Export progress at 25%, 50%, 75% completion

## Troubleshooting

**Error: FileNotFoundError**
- Make sure you're in the repository root directory
- The progress_tracker.json file should be in the same directory

**Progress not updating**
- Check phase number is correct (0-13)
- Verify notebook name matches exactly (case-sensitive)

## Integration with Checklist

The progress tracker complements checklist.md:
- Use checklist.md for manual tracking
- Use progress_tracker for automated stats
- Export progress to update README badges (future feature)
