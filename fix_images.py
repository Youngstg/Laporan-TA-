import re

with open('chapters/chapter-3.tex', 'r', encoding='utf-8') as f:
    text3 = f.read()

# For chapter-3, let's find all \begin{figure} ... \end{figure}
def process_figure3(m):
    fig = m.group(0)
    # Check if it already has \fbox
    if '\\fbox{' in fig:
        return fig
    
    # Try to find \resizebox
    if '\\resizebox' in fig:
        # Wrap the whole resizebox statement
        # Structure is usually \resizebox{...}{...}{ ... }
        # We can use a simple regex since it's well formatted
        def repl_resize(rm):
            return '\\fbox{' + rm.group(0) + '}'
        # match \resizebox{..}{..}{ ... \end{tikzpicture} ... }
        fig = re.sub(r'\\resizebox\{[^\}]+\}\{[^\}]+\}\{%?\s*\\begin\{tikzpicture\}(.*?)\\end\{tikzpicture\}%?\s*\}', repl_resize, fig, flags=re.DOTALL)
        return fig
    else:
        # Wrap tikzpicture directly
        def repl_tikz(tm):
            return '\\fbox{' + tm.group(0) + '}'
        fig = re.sub(r'\\begin\{tikzpicture\}(.*?)\\end\{tikzpicture\}', repl_tikz, fig, flags=re.DOTALL)
        return fig

text3 = re.sub(r'\\begin\{figure\}.*?\\end\{figure\}', process_figure3, text3, flags=re.DOTALL)

with open('chapters/chapter-3.tex', 'w', encoding='utf-8') as f:
    f.write(text3)


# For chapter-4
with open('chapters/chapter-4.tex', 'r', encoding='utf-8') as f:
    text4 = f.read()

# We want to remove margin for cm and lc images inside \fbox
# The pattern is \fbox{\includegraphics[...]{figure/lc_...}} or figure/cm_...
# We will replace \fbox{...} with {\setlength{\fboxsep}{0pt}\fbox{...}}
def repl_margin(m):
    inner = m.group(1)
    return '{\\setlength{\\fboxsep}{0pt}\\fbox{' + inner + '}}'

text4 = re.sub(r'\\fbox\{(\\includegraphics\[[^\]]*\]\{figure/(?:lc|cm)_[^\}]+\})\}', repl_margin, text4)

with open('chapters/chapter-4.tex', 'w', encoding='utf-8') as f:
    f.write(text4)

print("Chapter 3 and 4 processed successfully.")
