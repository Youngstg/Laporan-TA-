import re

with open('chapters/chapter-4.tex', 'r', encoding='utf-8') as f:
    text = f.read()

def repl2(match):
    start = match.start()
    if start >= 6 and text[start-6:start] == '\\fbox{':
        return match.group(0)
    return '\\fbox{' + match.group(0) + '}'

# Only match includegraphics for aug_ and sampel_blurred
text = re.sub(r'\\includegraphics(?:\[.*?\])?\{figure/(?:aug|sampel_blurred)[^\}]+\}', repl2, text)

with open('chapters/chapter-4.tex', 'w', encoding='utf-8') as f:
    f.write(text)

print('Added fbox to aug and sampel_blurred images.')
