# Input:  A DNA string Pattern
# Output: The complementary string of Pattern (with every nucleotide replaced by its complement).
def Complement(Pattern):
    comp=''
    for c in Pattern:
        if c == "A":
            comp=comp+"T"
        elif c == "T":
            comp=comp+"A"
        elif c == "G":
            comp=comp+"C"
        elif c == "C":
            comp=comp+"G"
    return comp
           
        