def Consensus(Motifs):
    consensus=""
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
    
    for i in range(t):
        m=0
        symbol=""
        for j in "ACTG":
            if count[j][i]>m:
                m=count[j][i]
                symbol=j
        consensus+=symbol

   
    return consensus