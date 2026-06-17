import re

with open('chapters/chapter-3.tex', 'r', encoding='utf-8') as f:
    text = f.read()

old_str = r'''\begin{multline*}
  \mathrm{GELU}(x) \approx \\
  0.5x\!\left(1 + \tanh\!\left(\sqrt{\tfrac{2}{\pi}}\,
  \bigl(x + 0{,}044715\,x^3\bigr)\right)\right)
\end{multline*}
 
\vspace{0.5cm}
\begin{align*}
  \text{Untuk } h_1 = 0.921: \notag \\
  0.044715 \times (0.921)^3
  &= 0.044715 \times 0.782 = 0.035 \notag \\
  \sqrt{2/\pi} \times (0.921 + 0.035)
  &= 0.7979 \times 0.956 = 0.763 \notag \\
  \tanh(0.763) &= 0.644 \notag \\
  \mathrm{GELU}(0.921)
  &= 0.5 \times 0.921 \times (1 + 0.644)
   = 0.5 \times 0.921 \times 1.644
   = \mathbf{0.757} \\[10pt]
  \text{Untuk } h_2 = -0.429: \notag \\
  0.044715 \times (-0.429)^3
  &= 0.044715 \times (-0.079) = -0.004 \notag \\
  \sqrt{2/\pi} \times (-0.429 + (-0.004))
  &= 0.7979 \times (-0.433) = -0.346 \notag \\
  \tanh(-0.346) &= -0.333 \notag \\
  \mathrm{GELU}(-0.429)
  &= 0.5 \times (-0.429) \times (1 + (-0.333))
   = 0.5 \times (-0.429) \times 0.667
   = \mathbf{-0.143}
\end{align*}'''

new_str = r'''\begin{equation*}
  \mathrm{GELU}(x) \approx 0.5x \left( 1 + \tanh \left( \sqrt{\frac{2}{\pi}} \left( x + 0.044715 x^3 \right) \right) \right)
\end{equation*}
 
\vspace{0.5cm}
\begin{align*}
  \intertext{Untuk $h_1 = 0.921$:}
  0.044715 \times (0.921)^3
  &= 0.044715 \times 0.782 = 0.035 \\
  \sqrt{2/\pi} \times (0.921 + 0.035)
  &= 0.7979 \times 0.956 = 0.763 \\
  \tanh(0.763) &= 0.644 \\
  \mathrm{GELU}(0.921)
  &= 0.5 \times 0.921 \times (1 + 0.644) \\
  &= 0.5 \times 0.921 \times 1.644 \\
  &= \mathbf{0.757} \\[10pt]
  \intertext{Untuk $h_2 = -0.429$:}
  0.044715 \times (-0.429)^3
  &= 0.044715 \times (-0.079) = -0.004 \\
  \sqrt{2/\pi} \times (-0.429 - 0.004)
  &= 0.7979 \times (-0.433) = -0.346 \\
  \tanh(-0.346) &= -0.333 \\
  \mathrm{GELU}(-0.429)
  &= 0.5 \times (-0.429) \times (1 - 0.333) \\
  &= 0.5 \times (-0.429) \times 0.667 \\
  &= \mathbf{-0.143}
\end{align*}'''

if old_str in text:
    with open('chapters/chapter-3.tex', 'w', encoding='utf-8') as f:
        f.write(text.replace(old_str, new_str))
    print('Replaced successfully!')
else:
    print('Old string not found.')
