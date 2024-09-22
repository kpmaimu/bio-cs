def HammingDistance(p, q):
    h=0
    count=0
    for i in range(len(p)):
        if p[i]!=q[i]:
            count = count+1
    return count