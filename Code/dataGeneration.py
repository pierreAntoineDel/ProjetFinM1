import random
from dataManagement import ecrire


def block(rel):
    res = []
    for i in range(0,len(rel)-1, 2):
        res.append([rel[i], rel[i+1]])
    return res


def generation_donnees(taille, pourcentage, multiple):
    tailleS = taille * multiple
    taille = taille*2
    list_numbersS = []
    R = []
    S = []
    list_numbers = []
    nb = 0
    double = 0
    while len(list_numbers) < taille:
        number = random.randint(1, taille)
        if not(number in list_numbers):
            list_numbers.append(number)
            list_numbersS.append(number+taille)
    while len(list_numbers) > 0:
        i = random.randint(0, len(list_numbers)-2)
        if nb < ((taille/2)*pourcentage):
            R.append([list_numbers[i], list_numbers[i+1]])
            S.append([list_numbers[i+1], list_numbers[i]])
            nb += 1
            if double == 0 and nb < ((taille/2)*pourcentage):
                S.append([list_numbers[i + 1], list_numbers[i + 1]])
                double += 1
                nb += 1
            else:
                double = 0
            list_numbers.remove(list_numbers[i])
            list_numbers.remove(list_numbers[i])
        else:
            R.append([list_numbers[i], list_numbers[i+1]])
            if len(S) < taille/2:
                S.append([list_numbers[i], list_numbers[i+1]])
            list_numbers.remove(list_numbers[i])
            list_numbers.remove(list_numbers[i])
    i = 0
    while len(R) <= tailleS:
        R.append([list_numbersS[i]-1, list_numbersS[i + 1] - 1])
        i += 1
    R = block(R)
    S = block(S)
    return R, S

# Pourcentage par rapport à S (si 50% alors la moitié des données de S à une correspondance)


# a executer qu une fois pour obtenir les donnees
distributions = [0.01, 0.05, 0.2, 0.5, 1]
for i in range(len(distributions)):
    R, S = generation_donnees(100,distributions[i],1.4)
    ecrire(R, "data/input/pageR_"+str(distributions[i])+".txt")
    ecrire(S, "data/input/pageS_" + str(distributions[i]) + ".txt")
