import socket
from Display import Display
from inputList import inputList
from IsGameEnd import isGameEnd
import os
from listToString import listToString
from StringToListe import stringToListe

host='192.168.229.110' #client ip
port = 4005

server = ('192.168.229.30', 4000)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.bind((host,port))
client.connect(server)
print ('Connexion vers ' + host + ':' + str(port) + ' reussie.')

game = [[0,0,0],[0,0,0],[0,0,0]]

while True:
    Display(game)

    game = inputList(game,1)
    gameStatus = isGameEnd(game)
    if gameStatus != 0:
        match gameStatus:
            case 1:
                print("you have win")
                client.sendto(listToString(game).encode('utf-8'), server)
                break
            case 2:
                print("the other have win")
                client.sendto(listToString(game).encode('utf-8'), server)
                break
            case 3:
                print("no cells left")
                client.sendto(listToString(game).encode('utf-8'), server)
                break
    print(listToString(game))
    Display(game)
    client.sendto(listToString(game).encode('utf-8'), server)
    data, addr = client.recvfrom(1024)
    os.system("clear")
    data = data.decode('utf-8')
    game = stringToListe(data)
    gameStatus = isGameEnd(game)
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

