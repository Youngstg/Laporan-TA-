import re

with open('chapters/chapter-4.tex', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Tabel 4.8 (tab:4.s2_config)
# Replace \begin{tabular}{|l|c|c|c|} with |l|r|r|r|
text = text.replace(r'\begin{tabular}{|l|c|c|c|}', r'\begin{tabular}{|l|r|r|r|}')
text = text.replace(r'\multicolumn{1}{|l|}{\textbf{Parameter}} & \multicolumn{1}{c|}{\textbf{E5}} & \multicolumn{1}{c|}{\textbf{E6}} & \multicolumn{1}{c|}{\textbf{E7}} \\',
                    r'\rowcolor{gray!15} \multicolumn{1}{|l|}{\textbf{Parameter}} & \multicolumn{1}{c|}{\textbf{E5}} & \multicolumn{1}{c|}{\textbf{E6}} & \multicolumn{1}{c|}{\textbf{E7}} \\')
# Change \multicolumn{3}{c|}{50} to r|
text = text.replace(r'\textit{Epoch Stage} 2 & \multicolumn{3}{c|}{50} \\', r'\textit{Epoch Stage} 2 & \multicolumn{3}{r|}{50} \\')
text = text.replace(r'\textit{Batch Size} & \multicolumn{3}{c|}{16} \\', r'\textit{Batch Size} & \multicolumn{3}{r|}{16} \\')
# Strategi Pelatihan cells (makecell[c] to makecell[l])
text = text.replace(r'Strategi Pelatihan & \makecell[c]{\textit{Two-Stage}\\\textit{Pre-train}} & \makecell[c]{\textit{Two-Stage}\\\textit{Scratch}} & \makecell[c]{\textit{Single-Stage}\\\textit{Scratch}} \\',
                    r'Strategi Pelatihan & \makecell[l]{\textit{Two-Stage}\\\textit{Pre-train}} & \makecell[l]{\textit{Two-Stage}\\\textit{Scratch}} & \makecell[l]{\textit{Single-Stage}\\\textit{Scratch}} \\')
text = text.replace(r'\textit{Hyperparameter} Lain & \multicolumn{3}{c|}{Sama dengan Tabel~\ref{tab:4.umum_config}} \\',
                    r'\textit{Hyperparameter} Lain & \multicolumn{3}{c|}{Sama dengan Tabel~\ref{tab:4.umum_config}} \\') # Already c|

# 2. Tabel 4.11 (tab:4.s3_config)
text = text.replace(r'\multicolumn{1}{|l|}{\textbf{Parameter}} & \makecell[c]{\hspace{0.8cm}\textbf{E8}\hspace{0.8cm}} & \makecell[c]{\hspace{0.8cm}\textbf{E5}\hspace{0.8cm}} & \makecell[c]{\hspace{0.8cm}\textbf{E9}\hspace{0.8cm}} \\',
                    r'\rowcolor{gray!15} \multicolumn{1}{|l|}{\textbf{Parameter}} & \makecell[c]{\hspace{0.8cm}\textbf{E8}\hspace{0.8cm}} & \makecell[c]{\hspace{0.8cm}\textbf{E5}\hspace{0.8cm}} & \makecell[c]{\hspace{0.8cm}\textbf{E9}\hspace{0.8cm}} \\')
text = text.replace(r'Strategi Pelatihan & \multicolumn{3}{c|}{\textit{Two-Stage Pre-train}} \\',
                    r'Strategi Pelatihan & \multicolumn{3}{l|}{\textit{Two-Stage Pre-train}} \\')
text = text.replace(r'Inisialisasi & \multicolumn{3}{c|}{Bobot SSV2} \\',
                    r'Inisialisasi & \multicolumn{3}{l|}{Bobot SSV2} \\')
text = text.replace(r'\textit{Epoch Stage} 1 & \multicolumn{3}{c|}{5} \\',
                    r'\textit{Epoch Stage} 1 & \multicolumn{3}{r|}{5} \\')
text = text.replace(r'\textit{Learning Rate Stage} 1 & \multicolumn{3}{c|}{$10^{-3}$} \\',
                    r'\textit{Learning Rate Stage} 1 & \multicolumn{3}{l|}{$10^{-3}$} \\')
text = text.replace(r'\textit{Learning Rate Stage} 2 & \multicolumn{3}{c|}{$10^{-5}$} \\',
                    r'\textit{Learning Rate Stage} 2 & \multicolumn{3}{l|}{$10^{-5}$} \\')
text = text.replace(r'\textit{Batch Size} & \multicolumn{3}{c|}{16} \\',
                    r'\textit{Batch Size} & \multicolumn{3}{r|}{16} \\')

# 3. Tabel 4.14 (tab:4.s4_config)
text = text.replace(r'\begin{tabular}{|l|c|c|}', r'\begin{tabular}{|l|r|r|}')
text = text.replace(r'\multicolumn{1}{|l|}{\textbf{Parameter}} & \multicolumn{1}{c|}{\textbf{E5}} & \multicolumn{1}{c|}{\textbf{E10}} \\',
                    r'\rowcolor{gray!15} \multicolumn{1}{|l|}{\textbf{Parameter}} & \multicolumn{1}{c|}{\textbf{E5}} & \multicolumn{1}{c|}{\textbf{E10}} \\')
text = text.replace(r'Strategi \textit{Sampling} & \textit{Uniform} & \textit{Dense} \\',
                    r'Strategi \textit{Sampling} & \multicolumn{1}{l|}{\textit{Uniform}} & \multicolumn{1}{l|}{\textit{Dense}} \\')
text = text.replace(r'\textit{Epoch Stage} 1 & \multicolumn{2}{c|}{5} \\', r'\textit{Epoch Stage} 1 & \multicolumn{2}{r|}{5} \\')
text = text.replace(r'\textit{Epoch Stage} 2 & \multicolumn{2}{c|}{50} \\', r'\textit{Epoch Stage} 2 & \multicolumn{2}{r|}{50} \\')
text = text.replace(r'Jumlah \textit{Frame} & \multicolumn{2}{c|}{16} \\', r'Jumlah \textit{Frame} & \multicolumn{2}{r|}{16} \\')
text = text.replace(r'\textit{Batch Size} & \multicolumn{2}{c|}{16} \\', r'\textit{Batch Size} & \multicolumn{2}{r|}{16} \\')
text = text.replace(r'\textit{Learning Rate} & \multicolumn{2}{c|}{$10^{-3}$} \\', r'\textit{Learning Rate} & \multicolumn{2}{l|}{$10^{-3}$} \\')

# 4. Tabel 4.17 (tab:4.s5aug_config)
text = text.replace(r'\multicolumn{1}{|l|}{\textbf{Parameter}} & \multicolumn{1}{c|}{\textbf{E5}} & \multicolumn{1}{c|}{\textbf{E11}} \\',
                    r'\rowcolor{gray!15} \multicolumn{1}{|l|}{\textbf{Parameter}} & \multicolumn{1}{c|}{\textbf{E5}} & \multicolumn{1}{c|}{\textbf{E11}} \\')
text = text.replace(r'\textit{Backbone} & \multicolumn{2}{c|}{ViT-Small} \\', r'\textit{Backbone} & \multicolumn{2}{l|}{ViT-Small} \\')
text = text.replace(r'Dataset \textit{Pre-train} & \multicolumn{2}{c|}{SSV2} \\', r'Dataset \textit{Pre-train} & \multicolumn{2}{l|}{SSV2} \\')
text = text.replace(r'Strategi \textit{Sampling} & \multicolumn{2}{c|}{\textit{Uniform}} \\', r'Strategi \textit{Sampling} & \multicolumn{2}{l|}{\textit{Uniform}} \\')
text = text.replace(r'\makecell[l]{Augmentasi\\(\textit{Mixup, CutMix, Reprob})} & Aktif & Dinonaktifkan \\',
                    r'\makecell[l]{Augmentasi\\(\textit{Mixup, CutMix, Reprob})} & \multicolumn{1}{l|}{Aktif} & \multicolumn{1}{l|}{Dinonaktifkan} \\')
text = text.replace(r'\textit{Epoch} (\textit{Stage} 1 / \textit{Stage} 2) & \multicolumn{2}{c|}{5 / 50} \\',
                    r'\textit{Epoch} (\textit{Stage} 1 / \textit{Stage} 2) & \multicolumn{2}{r|}{5 / 50} \\')

# 5. Tabel 4.19 (tab:4.s6_config)
text = text.replace(r'\multicolumn{1}{|l|}{\textbf{Parameter}} & \multicolumn{1}{c|}{\textbf{E11}} & \multicolumn{1}{c|}{\textbf{E12}} & \multicolumn{1}{c|}{\textbf{ViViT}} & \multicolumn{1}{c|}{\textbf{I3D}} \\',
                    r'\rowcolor{gray!15} \multicolumn{1}{|l|}{\textbf{Parameter}} & \multicolumn{1}{c|}{\textbf{E11}} & \multicolumn{1}{c|}{\textbf{E12}} & \multicolumn{1}{c|}{\textbf{ViViT}} & \multicolumn{1}{c|}{\textbf{I3D}} \\')
text = text.replace(r'\makecell[l]{Arsitektur\\Model} & \makecell[c]{VideoMAE\\ViT-Small} & \makecell[c]{VideoMAE\\ViT-Base} & ViViT-B/16x2 & \makecell[c]{I3D (Inflated\\3D ConvNet)} \\',
                    r'\makecell[l]{Arsitektur\\Model} & \makecell[l]{VideoMAE\\ViT-Small} & \makecell[l]{VideoMAE\\ViT-Base} & \multicolumn{1}{l|}{ViViT-B/16x2} & \makecell[l]{I3D (Inflated\\3D ConvNet)} \\')
text = text.replace(r'\makecell[l]{Dataset\\\textit{Pre-train}} & SSV2 & Kinetics-400 & Kinetics-400 & ImageNet \\',
                    r'\makecell[l]{Dataset\\\textit{Pre-train}} & \multicolumn{1}{l|}{SSV2} & \multicolumn{1}{l|}{Kinetics-400} & \multicolumn{1}{l|}{Kinetics-400} & \multicolumn{1}{l|}{ImageNet} \\')
text = text.replace(r'\makecell[l]{Strategi\\\textit{Sampling}} & \makecell[c]{\textit{Uniform}\\(SSV2 loader)} & \makecell[c]{\textit{Dense}\\(Kin. loader)} & Seragam & \makecell[c]{Seluruh video\\(RGB)} \\',
                    r'\makecell[l]{Strategi\\\textit{Sampling}} & \makecell[l]{\textit{Uniform}\\(SSV2 loader)} & \makecell[l]{\textit{Dense}\\(Kin. loader)} & \multicolumn{1}{l|}{Seragam} & \makecell[l]{Seluruh video\\(RGB)} \\')
text = text.replace(r'\makecell[l]{\textit{Epoch}\\Total} & 55 (5 + 50) & 55 (5 + 50) & 55 & 55 \\',
                    r'\makecell[l]{\textit{Epoch}\\Total} & \multicolumn{1}{r|}{55 (5 + 50)} & \multicolumn{1}{r|}{55 (5 + 50)} & \multicolumn{1}{r|}{55} & \multicolumn{1}{r|}{55} \\')
text = text.replace(r'\makecell[l]{Jumlah\\\textit{Frame}} & 16 & 16 & 32 & 64 \\',
                    r'\makecell[l]{Jumlah\\\textit{Frame}} & \multicolumn{1}{r|}{16} & \multicolumn{1}{r|}{16} & \multicolumn{1}{r|}{32} & \multicolumn{1}{r|}{64} \\')
text = text.replace(r'\makecell[l]{\textit{Learning}\\Rate} & \multicolumn{4}{c|}{$10^{-3}$} \\',
                    r'\makecell[l]{\textit{Learning}\\Rate} & \multicolumn{4}{l|}{$10^{-3}$} \\')

# 6. Tabel 4.13 (tab:4.s3_perkelas)
text = text.replace(r'\cellcolor{gray!15}\multirow{2}{*}{\textbf{Kelas}} &',
                    r'\rowcolor{gray!15}\cellcolor{gray!15}\multirow{2}{*}{\textbf{Kelas}} &')
text = text.replace(r'\multicolumn{3}{c|}{E8 (10 epoch)} &', r'\multicolumn{3}{c|}{\cellcolor{gray!15}\textbf{E8 (10 epoch)}} &')
text = text.replace(r'\multicolumn{3}{c|}{E5 (50 epoch)} &', r'\multicolumn{3}{c|}{\cellcolor{gray!15}\textbf{E5 (50 epoch)}} &')
text = text.replace(r'\multicolumn{3}{c|}{E9 (100 epoch)} \\', r'\multicolumn{3}{c|}{\cellcolor{gray!15}\textbf{E9 (100 epoch)}} \\')

# 7. Tabel 4.24 (tab:4.inferensi)
# header belumm center dan belum abu2 serta param belum rata kanan untuk kontennya
text = text.replace(r'\begin{tabular}{|l|r|c|r|}', r'\begin{tabular}{|l|r|c|r|}') # already correct, let's fix header
old_hdr_424 = r'Model & Param. & \makecell[c]{Frame\\Input} & \makecell[c]{Rata-rata\\(ms)} \\'
new_hdr_424 = r'\rowcolor{gray!15} \multicolumn{1}{|c|}{\cellcolor{gray!15}\textbf{Model}} & \multicolumn{1}{c|}{\cellcolor{gray!15}\textbf{Param.}} & \multicolumn{1}{c|}{\cellcolor{gray!15}\makecell[c]{\textbf{Frame}\\\textbf{Input}}} & \multicolumn{1}{c|}{\cellcolor{gray!15}\makecell[c]{\textbf{Rata-rata}\\\textbf{(ms)}}} \\'
text = text.replace(old_hdr_424, new_hdr_424)

# 8. Tabel 4.25 (tab:4.rangkuman)
text = text.replace(r'\rowcolor{gray!20} \multicolumn{1}{|c|}{Kode} & \multicolumn{1}{c|}{\makecell[c]{Kelompok\\Eksperimen}} & \multicolumn{1}{c|}{Konfigurasi} & \multicolumn{1}{c|}{\makecell[c]{Rerata $\pm$ Std\\(\%)}} & \multicolumn{1}{c|}{\makecell[c]{Acc@1\\(\%)}} \\',
                    r'\rowcolor{gray!15} \multicolumn{1}{|c|}{\cellcolor{gray!15}\textbf{Kode}} & \multicolumn{1}{>{\centering\arraybackslash}p{2.5cm}|}{\cellcolor{gray!15}\makecell[c]{\textbf{Kelompok}\\\textbf{Eksperimen}}} & \multicolumn{1}{>{\centering\arraybackslash}X|}{\cellcolor{gray!15}\textbf{Konfigurasi}} & \multicolumn{1}{>{\centering\arraybackslash}p{2.3cm}|}{\cellcolor{gray!15}\makecell[c]{\textbf{Rerata} $\pm$ \textbf{Std}\\\textbf{(\%)}}} & \multicolumn{1}{c|}{\cellcolor{gray!15}\makecell[c]{\textbf{Acc@1}\\\textbf{(\%)}}} \\')

with open('chapters/chapter-4.tex', 'w', encoding='utf-8') as f:
    f.write(text)
print("Finished updates.")
