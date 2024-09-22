# Input:  A DNA string Pattern
# Output: The reverse complement of Pattern
def ReverseComplement(Pattern):   
    
    comp=''
    for c in Pattern:
        if c == "A":
            comp="T"+comp
        elif c == "T":
            comp="A"+comp
        elif c == "G":
            comp="C"+comp
        elif c == "C":
            comp="G"+comp
    return comp


def Reverse(Pattern):
    rev=''
    for c in Pattern:
        rev=c+rev
    

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
    