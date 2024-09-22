def FrequentWords(Text, k):
    words=[]
    freq=FrequencyMap(Text, k)
    m=max(freq.values())
    list=[]
    for key in freq:
        if freq[key] == m:
            list.append(key)    
        
    return list 
def FrequencyMap(Text, k):
    freq={}
    n=len(Text)
    for i in range(n-k+1):
        Pattern =Text[i:i+k]
        freq[Pattern]=0
        for j in range(n-k+1):
            if Text[j:j+k]== Pattern:
                freq[Pattern]= freq[Pattern]+1
    return freq
# Now, we will set Text equal to the oriC of Vibrio cholerae and Pattern equal to "TGATCA"
Text = "ATCAATGATCAACGTAAGCTTCTAAGCATGATCAAGGTGCTCACACAGTTTATCCACAACCTGAGTGGATGACATCAAGATAGGTCGTTGTATCTCCTTCCTCTCGTACTCTCATGACCACGGAAAGATGATCAAGAGAGGATGATTTCTTGGCCATATCGCAATGAATACTTGTGACTTGTGCTTCCAATTGACATCTTCAGCGCCATATTGCGCTGGCCAAGGTGACGGAGCGGGATTACGAAAGCATGATCATGGCTGTTGTTCTGTTTATCTTGTTTTGACTGAGACTTGTTAGGATAGACGGTTTTTCATCACTGACTAGCCAAAGCCTTACTCTGCCTGACATCGACCGTAAATTGATAATGAATTTACATGCTTCCGCGACGATTTACCTCTTGATCATCGATCCGATTGAAGATCTTCAATTGTTAATTCTCTTGCCTCGACTCATAGCCATGATGAGCTCTTGATCATGTTTCCTTAACCCTCTATTTTTTACGGAAGAATGATCAAGCTGCTGCTCTTGATCATCGTTTC"
k = 10

# Finally, let's print the result of calling FrequentWords on Text and Pattern.
print(FrequentWords(Text, k))