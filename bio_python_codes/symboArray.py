# Input:  Strings Genome and symbol
# Output: SymbolArray(Genome, symbol)
def SymbolArray(Genome, symbol):
    array = {}
    n = len(Genome)
    ExtendedGenome = Genome + Genome[0:n//2]
    for i in range(n):
        array[i] = PatternCount(symbol, ExtendedGenome[i: i+(n//2)])
    return array

def PatternCount(Pattern, Text):
    # type your code here
    n = len(Text)
    k = len(Pattern)
    count = 0
    for i in range(n-k+1):
        if Text[i:i+k] == Pattern:
            count = count+1
    return count 
