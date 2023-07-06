def transformer_matrice1(matrice):
    nouvelle_matrice = []
    for sous_matrice in matrice:
        for ligne in sous_matrice:
            nouvelle_matrice.append(ligne)
    return nouvelle_matrice


def ecrire_donnees_fichier(donnees, nom_fichier):
    with open(nom_fichier, 'w') as f:
        for ligne in donnees:
            ligne_texte = ' '.join([str(element) for element in ligne])
            f.write(f"{ligne_texte}\n")


def extraire_donnees_fichier(nom_fichier):
    donnees = []
    with open(nom_fichier, 'r') as f:
        for ligne in f:
            ligne = ligne.strip()
            elements = ligne.split()
            p = []
            for i in range(len(elements)):
                p.append(int(elements[i]))
            donnees.append(p)
    return donnees


def transformer_matrice2(matrice):
    nouvelle_matrice = []
    sous_matrice = []
    for i, ligne in enumerate(matrice):
        sous_matrice.append(ligne)
        if (i + 1) % 2 == 0:
            nouvelle_matrice.append(sous_matrice)
            sous_matrice = []
    return nouvelle_matrice


def ecrire(r,fileNameR):
    newR = transformer_matrice1(r)
    ecrire_donnees_fichier(newR, fileNameR)


def lire(fileNameR):
    R = extraire_donnees_fichier(fileNameR)
    R = transformer_matrice2(R)
    return R
