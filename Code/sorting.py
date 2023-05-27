def block(rel):
    res=[]
    for i in range(0,len(rel)-1,2):
        res.append([rel[i],rel[i+1]])
    return res

def tri(R,id): #id=1=>tri de R, id=0=>tri de S
    numbers=[]
    res=[]
    for i in range(len(R)):
        for j in range(len(R[i])):
            numbers.append([R[i][j][id],i,j])
    sortt=sorted(numbers)
    for i in range(len(sortt)):
        ii=sortt[i][1]
        j=sortt[i][2]
        res.append([R[ii][j][0],R[ii][j][1]])
    return block(res)

r=[[[1,2],[4,5]],[[9,3],[6,4]],[[8,7],[10,9]],[[5,11],[2,15]],[[14,8],[13,10]],[[11,13],[3,12]],[[7,14],[12,6]]]
s=[[[2,1],[4,2]],[[15,3],[1,4]],[[11,5],[7,6]],[[6,7],[5,8]],[[3,9],[12,10]],[[8,11],[13,12]],[[9,13],[10,14]],[[14,15],[16,16]]]

#Resultat attendu
#newR=[[[1,2],[9,3]],[[6,4],[4,5]],[[12,6],[8,7]],[[14,8],[10,9]],[[13,10],[5,11]],[[3,12],[11,13]],[[7,14],[2,15]]]
#newS=[[[1,4],[2,1]],[[3,9],[4,2]],[[5,8],[6,7]],[[7,6],[8,11]],[[9,13],[10,14]],[[11,5],[12,10]],[[13,12],[14,15]],[[15,3],[16,16]]]

#print(tri(r,1))
#print(tri(s,0))

