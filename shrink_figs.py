import re

with open('chapters/chapter-4.tex', 'r', encoding='utf-8') as f:
    text = f.read()

# For aug_mixup, aug_cutmix, and aug_reprob figures, we replace the minipage width and subfigure widths

def shrink_figures(match):
    content = match.group(0)
    # Replace the minipage width
    content = content.replace(r'\begin{minipage}{0.97\linewidth}', r'\begin{minipage}{0.65\linewidth}')
    # Replace subfigure width
    content = content.replace(r'\begin{subfigure}[t]{0.47\textwidth}', r'\begin{subfigure}[t]{0.48\linewidth}')
    return content

# We can match each figure block
for fig_name in ['aug_mixup', 'aug_cutmix', 'aug_reprob']:
    pattern = r'\\begin\{figure\}\[H\].*?\\label\{fig:4\.' + fig_name + r'\}.*?\\end\{figure\}'
    text = re.sub(pattern, shrink_figures, text, flags=re.DOTALL)

with open('chapters/chapter-4.tex', 'w', encoding='utf-8') as f:
    f.write(text)

print("Replacement done.")
