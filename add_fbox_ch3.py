import re

with open('chapters/chapter-3.tex', 'r', encoding='utf-8') as f:
    text = f.read()

# Find where Section 3.4 starts
# It starts at \section{Ilustrasi Perhitungan Metode}
split_str = r'\\section\{Ilustrasi Perhitungan Metode\}'
parts = re.split(split_str, text)

if len(parts) < 2:
    print("Section not found!")
    exit()

before_sec = parts[0]
after_sec = split_str + parts[1]

# In after_sec, find all \begin{figure} ... \end{figure}
def add_fbox_to_tikz(match):
    fig_content = match.group(0)
    # Check if it already has \fbox
    if r'\fbox{' in fig_content:
        return fig_content
        
    # Find \begin{tikzpicture} ... \end{tikzpicture}
    # and wrap it in \fbox{ ... }
    
    # We use a sub-replacement for the tikzpicture
    def wrap_tikz(tikz_match):
        return r'\fbox{%' + '\n' + tikz_match.group(0) + '\n}'
        
    new_fig_content = re.sub(r'\\begin\{tikzpicture\}.*?\\end\{tikzpicture\}', wrap_tikz, fig_content, flags=re.DOTALL)
    
    return new_fig_content

new_after_sec = re.sub(r'\\begin\{figure\}.*?\\end\{figure\}', add_fbox_to_tikz, after_sec, flags=re.DOTALL)

with open('chapters/chapter-3.tex', 'w', encoding='utf-8') as f:
    f.write(before_sec + new_after_sec)

print("Frames added to Subchapter 3.4")
