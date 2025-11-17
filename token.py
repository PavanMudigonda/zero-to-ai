#!/usr/bin/env python3
"""Script to move all modern AI/ML terms after line 707 to the end of the file."""

file_path = "/Users/nagapavankumar.mudigonda/code/0-glossary/GLOSSARY.md"

# Read the file
with open(file_path, 'r') as f:
    lines = f.readlines()

# Find line 706 (0-indexed = 705) - last line before modern terms
# Delete everything after line 706
new_content = lines[:706]

# Write back
with open(file_path, 'w') as f:
    f.writelines(new_content)

print(f"Truncated file to {len(new_content)} lines")
