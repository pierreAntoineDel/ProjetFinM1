from sorting import tri, index_generator
from dataManagement import lire, ecrire, transformer_matrice2
import time

# ces r et s sont pour les tests
r = [[[1, 2], [4, 5]], [[9, 3], [6, 4]], [[8, 7], [10, 9]], [[5, 11], [2, 15]], [[14, 8], [13, 10]], [[11, 13], [3, 12]], [[7, 14], [12, 6]],[[7, 0], [12, 64]]]
s = [[[2,1],[4,2]],[[15,3],[1,4]],[[11,5],[7,6]],[[6,7],[5,8]],[[3,9],[12,10]],[[8,11],[13,12]],[[9,13],[10,14]],[[14,15],[16,16]],[[2,12],[4,20]]]
rhh=r
shh=s
R_100 = lire("data/input/pageR_1.txt")
S_100 = lire("data/input/pageS_1.txt")

R_50 = lire("data/input/pageR_0.5.txt")
S_50 = lire("data/input/pageS_0.5.txt")

R_20 = lire("data/input/pageR_0.2.txt")
S_20 = lire("data/input/pageS_0.2.txt")

R_5 = lire("data/input/pageR_0.05.txt")
S_5 = lire("data/input/pageS_0.05.txt")

R_1 = lire("data/input/pageR_0.01.txt")
S_1 = lire("data/input/pageS_0.01.txt")

# modifier les nom de r,s et distribution pour les tester
distribution = "1"
r = R_1
s = S_1


def ProduitCartesien(R, S, T):
    debut = time.time()
    lecturesR, lecturesS, ecrituresT = 0, 0, 0

    for i in range(len(R)):
        lecturesR += 1
        for j in range(len(S)):
            it = 0
            while it <= 1:
                if R[i][0][1] == S[j][0+it][0]:
                    T.append([R[i][0][0], R[i][0][1], S[j][0+it][0], S[j][0+it][1]])
                    ecrituresT += 0.5
                if R[i][1][1] == S[j][0+it][0]:
                    T.append([R[i][1][0], R[i][1][1], S[j][0+it][0], S[j][0+it][1]])
                    ecrituresT += 0.5
                it += 1
            lecturesS += 1
    RST = int(ecrituresT+0.5)+lecturesS+lecturesR
    fin = time.time()
    temps_execution = fin - debut
    return T, RST,temps_execution


t,RST, temps_execution=ProduitCartesien(r, s, [])
"""
for i in range(len(t)):
    print(t[i])
    """
t=transformer_matrice2(t)
ecrire(t,"data/output/T.[Produit Cartesien]"+distribution+".txt")
print("[Produit Cartesien] Lectures/Ecritures disques:",RST)
print("[Produit Cartesien] Temps d'exécution:", temps_execution, "secondes")


def TriFusion(R, S, T):
    debut = time.time()
    R = tri(R,1)
    S = tri(S,0)
    idR1, idR2, idS1, idS2, lecturesR, lecturesS, ecrituresT = 0, 0, 0, 0, 0, 0, 0
    while idR1 < len(R) and idS1 < len(S):
        if R[idR1][idR2][1] == S[idS1][idS2][0]:
                while idS1<len(S) and R[idR1][idR2][1] == S[idS1][idS2][0] :
                    T.append([R[idR1][idR2][0], R[idR1][idR2][1], S[idS1][idS2][0], S[idS1][idS2][1]])
                    ecrituresT += 0.5
                    if idS2 == 1:
                        idS1 = idS1 + 1
                        idS2 = 0
                        lecturesS += 1
                    else:
                        idS2 = idS2 + 1
                if idR2 == 1:
                    idR1 = idR1+1
                    idR2 = 0
                    lecturesR += 1
                else:
                    idR2 = idR2+1
        elif R[idR1][idR2][1] < S[idS1][idS2][0]:
            if idR2 == 1:
                idR1 = idR1 + 1
                idR2 = 0
                lecturesR += 1
            else:
                idR2 = idR2 + 1
        else:
            if idS2 == 1:
                idS1 = idS1+1
                idS2 = 0
                lecturesS += 1
            else:
                idS2 = idS2+1
    RST = int(ecrituresT+0.5)+lecturesS+lecturesR
    fin = time.time()
    temps_execution = fin - debut
    return T, RST,temps_execution


t, RST, temps_execution = TriFusion(r, s, [])
"""
for i in range(len(t)):
    print(t[i])
    """
t=transformer_matrice2(t)
ecrire(t,"data/output/T.[Tri-Fusion]"+distribution+".txt")
print("[Tri-Fusion] Lectures/Ecritures disques:",RST)
print("[Tri-Fusion] Temps d'exécution:", temps_execution, "secondes")


def HachageSimple(R, S, T, modulo):
    debut = time.time()
    preHachage = []
    Hachage = []
    lecturesR, lecturesS, ecrituresT = 0, 0, 0

    for i in range(modulo):
        preHachage.append([])
        Hachage.append([])

    # Phase 1: Build
    for i in range(len(R)):
        preHachage[R[i][0][1] % modulo].append(R[i][0])
        preHachage[R[i][1][1] % modulo].append(R[i][1])
        lecturesR += 1
    for i in range(modulo):
        for j in range(0, len(preHachage[i])-1, 2):
            Hachage[i].append([preHachage[i][j], preHachage[i][j+1]])
        if (len(preHachage[i])-1) % 2 == 0:
            Hachage[i].append([preHachage[i][len(preHachage[i])-1]])

    # Phase 2: Probe
    for i in range(len(S)):
        it = 0
        lecturesS += 1
        while it <= 1:
            res_mod = S[i][0+it][0] % modulo
            for j in range(len(Hachage[res_mod])):
                for l in range(len(Hachage[res_mod][j])):
                    if S[i][0 + it][0] == Hachage[res_mod][j][l][1]:
                        T.append([Hachage[res_mod][j][l], S[i][0+it]])
                        ecrituresT += 0.5
            it = it+1
    RST = int(ecrituresT+0.5)+lecturesS+lecturesR
    fin = time.time()
    temps_execution = fin - debut
    return T, RST, temps_execution


t, RST,temps_execution = HachageSimple(r, s, [], 3)
"""
for i in range(len(t)):
    print(t[i])
    """
t=transformer_matrice2(t)
ecrire(t,"data/output/T.[Hachage Simple]"+distribution+".txt")
print("[Hachage Simple] Lectures/Ecritures disques:",RST)
print("[Hachage Simple] Temps d'exécution:", temps_execution, "secondes")


"______________________________________________________________________________________________________"


def ProduitCartesienIndexe(R, S, T):
    index = index_generator(S, 0)
    debut = time.time()
    lecturesR, ecrituresT = 0, 0
    lecturesS = len(S)
    for i in range(len(R)):
        lecturesR += 1
        for j in range(len(index)):
            if R[i][0][1] == index[j][0]:
                T.append([R[i][0][0], R[i][0][1], index[j][0], S[index[j][1]][index[j][2]][1]])
                ecrituresT += 0.5
            if R[i][1][1] == index[j][0]:
                T.append([R[i][1][0], R[i][1][1], index[j][0], S[index[j][1]][index[j][2]][1]])
                ecrituresT += 0.5
    RST = int(ecrituresT+0.5)+lecturesS+lecturesR
    fin = time.time()
    temps_execution = fin - debut
    return T, RST, temps_execution


t, RST, temps_execution = ProduitCartesienIndexe(r, s, [])
"""
for i in range(len(t)):
    print(t[i])
    """
t=transformer_matrice2(t)
ecrire(t,"data/output/T.[Produit Cartesien Indexe]"+distribution+".txt")
print("[Produit Cartesien Indexe] Lectures/Ecritures disques:",RST)
print("[Produit Cartesien Indexe] Temps d'exécution:", temps_execution, "secondes")


def HachageHybride(R, S, T, modulo, M, F):
    debut = time.time()
    preHachage, Hachage, Ri , Si = [], [], [], []
    lecturesR, lecturesS, ecrituresT = 0, 0, 0

    if len(R)*F > len(M):
        ## I.
        B = int((len(R)*F-len(M))/len(M)-1)
        D = [[] for _ in range(B+1)]

        for i in range(B):
            Ri.append([])
        for i in range(len(R)):
            if len(Ri[0]) < len(R)-(len(M)-B):
                Ri[0].append(R[i])
            elif len(Ri[1]) < int((len(R)-(len(M)-B))/(B-1)):
                Ri[1].append(R[i])
            elif len(Ri[2]) < int((len(R)-(len(M)-B))/(B-1)):
                Ri[2].append(R[i])
        ## II.
        for i in range(len(R)):
            lecturesR += 1
            for k in range(len(Ri)):
                for l in range(len(Ri[k])):
                    if R[i][0][1] == Ri[k][l][0][1] or R[i][0][1] == Ri[k][l][1][1]:
                        if k == 0:
                            M[(R[i][0][1] % modulo)].append([R[i][0][0], R[i][0][1]])
                        else:
                            D[k-1].append([R[i][0][0],R[i][0][1]])
                    if R[i][1][1] == Ri[k][l][0][1] or R[i][1][1] == Ri[k][l][1][1]:
                        if k == 0:
                            M[(R[i][1][1] % modulo)].append([R[i][1][0], R[i][1][1]])
                        else:
                            D[k-1].append([R[i][1][0],R[i][1][1]])
        ## III.
        for i in range(B):
            Si.append([])
        for i in range(len(S)):
            if len(Si[0]) < len(S)-(len(M)-B):
                Si[0].append(S[i])
            elif len(Si[1]) < int((len(S)-(len(M)-B))/(B-1)):
                Si[1].append(S[i])
            elif len(Si[2]) < int((len(S)-(len(M)-B))/(B-1)):
                Si[2].append(S[i])

        for i in range(len(S)):
            lecturesS += 1
            for k in range(len(Si)):
                for l in range(len(Si[k])):
                    if S[i][1][0] == Si[k][l][1][0] and S[i][1][1] == Si[k][l][1][1]:
                        if k == 0:
                            for n in range(2):
                                for m in range(len(M[(S[i][n][0] % modulo)])):
                                    if S[i][n][0] == M[(S[i][n][0] % modulo)][m][1]:
                                        T.append([M[(S[i][n][0] % modulo)][m][0], M[(S[i][n][0] % modulo)][m][1], S[i][n][0],S[i][n][1]])
                                        ecrituresT += 0.5
                        else:
                            D[k+1].append([S[i][0][0], S[i][0][1]])
                            D[k+1].append([S[i][1][0], S[i][1][1]])

        ecrire(D, "data/output/D.[Hachage Hybride]" + distribution + ".txt")
        disque = lire("data/output/D.[Hachage Hybride]1.txt")

        #IV & V
        for i in range(1, B):
            for j in range(len(Ri[i])):
                for k in range(2):
                    M[(Ri[i][j][k][1] % modulo)].append([Ri[i][j][k][0], Ri[i][j][k][1]])
            for j in range(len(Si[i])):
                for k in range(2):
                    for m in range(len(M[(Si[i][j][k][0] % modulo)])):
                        if Si[i][j][k][0] == M[(Si[i][j][k][0] % modulo)][m][1]:
                            T.append([M[(Si[i][j][k][0] % modulo)][m][0], M[(Si[i][j][k][0] % modulo)][m][1], Si[i][j][k][0],Si[i][j][k][1]])
                            ecrituresT += 0.5
        """
        for i in range(len(M)):
            print("M:", M[i], i)
        for i in range(len(D)):
            print("D:", D[i], i)
        """
    else:
        for i in range(modulo):
            preHachage.append([])
            Hachage.append([])

        # Phase 1: Build
        for i in range(len(R)):
            preHachage[R[i][0][1] % modulo].append(R[i][0])
            preHachage[R[i][1][1] % modulo].append(R[i][1])
            lecturesR += 1
        for i in range(modulo):
            for j in range(0, len(preHachage[i]) - 1, 2):
                Hachage[i].append([preHachage[i][j], preHachage[i][j + 1]])
            if (len(preHachage[i]) - 1) % 2 == 0:
                Hachage[i].append([preHachage[i][len(preHachage[i]) - 1]])

        # Phase 2: Probe
        for i in range(len(S)):
            it = 0
            lecturesS += 1
            while it <= 1:
                res_mod = S[i][0 + it][0] % modulo
                for j in range(len(Hachage[res_mod])):
                    for l in range(len(Hachage[res_mod][j])):
                        if S[i][0 + it][0] == Hachage[res_mod][j][l][1]:
                            T.append([Hachage[res_mod][j][l], S[i][0 + it]])
                            ecrituresT += 0.5
                it = it + 1

    RST = int(ecrituresT+0.5)+lecturesS+lecturesR
    fin = time.time()
    temps_execution = fin - debut
    return T, RST, temps_execution


m = [[],[],[],[],[],[],[]]
t,RST, temps_execution = HachageHybride(rhh, shh, [], 3, m, 5)
for i in range(len(t)):
    print(t[i])
print("[Hachage Indexe] Lectures/Ecritures disques:",RST) 
print("[Hachage Hybride] Temps d'exécution:", temps_execution, "secondes")
