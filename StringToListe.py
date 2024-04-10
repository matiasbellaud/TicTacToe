def stringToListe(liste):
    liste2 = [[0,0,0],[0,0,0],[0,0,0]]
    index=0
    for i in range(3) :
        for j in range(3) :
            liste2[i][j] = int(liste[index])
            index = index+1

    return (liste2)