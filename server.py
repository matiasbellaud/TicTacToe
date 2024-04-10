import os
import socket

from Display import Display
from IsGameEnd import isGameEnd
from StringToListe import stringToListe
from inputList import inputList
from listToString import listToString

def Main():

    client = ('192.168.229.110', 4006)

    server = socket.socket( socket.SOCK_DGRAM)
    
    server.bind(('192.168.229.30', 4000))
    server.listen(200)
    client_socket, client_address = server.accept()

    isGame = True
    while isGame :
        
        donnees = client_socket.recv(1024).decode('utf-8')
        
        donnees = stringToListe(donnees)
        gameStatus = isGameEnd(donnees)
        if gameStatus != 0:
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            Display(donnees)
            match gameStatus:
                case 2:
                    print("you have win")
                    break
                case 1:
                    print("the other have win")
                    break
                case 3:
                    print("no cells left")
                    break
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        Display(donnees)


        donnees = inputList(donnees,2)
        gameStatus = isGameEnd(donnees)
        if gameStatus != 0:
            client_socket.send(listToString(donnees).encode('utf-8'))
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            Display(donnees)
            match gameStatus:
                case 2:
                    print("you have win")
                    break
                case 1:
                    print("the other have win")
                    break
                case 3:
                    print("no cells left")
                    break
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        Display(donnees)
        client_socket.send(listToString(donnees).encode('utf-8'))
        
    client_socket.close()
    server.close()

   
if __name__=='__main__':
    Main()
