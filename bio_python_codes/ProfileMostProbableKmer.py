def ProfileMostProbableKmer(text, k, profile):
    max_pro=-1
    kmer=""
    for i in range(len(text)-k+1):
        
        x=text[i:i+k]
        pro=Pr(x,profile)
              
        if max_pro<pro:
            max_pro=pro
            kmer=str(x)
    return kmer
def Pr(Text, Profile):
    # insert your code here
    pro=1
    for i in range(len(Text)):
        pro=pro*Profile[Text[i]][i]
        
    return pro