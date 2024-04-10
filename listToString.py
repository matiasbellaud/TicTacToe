def listToString(game):
    res = ""
    for line in game:
        for cell in line:
            res += str(cell)
    return res