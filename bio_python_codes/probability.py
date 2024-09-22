def Pr(Text, Profile):
    # insert your code here
    pro=1
    for i in range(len(Text)):
        pro=pro*Profile[Text[i]][i]
        
    return pro
