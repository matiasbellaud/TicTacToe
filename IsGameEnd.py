# return 1 if player 1 have win
# return 2 if player 2 have win
# return 3 if all cell are full
# return 0 if the game is not over
def isGameEnd(game):
    for i in range(3):
        # check line
        if game[i][0] == game[i][1]  == game[i][2] != 0:
            return game[i][0]
        # check column
        if game[0][i] == game[1][i] == game[2][i] != 0:
            return game[0][i]
    # check diagonals
    if game[0][0] == game[1][1] == game[2][2] != 0:
        return game[0][0]
    if game[0][2] == game[1][1] == game[2][0] != 0:
        return game[0][0]
    # check if there is empty cells
    for line in game:
        for cell in line:
            if cell == 0:
                return 0
    return 3