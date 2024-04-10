import socket
from Display import Display
from inputList import inputList
from IsGameEnd import IsGameEnd
import os
from listToString import listToString
from StringToListe import StringToListe

host='192.168.229.110' #client ip
port = 4005

server = ('192.168.229.30', 4000)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(server)
print ('Connexion vers ' + host + ':' + str(port) + ' reussie.')

game = [[0,0,0],[0,0,0],[0,0,0]]

while True:
    Display.Display(game)

    game = inputList(game,1)
    gameStatus = IsGameEnd(game)
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
    print(listToString(game))
    Display.Display(game)
    client.sendto(listToString(game).encode('utf-8'), server)
    data, addr = client.recvfrom(1024)
    os.system("clear")
    data = data.decode('utf-8')
    game = StringToListe(data)
    gameStatus = IsGameEnd(game)
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

