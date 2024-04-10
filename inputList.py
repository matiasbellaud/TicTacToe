def inputList(liste, player):
    message = input("nombre entre 1 et 9 -> ")
    if message.isdigit() == True :
        if int(message) <= 9 and int(message) >= 1 :
            tic = 0
            for i in range(3):
               for j in range(3): 
                   tic = tic + 1
                   if tic == int(message):
                       if liste[i][j] == 0 :
                            liste[i][j] = player
                       else :
                            print("entré non valide")
                            return inputList(liste,player)
                                    
        else :
            print("entré non valide")
            return inputList(liste,player)
    else :
        print("entré non valide")
        return inputList(liste,player)

    return (liste)