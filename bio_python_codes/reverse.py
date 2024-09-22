# Input:  A string Pattern
# Output: The reverse of Pattern
def Reverse(Pattern):
    # your code here
    z=''
    for c in Pattern:
        z=c+z
    return z
