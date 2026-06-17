#!/usr/bin/env python3
"""
Fix remaining issues:
1. Table 4.7 (s1_perkelas): make P,R,F1 equal width using p{0.65cm} columns
2. Table 4.14 (s4_config): make E5 and E10 columns equal width
3. Table 4.16 (s4_perkelas): remove resizebox, use p{0.85cm} for P,R,F1 equal width
"""

with open('chapters/chapter-4.tex', 'rb') as f:
    raw = f.read()
text = raw.decode('utf-8')

# Normalize line endings
text = text.replace('\r\n', '\n').replace('\r', '\n')

# -------------------------------------------------------------------------
# Fix 1: Table 4.7 - change column spec so P,R,F1 are equal width
# Use p{0.6cm} for all 12 number columns inside resizebox
# -------------------------------------------------------------------------
old_47_spec = '\\begin{tabular}{|l|r|r|r|r|r|r|r|r|r|r|r|r|}\n'
new_47_spec = '\\begin{tabular}{|l|>{\\centering\\arraybackslash}p{0.6cm}|>{\\centering\\arraybackslash}p{0.6cm}|>{\\centering\\arraybackslash}p{0.6cm}|>{\\centering\\arraybackslash}p{0.6cm}|>{\\centering\\arraybackslash}p{0.6cm}|>{\\centering\\arraybackslash}p{0.6cm}|>{\\centering\\arraybackslash}p{0.6cm}|>{\\centering\\arraybackslash}p{0.6cm}|>{\\centering\\arraybackslash}p{0.6cm}|>{\\centering\\arraybackslash}p{0.6cm}|>{\\centering\\arraybackslash}p{0.6cm}|>{\\centering\\arraybackslash}p{0.6cm}|}\n'

if old_47_spec in text:
    text = text.replace(old_47_spec, new_47_spec, 1)
    print("Fixed table 4.7 column spec (equal P,R,F1 width)")
else:
    print("WARNING: table 4.7 spec not found!")
    # Try alternative search
    idx = text.find('s1_perkelas')
    print(f"  s1_perkelas found at index: {idx}")
    if idx > 0:
        print(f"  Context: {text[idx:idx+300]}")

# -------------------------------------------------------------------------
# Fix 2: Table 4.14 (s4_config) - equal width for E5 and E10 columns
# Add \hspace to make columns visually equal - simpler: use p{2.5cm} cols
# -------------------------------------------------------------------------
old_414_spec = '\\begin{tabular}{|l|l|l|}\n\\hline\n\\rowcolor{gray!15} \\multicolumn{1}{|c|}{\\textbf{Parameter}} & \\multicolumn{1}{c|}{\\textbf{E5}} & \\multicolumn{1}{c|}{\\textbf{E10}}'
new_414_spec = '\\begin{tabular}{|l|p{2.8cm}|p{2.8cm}|}\n\\hline\n\\rowcolor{gray!15} \\multicolumn{1}{|c|}{\\textbf{Parameter}} & \\multicolumn{1}{c|}{\\textbf{E5}} & \\multicolumn{1}{c|}{\\textbf{E10}}'

if old_414_spec in text:
    text = text.replace(old_414_spec, new_414_spec)
    print("Fixed table 4.14 equal column width")
else:
    print("WARNING: table 4.14 spec not found!")

# -------------------------------------------------------------------------
# Fix 3: Table 4.16 (s4_perkelas) - REMOVE resizebox, use p{} cols for equal P,R,F1
# -------------------------------------------------------------------------

# Remove resizebox opening
old_416_open = (
    '{\\setlength{\\tabcolsep}{3pt}\n'
    '\\footnotesize\n'
    '\\resizebox{\\linewidth}{!}{%\n'
    '\\begin{tabular}{|l|r|r|r|r|r|r|}\n'
)
new_416_open = (
    '{\\setlength{\\tabcolsep}{3pt}\n'
    '\\footnotesize\n'
    '\\begin{tabular}{|l|>{\\centering\\arraybackslash}p{0.9cm}|>{\\centering\\arraybackslash}p{0.9cm}|>{\\centering\\arraybackslash}p{0.9cm}|>{\\centering\\arraybackslash}p{0.9cm}|>{\\centering\\arraybackslash}p{0.9cm}|>{\\centering\\arraybackslash}p{0.9cm}|}\n'
)

if old_416_open in text:
    text = text.replace(old_416_open, new_416_open)
    print("Fixed table 4.16 open (removed resizebox, equal p{} cols)")
else:
    print("WARNING: table 4.16 open not found!")

# Remove resizebox closing (the extra } before \end{table})
old_416_close = (
    '\\end{tabular}%\n'
    '}\n'
    '}\n'
    '\\end{table}'
)
new_416_close = (
    '\\end{tabular}\n'
    '}\n'
    '\\end{table}'
)

# Count occurrences to be careful
count = text.count(old_416_close)
if count == 1:
    text = text.replace(old_416_close, new_416_close)
    print("Fixed table 4.16 close (removed extra resizebox brace)")
elif count > 1:
    print(f"WARNING: table 4.16 close found {count} times - being careful")
    # Only replace near the s4_perkelas label
    idx = text.find('s4_perkelas')
    if idx > 0:
        # Find the close after it
        close_idx = text.find(old_416_close, idx)
        if close_idx > 0:
            text = text[:close_idx] + new_416_close + text[close_idx + len(old_416_close):]
            print(f"  Fixed table 4.16 close at index {close_idx}")
else:
    print("WARNING: table 4.16 close not found!")

# Normalize back to \r\n
text = text.replace('\n', '\r\n')

with open('chapters/chapter-4.tex', 'w', encoding='utf-8', newline='') as f:
    f.write(text)

print("\nDone!")
