#!/usr/bin/env python3
"""
Progress tracking utility for Zero-to-AI learning path.
"""

import json
import os
from pathlib import Path
from datetime import datetime

class ProgressTracker:
    """Track learning progress through the curriculum."""

    def __init__(self, progress_file="progress.json"):
        self.progress_file = Path(progress_file)
        self.progress = self.load_progress()

    def load_progress(self):
        """Load progress from file."""
        if self.progress_file.exists():
            with open(self.progress_file, 'r') as f:
                return json.load(f)
        return {"start_date": datetime.now().isoformat(), "phases": {}}

    def save_progress(self):
        """Save progress to file."""
        with open(self.progress_file, 'w') as f:
            json.dump(self.progress, f, indent=2)

    def update_phase(self, phase, completed_items):
        """Update progress for a specific phase."""
        if phase not in self.progress["phases"]:
            self.progress["phases"][phase] = {"completed": [], "total": 0}

        self.progress["phases"][phase]["completed"] = list(set(
            self.progress["phases"][phase]["completed"] + completed_items
        ))

    def get_summary(self):
        """Get progress summary."""
        total_completed = sum(len(phase["completed"]) for phase in self.progress["phases"].values())
        return {
            "start_date": self.progress["start_date"],
            "total_completed": total_completed,
            "phases": self.progress["phases"]
        }

def main():
    """Main function to display progress."""
    tracker = ProgressTracker()

    print("🚀 Zero-to-AI Progress Tracker")
    print("=" * 40)

    summary = tracker.get_summary()
    print(f"Started: {summary['start_date'][:10]}")
    print(f"Total completed items: {summary['total_completed']}")

    if summary["phases"]:
        print("\nPhase Progress:")
        for phase, data in summary["phases"].items():
            completed = len(data["completed"])
            print(f"  {phase}: {completed} items completed")
    else:
        print("\nNo progress recorded yet. Start learning!")

    print("\n💡 Tip: Run this script anytime to check your progress!")

if __name__ == "__main__":
    main()