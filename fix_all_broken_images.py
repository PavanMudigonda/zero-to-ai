import sys
import subprocess
import re

def run_build():
    print("Running next build...")
    result = subprocess.run(["npm", "run", "build"], cwd="next-docs", capture_output=True, text=True)
    return result.stdout + result.stderr

def fix_errors():
    while True:
        output = run_build()
        if "Failed to compile." not in output and "Error:" not in output:
            if "Compiled successfully" in output or "optimized production build" in output and "Error:" not in output and "Failed to compile." not in output:
                # Need to be sure it actually passed exported phase
                if "Export successful" in output or "Finalizing page optimization" in output:
                    print("Build succeeded!")
                    break
        
        print("Build failed. Analyzing errors...")
        
        # Regex to find:
        # ./src/app/.../page.mdx
        # Module not found: Can't resolve 'some_image.png'
        pattern = r"\.\/src\/(.+?\.mdx).*?Module not found: Can't resolve '(.*?)'"
        matches = re.finditer(pattern, output, re.DOTALL | re.IGNORECASE)
        
        fixed_count = 0
        for match in matches:
            filepath = "next-docs/src/" + match.group(1).strip()
            missing_module = match.group(2).strip()
            
            print(f"Fixing {missing_module} in {filepath}")
            
            try:
                with open(filepath, "r", encoding="utf-8") as f:
                    lines = f.readlines()
                
                with open(filepath, "w", encoding="utf-8") as f:
                    for line in lines:
                        if missing_module not in line:
                            f.write(line)
                        else:
                            print(f"  Removed line: {line.strip()}")
                fixed_count += 1
            except Exception as e:
                print(f"Failed to edit {filepath}: {e}")
                
        if fixed_count == 0:
            print("Could not find any errors to automatically fix. Exiting.")
            # Print the tail of the log for debugging
            print(output[-1000:])
            break

if __name__ == "__main__":
    fix_errors()
