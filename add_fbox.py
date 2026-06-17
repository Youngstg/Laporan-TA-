import re

with open('chapters/chapter-4.tex', 'r', encoding='utf-8') as f:
    text = f.read()

# Find \includegraphics that are NOT preceded by \fbox{
# Lookbehind is hard for variable length, so we match \fbox{\includegraphics...} or just \includegraphics...
def repl(match):
    full = match.group(0)
    if 'fbox' in full:
        return full
    else:
        # It's an \includegraphics without \fbox
        return r'\fbox{' + full + '}'

# Pattern: match optional \fbox{ then \includegraphics[...]\{...\} then optional }
pattern = r'(?:\\fbox\{)?\\includegraphics\[.*?\]\{.*?\}(?:\})?'

# Wait, the above pattern might match \fbox{\includegraphics...} and the trailing }
# Let's do it simpler. Let's just find \includegraphics[...]\{...\}
# and if the preceding 6 chars are \fbox{ we ignore it.
def repl2(match):
    start = match.start()
    if start >= 6 and text[start-6:start] == '\\fbox{':
        return match.group(0)
    return '\\fbox{' + match.group(0) + '}'

new_text = re.sub(r'\\includegraphics(?:\[.*?\])?\{.*?\}', repl2, text)

with open('chapters/chapter-4.tex', 'w', encoding='utf-8') as f:
    f.write(new_text)

print('Added fbox to includegraphics successfully.')
