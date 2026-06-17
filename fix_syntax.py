import re

with open('chapters/chapter-4.tex', 'r', encoding='utf-8') as f:
    text = f.read()

# Fix Figure 4.1 (aug_contoh)
bad_fig1 = r"""\begin{figure}[H]
  \centering
  \fbox{\begin{minipage}{0.97\linewidth}
\centering
\makebox[\linewidth][c]{\fbox{\begin{minipage}{0.97\linewidth}
\centering
\makebox[\linewidth][c]{\fbox{\begin{minipage}{0.97\linewidth}
\makebox[\linewidth][c]{\fbox{\begin{minipage}{0.97\linewidth}
\makebox[\linewidth][c]{\fbox{\begin{minipage}{0.97\linewidth}
\begin{subfigure}[b]{0.22\textwidth}
    \centering
    \includegraphics[width=\textwidth]{figure/aug_orig.jpg}
    \caption{Asli}
    \label{fig:aug_orig}
  \end{subfigure}
  \end{subfigure}
  \hfill
  \begin{subfigure}[b]{0.22\textwidth}
    \centering
    \includegraphics[width=\textwidth]{figure/aug_inv.jpg}
    \caption{Inversi warna}
    \label{fig:aug_inv}
  \end{subfigure}
  \hfill
  \begin{subfigure}[b]{0.22\textwidth}
    \centering
    \includegraphics[width=\textwidth]{figure/aug_mult.jpg}
    \caption{Penguatan kecerahan}
    \label{fig:aug_mult}
  \end{subfigure}
  \hfill
  \begin{subfigure}[b]{0.22\textwidth}
    \centering
    \includegraphics[width=\textwidth]{figure/aug_down.jpg}
    \caption{Resolusi rendah}
    \label{fig:aug_down}
  \end{subfigure}
\end{minipage}}}
  \caption{Contoh \textit{frame} hasil augmentasi pada klip ``Aku'' (video ke-90, \textit{frame} ke-39)}
  \label{fig:aug_contoh}
\end{figure}"""

good_fig1 = r"""\begin{figure}[H]
  \centering
  \makebox[\linewidth][c]{\fbox{\begin{minipage}{0.97\linewidth}
  \centering
  \begin{subfigure}[b]{0.22\textwidth}
    \centering
    \includegraphics[width=\textwidth]{figure/aug_orig.jpg}
    \caption{Asli}
    \label{fig:aug_orig}
  \end{subfigure}
  \hfill
  \begin{subfigure}[b]{0.22\textwidth}
    \centering
    \includegraphics[width=\textwidth]{figure/aug_inv.jpg}
    \caption{Inversi warna}
    \label{fig:aug_inv}
  \end{subfigure}
  \hfill
  \begin{subfigure}[b]{0.22\textwidth}
    \centering
    \includegraphics[width=\textwidth]{figure/aug_mult.jpg}
    \caption{Penguatan kecerahan}
    \label{fig:aug_mult}
  \end{subfigure}
  \hfill
  \begin{subfigure}[b]{0.22\textwidth}
    \centering
    \includegraphics[width=\textwidth]{figure/aug_down.jpg}
    \caption{Resolusi rendah}
    \label{fig:aug_down}
  \end{subfigure}
  \end{minipage}}}
  \caption{Contoh \textit{frame} hasil augmentasi pada klip ``Aku'' (video ke-90, \textit{frame} ke-39)}
  \label{fig:aug_contoh}
\end{figure}"""

if bad_fig1 in text:
    text = text.replace(bad_fig1, good_fig1)
else:
    print("Warning: Figure 4.1 not matched precisely!")

# Fix mixup
bad_mixup = r"""\begin{figure}[H]
\centering
\begin{subfigure}[t]{0.47\textwidth}
  \centering
  \includegraphics[width=\linewidth]{figure/aug_mixup_asli.png}
  \caption{Asli: gestur \textit{Aku}}
\end{subfigure}
\hfill
\begin{subfigure}[t]{0.47\textwidth}
  \centering
  \includegraphics[width=\linewidth]{figure/aug_mixup_hasil.png}
  \caption{\textit{Mixup} ($\lambda{=}0.5$): perpaduan piksel \textit{Aku} + \textit{Bapak}}
\end{subfigure}
\end{minipage}}}

\caption{Ilustrasi efek augmentasi \textit{Mixup} pada frame gestur SIBI}
\label{fig:4.aug_mixup}
\end{figure}"""

good_mixup = r"""\begin{figure}[H]
\centering
\makebox[\linewidth][c]{\fbox{\begin{minipage}{0.97\linewidth}
\begin{subfigure}[t]{0.47\textwidth}
  \centering
  \includegraphics[width=\linewidth]{figure/aug_mixup_asli.png}
  \caption{Asli: gestur \textit{Aku}}
\end{subfigure}
\hfill
\begin{subfigure}[t]{0.47\textwidth}
  \centering
  \includegraphics[width=\linewidth]{figure/aug_mixup_hasil.png}
  \caption{\textit{Mixup} ($\lambda{=}0.5$): perpaduan piksel \textit{Aku} + \textit{Bapak}}
\end{subfigure}
\end{minipage}}}

\caption{Ilustrasi efek augmentasi \textit{Mixup} pada frame gestur SIBI}
\label{fig:4.aug_mixup}
\end{figure}"""

if bad_mixup in text:
    text = text.replace(bad_mixup, good_mixup)
else:
    print("Warning: mixup not matched precisely!")

# Fix cutmix
bad_cutmix = r"""\begin{figure}[H]
\centering
\begin{subfigure}[t]{0.47\textwidth}
  \centering
  \includegraphics[width=\linewidth]{figure/aug_cutmix_asli.png}
  \caption{Asli: gestur \textit{Aku}}
\end{subfigure}
\hfill
\begin{subfigure}[t]{0.47\textwidth}
  \centering
  \includegraphics[width=\linewidth]{figure/aug_cutmix_hasil.png}
  \caption{\textit{CutMix} ($\lambda{=}0.5$): region dari \textit{Bapak} ditempel ke \textit{Aku}}
\end{subfigure}
\end{minipage}}}

\caption{Ilustrasi efek augmentasi \textit{CutMix} pada frame gestur SIBI}
\label{fig:4.aug_cutmix}
\end{figure}"""

good_cutmix = r"""\begin{figure}[H]
\centering
\makebox[\linewidth][c]{\fbox{\begin{minipage}{0.97\linewidth}
\begin{subfigure}[t]{0.47\textwidth}
  \centering
  \includegraphics[width=\linewidth]{figure/aug_cutmix_asli.png}
  \caption{Asli: gestur \textit{Aku}}
\end{subfigure}
\hfill
\begin{subfigure}[t]{0.47\textwidth}
  \centering
  \includegraphics[width=\linewidth]{figure/aug_cutmix_hasil.png}
  \caption{\textit{CutMix} ($\lambda{=}0.5$): region dari \textit{Bapak} ditempel ke \textit{Aku}}
\end{subfigure}
\end{minipage}}}

\caption{Ilustrasi efek augmentasi \textit{CutMix} pada frame gestur SIBI}
\label{fig:4.aug_cutmix}
\end{figure}"""

if bad_cutmix in text:
    text = text.replace(bad_cutmix, good_cutmix)
else:
    print("Warning: cutmix not matched precisely!")

# Fix reprob
bad_reprob = r"""\begin{figure}[H]
\centering
\begin{subfigure}[t]{0.47\textwidth}
  \centering
  \includegraphics[width=\linewidth]{figure/aug_erase_asli.png}
  \caption{Asli: gestur \textit{Aku}}
\end{subfigure}
\hfill
\begin{subfigure}[t]{0.47\textwidth}
  \centering
  \includegraphics[width=\linewidth]{figure/aug_erase_hasil.png}
  \caption{\textit{Random Erasing}: area tangan digantikan \textit{noise} piksel acak}
\end{subfigure}
\end{minipage}}}

\caption{Ilustrasi efek augmentasi \textit{Random Erasing} pada frame gestur SIBI}
\label{fig:4.aug_reprob}
\end{figure}"""

good_reprob = r"""\begin{figure}[H]
\centering
\makebox[\linewidth][c]{\fbox{\begin{minipage}{0.97\linewidth}
\begin{subfigure}[t]{0.47\textwidth}
  \centering
  \includegraphics[width=\linewidth]{figure/aug_erase_asli.png}
  \caption{Asli: gestur \textit{Aku}}
\end{subfigure}
\hfill
\begin{subfigure}[t]{0.47\textwidth}
  \centering
  \includegraphics[width=\linewidth]{figure/aug_erase_hasil.png}
  \caption{\textit{Random Erasing}: area tangan digantikan \textit{noise} piksel acak}
\end{subfigure}
\end{minipage}}}

\caption{Ilustrasi efek augmentasi \textit{Random Erasing} pada frame gestur SIBI}
\label{fig:4.aug_reprob}
\end{figure}"""

if bad_reprob in text:
    text = text.replace(bad_reprob, good_reprob)
else:
    print("Warning: reprob not matched precisely!")


with open('chapters/chapter-4.tex', 'w', encoding='utf-8') as f:
    f.write(text)
print("Fixes applied.")
