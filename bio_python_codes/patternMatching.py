
def PatternMatching(Pattern, Genome):
    positions = [] # output variable
    
    for i in range(len(Genome)-len(Pattern)+1):
        if Genome[i:i+len(Pattern)] == Pattern:
            positions.append(i)
        
    # your code here
    return positions

# Behind the scenes, we read in Genome equal to the genome of V. cholerae.

Pattern="CTTGATCAT"
positions=PatternMatching(Pattern, Genome)
# Call PatternMatching on Pattern and Genome, and store the output as a variable called positions
print(positions)
# print the positions variable