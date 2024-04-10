import socket
import Display
import inputList
import IsGameEnd
import os
import listToString
import StringToListe

host='192.168.229.110' #client ip
port = 4005

server = ('192.168.229.30', 4000)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(server)
print ('Connexion vers ' + host + ':' + str(port) + ' reussie.')

game = [[0,0,0],[0,0,0],[0,0,0]]

while True:
    Display.Display(game)

    game = inputList.inputList(game,1)
    gameStatus = IsGameEnd.IsGameEnd(game)
    if gameStatus != 0:
        match gameStatus:
            case 1:
                print("you have win")
                break
            case 2:
                print("the other have win")
                break
            case 3:
                print("no cells left")
                break
    print(listToString.listToString(game))
    Display.Display(game)
    client.sendto(listToString.listToString(game).encode('utf-8'), server)
    data, addr = client.recvfrom(1024)
    os.system("clear")
    data = data.decode('utf-8')
    game = StringToListe.StringToListe(data)
    gameStatus = IsGameEnd.IsGameEnd(game)
    if gameStatus != 0:
        match gameStatus:
            case 1:
                print("you have win")
                break
            case 2:
                print("the other have win")
                break
            case 3:
                print("no cells left")
                break

