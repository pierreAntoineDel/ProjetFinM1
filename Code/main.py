#brouillon possible projet Master

r=[[[1,2],[4,5]],[[9,3],[6,4]],[[8,7],[10,9]],[[5,11],[2,15]],[[14,8],[13,10]],[[11,13],[3,12]],[[7,14],[12,6]]]
s=[[[2,1],[4,2]],[[15,3],[1,4]],[[11,5],[7,6]],[[6,7],[5,8]],[[3,9],[12,10]],[[8,11],[13,12]],[[9,13],[10,14]],[[14,15],[16,16]]]

newR=[[[1,2],[9,3]],[[6,4],[4,5]],[[12,6],[8,7]],[[14,8],[10,9]],[[13,10],[5,11]],[[3,12],[11,13]],[[7,14],[2,15]]]
newS=[[[1,4],[2,1]],[[3,9],[4,2]],[[5,8],[6,7]],[[7,6],[8,11]],[[9,13],[10,14]],[[11,5],[12,10]],[[13,12],[14,15]],[[15,3],[16,16]]]

def ProduitCartesien(R,S,T):
    lecturesR=0
    lecturesS=0
    ecrituresT=0
    for i in range(len(R)):
        lecturesR=lecturesR+1
        for j in range(len(S)):
            if R[i][0][1]==S[j][0][0]:
                T.append([R[i][0][0],R[i][0][1],S[j][0][0],S[j][0][1]])
                ecrituresT=ecrituresT+1
            if R[i][0][1]==S[j][1][0]:
                T.append([R[i][0][0],R[i][0][1],S[j][1][0],S[j][1][1]])
                ecrituresT=ecrituresT+1
            if R[i][1][1]==S[j][0][0]:
                T.append([R[i][1][0],R[i][1][1],S[j][0][0],S[j][0][1]])
                ecrituresT=ecrituresT+1
            if R[i][1][1]==S[j][1][0]:
                T.append([R[i][1][0],R[i][1][1],S[j][1][0],S[j][1][1]])
                ecrituresT=ecrituresT+1
            lecturesS=lecturesS+1
    RST=int((ecrituresT/2)+lecturesS+lecturesR)
    return T,RST

t,RST=ProduitCartesien(r,s,[])
for i in range(len(t)):
    print(t[i])
print("Lectures/Ecritures disques:",RST)


def TriFusion(R,S,T):
    idR1=0
    idR2=0
    idS1=0
    idS2=0
    lecturesR=0
    lecturesS=0
    ecrituresT=0
    while idR1<len(R) and idR2<len(R):
        if R[idR1][idR2][1]==S[idS1][idS2][0]:
                T.append([R[idR1][idR2][0],R[idR1][idR2][1],S[idS1][idS2][0],S[idS1][idS2][1]])
                ecrituresT=ecrituresT+1
                if idR2==1:
                    idR1=idR1+1
                    idR2=0
                    lecturesR=lecturesR+1
                else:
                    idR2=idR2+1

                if idS2==1:
                    idS1=idS1+1
                    idS2=0
                    lecturesS=lecturesS+1
                else:
                    idS2=idS2+1
        else:
            if idS2==1:
                idS1=idS1+1
                idS2=0
            else:
                idS2=idS2+1
                lecturesS=lecturesS+1
    RST=int((ecrituresT/2)+lecturesR+lecturesS)
    return T,RST

t,RST=TriFusion(newR,newS,[])
for i in range(len(t)):
    print(t[i])
print("Lectures/Ecritures disques:",RST)
