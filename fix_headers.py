import re

with open('chapters/chapter-3.tex', 'r', encoding='utf-8') as f:
    text = f.read()

old1 = r'\rowcolor{gray!15} Kode & Kelompok Eksperimen & Variasi Utama \\'
new1 = r'\rowcolor{gray!15} \multicolumn{1}{|c|}{\textbf{Kode}} & \multicolumn{1}{c|}{\textbf{Kelompok Eksperimen}} & \multicolumn{1}{c|}{\textbf{Variasi Utama}} \\'

old2 = r'\rowcolor{gray!15}   No & Alat & Spesifikasi \\'
new2 = r'\rowcolor{gray!15} \multicolumn{1}{|c|}{\textbf{No}} & \multicolumn{1}{c|}{\textbf{Alat}} & \multicolumn{1}{c|}{\textbf{Spesifikasi}} \\'

text = text.replace(old1, new1)
text = text.replace(old2, new2)

with open('chapters/chapter-3.tex', 'w', encoding='utf-8') as f:
    f.write(text)

print('Headers replaced successfully.')
