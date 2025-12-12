#!/usr/bin/env python3
"""
View 3Blue1Brown notebooks progress
"""

from pathlib import Path

def main():
    base_path = Path("2-maths/3blue1brown")
    
    series = {
        "linear-algebra": {
            "name": "Linear Algebra",
            "total": 16,
            "completed": []
        },
        "calculus": {
            "name": "Essence of Calculus",
            "total": 12,
            "completed": []
        },
        "differential-equations": {
            "name": "Differential Equations",
            "total": 8,
            "completed": []
        },
        "neural-networks": {
            "name": "Neural Networks",
            "total": 9,
            "completed": []
        }
    }
    
    print("\n" + "="*70)
    print("🎬 3Blue1Brown Series - Notebook Status".center(70))
    print("="*70 + "\n")
    
    total_notebooks = 0
    total_completed = 0
    
    for series_key, series_data in series.items():
        series_path = base_path / series_key
        name = series_data["name"]
        total = series_data["total"]
        
        # Check which notebooks exist
        completed = []
        if series_path.exists():
            notebooks = list(series_path.glob("*.ipynb"))
            completed = [nb.name for nb in notebooks if not nb.name.startswith('.')]
        
        completed_count = len(completed)
        total_notebooks += total
        total_completed += completed_count
        
        percentage = (completed_count / total * 100) if total > 0 else 0
        
        # Status
        if completed_count == 0:
            status = "⏳"
        elif completed_count == total:
            status = "✅"
        else:
            status = "🔄"
        
        # Progress bar
        filled = int(30 * percentage / 100)
        bar = f"[{'█' * filled}{'░' * (30 - filled)}]"
        
        print(f"{status} {name:30s}")
        print(f"   {bar} {completed_count:2d}/{total:2d} ({percentage:5.1f}%)")
        
        if completed and completed_count < total:
            print(f"   📝 Created: {', '.join(sorted(completed)[:3])}")
            if len(completed) > 3:
                print(f"               ... and {len(completed) - 3} more")
        
        print()
    
    overall_pct = (total_completed / total_notebooks * 100) if total_notebooks > 0 else 0
    filled = int(50 * overall_pct / 100)
    overall_bar = f"[{'█' * filled}{'░' * (50 - filled)}]"
    
    print("="*70)
    print(f"\n📊 Overall 3Blue1Brown: {total_completed}/{total_notebooks} notebooks ({overall_pct:.1f}%)")
    print(overall_bar)
    print("\n" + "="*70 + "\n")

if __name__ == "__main__":
    main()
