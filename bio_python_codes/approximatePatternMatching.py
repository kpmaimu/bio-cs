# Input:  Strings Pattern and Text along with an integer d
# Output: A list containing all starting positions where Pattern appears
# as a substring of Text with at most d mismatches
def ApproximatePatternMatching(Text, Pattern, d):
    positions = [] # initializing list of positions
    n=len(Text)-len(Pattern)
   
    for i in range(n+1):
        
        h=0
        x=i
        k=i
        for j in range(len(Pattern)):
            if Text[k]!=Pattern[j]:
        
                h= h+1
            k=k+1
        if h<=d:
        
            positions.append(x)
    return positions