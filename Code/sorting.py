def block(rel):
    res = []
    for i in range(0, len(rel)-1, 2):
        res.append([rel[i], rel[i+1]])
    return res


def tri(R, id):  # id=1=>tri de R, id=0=>tri de S
    numbers = []
    res = []
    for i in range(len(R)):
        for j in range(len(R[i])):
            numbers.append([R[i][j][id], i, j])
    sortt = sorted(numbers)
    for i in range(len(sortt)):
        ii = sortt[i][1]
        j = sortt[i][2]
        res.append([R[ii][j][0], R[ii][j][1]])
    return block(res)


def index_generator(r, id):
    index = []
    r_sorted = tri(r, id)
    for i in range(len(r_sorted)):
        for j in range(len(r_sorted[i])):
            for k in range(len(r)):
                for l in range(len(r[k])):
                    if r[k][l][id] == r_sorted[i][j][id]:
                        index.append([r[k][l][id], k, l])
    # enlever les doublons créés lorsqu'il y a 2 memes Y
    index_sans_doublons = []
    for sublist in index:
        if sublist not in index_sans_doublons:
            index_sans_doublons.append(sublist)
    return index_sans_doublons

