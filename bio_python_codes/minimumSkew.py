# Input:  A DNA string Genome
# Output: A list containing all integers i minimizing Skew(Prefix_i(Text)) over all values of i (from 0 to |Genome|)
def MinimumSkew(Genome):
    positions = [] # output variable
    skew = SkewArray(Genome)
    m=min(skew)
    for i in range(len(skew)):
        if m==skew[i]:
            positions.append(i)
    
    return positions

# Input:  A String Genome
# Output: SkewArray(Genome)
# HINT:   This code should be taken from the last Code Challenge.
def SkewArray(Genome):
    skew = [0] # output variable
    n=len(Genome)
    for i in range(n):
        if Genome[i]=='G':
            skew.append(skew[i]+1)
        elif Genome[i]=='C':
            skew.append(skew[i]-1)
        else:
            skew.append(skew[i])
    return skew