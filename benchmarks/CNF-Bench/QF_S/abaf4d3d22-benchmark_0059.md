(⟦(= y1 (str.replace_all y "u" "A"))⟧) ∧
(⟦(= y2 (str.replace_all y1 "a" "T"))⟧) ∧
(⟦(= y3 (str.replace_all y2 "g" "C"))⟧) ∧
(⟦(= x (str.replace_all y3 "c" "G"))⟧) ∧
(⟦(= x "CCCGTTCTCTCTTGGTTAATACCCAAACTCGCGCCGACGTAGAGCCCCGCTAGGGGGGCCACCATTCTGATCGATTGGGCTCGCGTGTGTGCTAAACCCAGTAGTTGACCCTATTTGCTGTGTATGCGTAGCTTAGGGTCGCTGTGTGTCATTCAGCAACTTCTCTGTCCCATGTCGAATATCCGCCAGGCTACCTGGGT")⟧) ∧
(⟦(= z "gucccccgcuuauua")⟧) ∧
(⟦(str.contains y z)⟧)
