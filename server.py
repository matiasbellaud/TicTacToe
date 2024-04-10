import socket

from Display import Display
from IsGameEnd import isGameEnd
from StringToListe import stringToListe
from inputList import inputList
from listToString import listToString

def Main():

    client = ('192.168.229.110', 4005)

    server = socket.socket( socket.SOCK_DGRAM)
    server.bind(('192.168.229.30', 4000))
    server.listen(200)

    

    isGame = True
    while isGame :
        client_socket, client_address = server.accept()
        donnees = client_socket.recv(1024).decode('utf-8')
        
        donnees = StringToListe(donnees)
        gameStatus = IsGameEnd(donnees)
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
        Display(donnees)


        donnees = inputList.inputList(donnees,2)
        gameStatus = IsGameEnd=(donnees)
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
        print(listToString.listToString(donnees))
        Display.Display(donnees)
        server.sendto(listToString.listToString(donnees).encode('utf-8'), server)
        
    client_socket.close()
    server.close()

   
if __name__=='__main__':
    Main()
