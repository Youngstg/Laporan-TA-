import re

with open('chapters/chapter-2.tex', 'r', encoding='utf-8') as f:
    text = f.read()

# Pattern to find \footnotesize followed by \begin{tabular} ... \end{tabular}
pattern = r'(\t\footnotesize\n\\begin\{tabular\}(?:.|[\r\n])*?\\end\{tabular\})'

def repl(match):
    return '\\begingroup\n' + match.group(1) + '\n\t\\endgroup'

# But let's check if they are already wrapped
new_text = re.sub(pattern, repl, text)

with open('chapters/chapter-2.tex', 'w', encoding='utf-8') as f:
    f.write(new_text)

print(f"Replaced {len(re.findall(pattern, text))} occurrences.")
