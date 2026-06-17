import os
import re
from difflib import SequenceMatcher

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

def find_similar_paragraphs():
    chapter_dir = 'chapters'
    for filename in sorted(os.listdir(chapter_dir)):
        if not filename.endswith('.tex'):
            continue
            
        filepath = os.path.join(chapter_dir, filename)
        try:
            with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
        except:
            continue
            
        # Split by blank lines or \par
        paragraphs = re.split(r'\n\s*\n|\\par\s*\n', content)
        # remove empty
        paragraphs = [p.strip() for p in paragraphs if p.strip() and not p.strip().startswith('%')]
        
        for i in range(len(paragraphs) - 1):
            p1 = paragraphs[i]
            p2 = paragraphs[i+1]
            if len(p1) > 100 and len(p2) > 100:
                similarity = similar(p1, p2)
                if similarity > 0.8:
                    print(f"[{filename}] Possible duplicate paragraphs found! (Similarity: {similarity:.2f})")
                    print(f"Paragraph 1:\n{p1[:150]}...")
                    print(f"Paragraph 2:\n{p2[:150]}...")
                    print()
                    
if __name__ == '__main__':
    find_similar_paragraphs()
