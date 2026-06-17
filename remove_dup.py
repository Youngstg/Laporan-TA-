import os
import re
from difflib import SequenceMatcher

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

def remove_duplicate_paragraphs():
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
            
        # We need to split the document into tokens of paragraphs and separators
        # so we can rebuild it exactly, minus the duplicate paragraphs.
        
        # This regex splits keeping the separators:
        tokens = re.split(r'(\n\s*\n|\\par\s*\n)', content)
        
        new_tokens = []
        last_paragraph = None
        
        for i in range(len(tokens)):
            # Even indices are the text blocks (paragraphs), odd indices are separators.
            if i % 2 == 0:
                p = tokens[i].strip()
                if p and not p.startswith('%') and len(p) > 100:
                    if last_paragraph is not None and similar(last_paragraph, p) > 0.85:
                        # It's a duplicate. We skip this paragraph, AND we should probably skip the preceding separator
                        # to avoid leaving double blank lines, but for simplicity, we just won't append the paragraph.
                        # Wait, if we don't append it, we might leave the separator. It's better to just leave the separator
                        # so it collapses into multiple newlines (LaTeX treats multiple newlines as one \par).
                        print(f"[{filename}] Removed duplicate paragraph starting with: {p[:50]}...")
                        continue
                    else:
                        last_paragraph = p
                        new_tokens.append(tokens[i])
                else:
                    new_tokens.append(tokens[i])
                    # We don't update last_paragraph because this isn't a long valid text block
            else:
                new_tokens.append(tokens[i])
                
        # Write back
        new_content = "".join(new_tokens)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)

if __name__ == '__main__':
    remove_duplicate_paragraphs()
