#!/usr/bin/env python3
"""
Progress Tracker for AI/ML Learning Repository
Track completion of 732 notebooks across 14 phases
"""

import json
import os
from pathlib import Path
from datetime import datetime
from typing import List, Dict, Optional

class ProgressTracker:
    def __init__(self, tracker_file: str = "progress_tracker.json"):
        self.tracker_file = Path(tracker_file)
        self.data = self.load_progress()
    
    def load_progress(self) -> Dict:
        """Load progress from JSON file"""
        if self.tracker_file.exists():
            with open(self.tracker_file, 'r') as f:
                return json.load(f)
        return self._create_default_structure()
    
    def save_progress(self):
        """Save progress to JSON file"""
        self.data['metadata']['last_updated'] = datetime.now().strftime("%Y-%m-%d")
        with open(self.tracker_file, 'w') as f:
            json.dump(self.data, f, indent=2)
        print(f"✅ Progress saved to {self.tracker_file}")
    
    def mark_complete(self, phase: str, notebook: str):
        """Mark a notebook as complete"""
        phase_key = f"phase_{phase}" if not phase.startswith("phase_") else phase
        
        if phase_key not in self.data['phases']:
            print(f"❌ Phase {phase} not found")
            return
        
        completed = self.data['phases'][phase_key].get('completed', [])
        if notebook not in completed:
            completed.append(notebook)
            self.data['phases'][phase_key]['completed'] = completed
            self._update_statistics()
            self.save_progress()
            print(f"✅ Marked complete: {notebook} in {phase_key}")
        else:
            print(f"ℹ️  Already completed: {notebook}")
    
    def mark_incomplete(self, phase: str, notebook: str):
        """Unmark a notebook as complete"""
        phase_key = f"phase_{phase}" if not phase.startswith("phase_") else phase
        
        if phase_key in self.data['phases']:
            completed = self.data['phases'][phase_key].get('completed', [])
            if notebook in completed:
                completed.remove(notebook)
                self.data['phases'][phase_key]['completed'] = completed
                self._update_statistics()
                self.save_progress()
                print(f"✅ Marked incomplete: {notebook}")
    
    def _update_statistics(self):
        """Update overall statistics"""
        total_completed = sum(
            len(phase.get('completed', []))
            for phase in self.data['phases'].values()
        )
        total_notebooks = self.data['metadata']['total_notebooks']
        
        self.data['statistics']['total_completed'] = total_completed
        self.data['statistics']['completion_percentage'] = round(
            (total_completed / total_notebooks * 100) if total_notebooks > 0 else 0, 2
        )
    
    def show_progress(self):
        """Display current progress"""
        stats = self.data['statistics']
        total = self.data['metadata']['total_notebooks']
        completed = stats['total_completed']
        percentage = stats['completion_percentage']
        
        print("\n" + "="*60)
        print("📊 AI/ML Learning Progress")
        print("="*60)
        print(f"Total Notebooks: {total}")
        print(f"Completed: {completed}")
        print(f"Remaining: {total - completed}")
        print(f"Progress: {self._progress_bar(percentage)} {percentage}%")
        print("="*60)
        
        print("\n📚 Progress by Phase:\n")
        for phase_key, phase_data in self.data['phases'].items():
            name = phase_data.get('name', phase_key)
            total_phase = phase_data.get('total_notebooks', 0)
            completed_phase = len(phase_data.get('completed', []))
            
            if total_phase > 0:
                phase_pct = round((completed_phase / total_phase * 100), 1)
                bar = self._progress_bar(phase_pct, width=20)
                status = "✅" if completed_phase == total_phase else "🔄"
                print(f"{status} {name:30s} {bar} {completed_phase}/{total_phase} ({phase_pct}%)")
        
        print("\n" + "="*60)
    
    def _progress_bar(self, percentage: float, width: int = 30) -> str:
        """Generate a visual progress bar"""
        filled = int(width * percentage / 100)
        bar = "█" * filled + "░" * (width - filled)
        return f"[{bar}]"
    
    def export_to_markdown(self, output_file: str = "PROGRESS.md"):
        """Export progress to markdown file"""
        stats = self.data['statistics']
        total = self.data['metadata']['total_notebooks']
        completed = stats['total_completed']
        percentage = stats['completion_percentage']
        
        with open(output_file, 'w') as f:
            f.write("# AI/ML Learning Progress\n\n")
            f.write(f"**Last Updated:** {self.data['metadata']['last_updated']}\n\n")
            f.write(f"## Overall Progress\n\n")
            f.write(f"- **Total Notebooks:** {total}\n")
            f.write(f"- **Completed:** {completed}\n")
            f.write(f"- **Remaining:** {total - completed}\n")
            f.write(f"- **Progress:** {percentage}%\n\n")
            
            f.write("## Phase Breakdown\n\n")
            f.write("| Phase | Name | Completed | Total | Progress |\n")
            f.write("|-------|------|-----------|-------|----------|\n")
            
            for phase_key, phase_data in self.data['phases'].items():
                name = phase_data.get('name', phase_key)
                total_phase = phase_data.get('total_notebooks', 0)
                completed_phase = len(phase_data.get('completed', []))
                
                if total_phase > 0:
                    phase_pct = round((completed_phase / total_phase * 100), 1)
                    f.write(f"| {phase_key.replace('phase_', '')} | {name} | {completed_phase} | {total_phase} | {phase_pct}% |\n")
        
        print(f"✅ Progress exported to {output_file}")
    
    def _create_default_structure(self) -> Dict:
        """Create default progress structure"""
        return {
            "metadata": {
                "total_notebooks": 732,
                "last_updated": datetime.now().strftime("%Y-%m-%d"),
                "repository": "zero-to-ai",
                "owner": "PavanMudigondaTR"
            },
            "phases": {},
            "statistics": {
                "total_completed": 0,
                "completion_percentage": 0.0,
                "current_phase": "phase_0",
                "notebooks_this_week": 0,
                "streak_days": 0
            }
        }


def main():
    """Main CLI interface"""
    import sys
    
    tracker = ProgressTracker()
    
    if len(sys.argv) < 2:
        tracker.show_progress()
        return
    
    command = sys.argv[1]
    
    if command == "complete" and len(sys.argv) >= 4:
        phase = sys.argv[2]
        notebook = sys.argv[3]
        tracker.mark_complete(phase, notebook)
    
    elif command == "incomplete" and len(sys.argv) >= 4:
        phase = sys.argv[2]
        notebook = sys.argv[3]
        tracker.mark_incomplete(phase, notebook)
    
    elif command == "show":
        tracker.show_progress()
    
    elif command == "export":
        output = sys.argv[2] if len(sys.argv) >= 3 else "PROGRESS.md"
        tracker.export_to_markdown(output)
    
    else:
        print("Usage:")
        print("  python track_progress.py                          # Show progress")
        print("  python track_progress.py show                     # Show progress")
        print("  python track_progress.py complete PHASE NOTEBOOK  # Mark complete")
        print("  python track_progress.py incomplete PHASE NOTEBOOK # Mark incomplete")
        print("  python track_progress.py export [FILE]            # Export to markdown")
        print("\nExamples:")
        print("  python track_progress.py complete 3 tiktoken_example.ipynb")
        print("  python track_progress.py export MY_PROGRESS.md")


if __name__ == "__main__":
    main()
