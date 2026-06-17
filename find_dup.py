import os
import re

def find_duplicates():
    chapter_dir = 'chapters'
    for filename in sorted(os.listdir(chapter_dir)):
        if not filename.endswith('.tex'):
            continue
            
        filepath = os.path.join(chapter_dir, filename)
        try:
            with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                lines = f.readlines()
        except:
            continue
            
        # 1. Check identical consecutive lines (long enough)
        for i in range(len(lines) - 1):
            line1 = lines[i].strip()
            line2 = lines[i+1].strip()
            
            if len(line1) > 50 and line1 == line2 and not line1.startswith('%'):
                print(f"[{filename}] Consecutive duplicate line at {i+1} and {i+2}:")
                print(f"  {line1[:100]}...")
                print()
                
        # 2. Check identical consecutive paragraphs
        try:
            with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
        except:
            continue
            
        # Split by blank lines or \par
        paragraphs = re.split(r'\n\s*\n|\\par\s*\n', content)
        # remove empty
        paragraphs = [p.strip() for p in paragraphs if p.strip()]
        
        for i in range(len(paragraphs) - 1):
            p1 = paragraphs[i]
            p2 = paragraphs[i+1]
            if len(p1) > 100 and p1 == p2 and not p1.startswith('%'):
                print(f"[{filename}] Consecutive duplicate PARAGRAPH:")
                print(f"  {p1[:100]}...")
                print()

if __name__ == '__main__':
    find_duplicates()
