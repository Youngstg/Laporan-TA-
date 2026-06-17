import re

# Process chapter-3.tex
with open('chapters/chapter-3.tex', 'r', encoding='utf-8') as f:
    text3 = f.read()

# For Figure 6 (no resizebox, directly \begin{tikzpicture})
# Make sure we don't double wrap.
def wrap_tikz(m):
    start = m.start()
    if start >= 6 and text3[start-6:start] == '\\fbox{':
        return m.group(0)
    return '\\fbox{' + m.group(0) + '}'

text3 = re.sub(r'\\begin\{tikzpicture\}(.*?)\\end\{tikzpicture\}', wrap_tikz, text3, flags=re.DOTALL)

# Wait, if we wrap the inner \begin{tikzpicture}...\end{tikzpicture}, what about the resizebox?
# For Figures 7-12, they have \resizebox{...}{!}{% \begin{tikzpicture}...\end{tikzpicture} }
# If we wrap just the tikzpicture inside the resizebox, the box will be drawn BEFORE resizing.
# This means the line width of the box will also be scaled!
# But for Figures 1-5, \fbox is OUTSIDE the \resizebox!
# So for consistency, we should put \fbox outside \resizebox.
