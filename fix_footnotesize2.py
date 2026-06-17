import re

with open('chapters/chapter-2.tex', 'r', encoding='utf-8') as f:
    text = f.read()

# Pattern to find \footnotesize \n \begin{tabular}{@{}ll} ... \end{tabular}
pattern = r'(\t?\\footnotesize\s*\\begin\{tabular\}\{@\{\}ll\}(?:.|[\r\n])*?\\end\{tabular\})'

def repl(match):
    return '\\begingroup\n' + match.group(1) + '\n\t\\endgroup'

new_text = re.sub(pattern, repl, text)

with open('chapters/chapter-2.tex', 'w', encoding='utf-8') as f:
    f.write(new_text)

print(f"Replaced {len(re.findall(pattern, text))} occurrences.")
