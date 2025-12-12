#!/usr/bin/env python3
"""
View current learning progress across all phases
"""

import json
from pathlib import Path

def load_progress():
    tracker_file = Path("progress_tracker.json")
    if tracker_file.exists():
        with open(tracker_file, 'r') as f:
            return json.load(f)
    return None

def progress_bar(percentage, width=30):
    filled = int(width * percentage / 100)
    return f"[{'█' * filled}{'░' * (width - filled)}]"

def main():
    data = load_progress()
    if not data:
        print("❌ No progress data found. Run track_progress.py first.")
        return
    
    stats = data['statistics']
    total = data['metadata']['total_notebooks']
    completed = stats['total_completed']
    percentage = stats['completion_percentage']
    
    print("\n" + "="*70)
    print("🎓 AI/ML Learning Journey - Progress Dashboard".center(70))
    print("="*70)
    print(f"\n📊 Overall: {completed}/{total} notebooks ({percentage}%)")
    print(progress_bar(percentage, 50))
    
    print("\n📚 Phase Progress:\n")
    
    for phase_key in sorted(data['phases'].keys()):
        phase_data = data['phases'][phase_key]
        name = phase_data.get('name', phase_key)
        total_phase = phase_data.get('total_notebooks', 0)
        completed_phase = len(phase_data.get('completed', []))
        
        if total_phase > 0:
            phase_pct = round((completed_phase / total_phase * 100), 1)
            bar = progress_bar(phase_pct, 25)
            
            # Status emoji
            if completed_phase == 0:
                status = "⏳"
            elif completed_phase == total_phase:
                status = "✅"
            else:
                status = "🔄"
            
            print(f"{status} {phase_key.replace('phase_', 'Phase '):12s} {name:25s}")
            print(f"   {bar} {completed_phase:3d}/{total_phase:3d} ({phase_pct:5.1f}%)")
            print()
    
    print("="*70)
    print(f"\n💡 Keep going! {total - completed} notebooks remaining.\n")

if __name__ == "__main__":
    main()
