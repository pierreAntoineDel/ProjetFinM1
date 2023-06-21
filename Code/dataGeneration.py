import random

def block(rel):
    res=[]
    for i in range(0,len(rel)-1,2):
        res.append([rel[i],rel[i+1]])
    return res

def generation_donnees(taille, pourcentage):
    taille=taille*2
    R=[]
    S=[]
    list_numbers=[]
    nb=0
    double=0
    while len(list_numbers)<taille:
        number=random.randint(1,taille)
        if not(number in list_numbers):
            list_numbers.append(number)
    while len(list_numbers)>0:
        i=random.randint(0,len(list_numbers)-2)
        if nb<((taille/2)*pourcentage):
            R.append([list_numbers[i],list_numbers[i+1]])
            S.append([list_numbers[i+1],list_numbers[i]])
            nb+=1
            if double==0 and nb<((taille/2)*pourcentage):
                S.append([list_numbers[i + 1], list_numbers[i + 1]])
                double+=1
                nb += 1
            else :
                double=0
            list_numbers.remove(list_numbers[i])
            list_numbers.remove(list_numbers[i])
        else:
            R.append([list_numbers[i],list_numbers[i+1]])
            S.append([list_numbers[i],list_numbers[i+1]])
            list_numbers.remove(list_numbers[i])
            list_numbers.remove(list_numbers[i])
    R=block(R)
    S=block(S)
    return R, S

#R,S=generation_donnees(10, 0.5)
