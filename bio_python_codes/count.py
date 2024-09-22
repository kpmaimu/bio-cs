def Count(Motifs):
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
    # initializing the count dictionary
    
    return count