# Input:  A list of kmers Motifs
# Output: the profile matrix of Motifs, as a dictionary of lists.
def Profile(Motifs):
    t = len(Motifs)
    k = len(Motifs[0])
    profile = {}
    count = {}
    n=len(Motifs)
    t=len(Motifs[0])
    for x in "ACTG":
        count[x]=[]
        for y in range(t):
            count[x].append(0)
    for i in range(n):
        for j in range(t):
            s=Motifs[i][j]
            count[s][j]+=1
    profile=count
    for x in "ACTG":
        for j in range(t):
            profile[x][j]=profile[x][j]/n
   
    return profile