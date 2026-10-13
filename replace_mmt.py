import os
import re

def case_preserving_replace(match):
    text = match.group(0)
    if text.isupper():
        return "PYT"
    elif text.istitle():
        return "Pyt"
    else:
        return "pyt"

def process_directory(directory, exclude_dirs):
    for root, dirs, files in os.walk(directory):
        dirs[:] = [d for d in dirs if d not in exclude_dirs]
        for file in files:
            if not (file.endswith('.js') or file.endswith('.jsx') or file.endswith('.html') or file.endswith('.css') or file.endswith('.py') or file.endswith('.txt') or file.endswith('.md')):
                continue
            
            filepath = os.path.join(root, file)
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                if 'pyt' in content.lower():
                    new_content = re.sub(r'(?i)pyt', case_preserving_replace, content)
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    print(f"Updated: {filepath}")
            except Exception as e:
                print(f"Error processing {filepath}: {e}")

if __name__ == "__main__":
    base_dir = r"d:\sem 4 project\makemytrip (2)\makemytrip"
    exclude = {"node_modules", "venv", ".git", "dist", "__pycache__"}
    process_directory(base_dir, exclude)
    print("Done!")
