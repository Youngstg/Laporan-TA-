import re

with open('chapters/chapter-4.tex', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Wrap lc_ and cm_ images
def repl_lc_cm(m):
    img_cmd = m.group(0)
    return r'{\setlength{\fboxsep}{0pt}\fbox{' + img_cmd + r'}}'

pattern_lc_cm = r'\\includegraphics\[[^\]]*\]\{figure/(?:lc_|cm_)[^\}]+\}'
content = re.sub(pattern_lc_cm, repl_lc_cm, content)

# 2. Fix the broken nested fboxes in aug_orig
broken_fboxes = r"""\fbox{\begin{minipage}{0.97\linewidth}
\centering
\fbox{\begin{minipage}{0.97\linewidth}
\centering
\fbox{\begin{minipage}{0.97\linewidth}
\centering
\begin{subfigure}[b]{0.22\textwidth}"""

fixed_fboxes = r"""\makebox[\linewidth][c]{\fbox{\begin{minipage}{0.97\linewidth}
\centering
\begin{subfigure}[b]{0.22\textwidth}"""

content = content.replace(broken_fboxes, fixed_fboxes)

broken_end = r"""\end{minipage}}
\end{minipage}}
\end{minipage}}
\end{minipage}}
\hfill
  \begin{subfigure}"""

fixed_end = r"""  \end{subfigure}
  \hfill
  \begin{subfigure}"""

content = content.replace(broken_end, fixed_end)

end_of_aug = r"""    \label{fig:aug_down}
  \end{subfigure}
  \caption{Contoh"""

fixed_end_aug = r"""    \label{fig:aug_down}
  \end{subfigure}
\end{minipage}}}
  \caption{Contoh"""

content = content.replace(end_of_aug, fixed_end_aug)

# 3. Add frames to the mixup/cutmix/reprob figures
def wrap_subfigures(m):
    return r"\makebox[\linewidth][c]{\fbox{\begin{minipage}{0.97\linewidth}" + "\n" + m.group(0) + "\n" + r"\end{minipage}}}"

for prefix in ['mixup', 'cutmix', 'erase']:
    pat = r"\\begin\{subfigure\}.*?figure/aug_" + prefix + r"_asli.*?\\end\{subfigure\}\s*\\hfill\s*\\begin\{subfigure\}.*?figure/aug_" + prefix + r"_hasil.*?\\end\{subfigure\}"
    content = re.sub(pat, wrap_subfigures, content, flags=re.DOTALL)

with open('chapters/chapter-4.tex', 'w', encoding='utf-8') as f:
    f.write(content)
print("Done")
