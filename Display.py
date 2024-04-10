def Display(game):
    copyGame = [[],[],[]]
    idLine = 0
    for line in game:
        for cell in line:
            newCell = 0
            match cell:
                case 0:
                    newCell = " "
                case 1:
                    newCell = "O"
                case 2:
                    newCell = "X"
            copyGame[idLine].append(newCell)
        idLine+=1
    print("game : ")
    for line in copyGame:
        print("|"+str(line[0])+","+str(line[1])+","+str(line[2])+"|")
    # display coo of each cells
    print("cells coordonates :")
    print("|1,2,3|")
    print("|4,5,6|")
    print("|7,8,9|")
game = [[1,2,2],[0,1,0],[2,1,1]]
DisplayUserInterface(game)