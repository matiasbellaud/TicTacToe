import socket

from Display import Display
from StringToListe import StringToListe
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
        print(donnees)
        Display(donnees)

        liste = inputList(donnees,2)
        liste = listToString(liste)
        server.sendto(liste.encode('utf-8'), client)
        Display(donnees)
        
    client_socket.close()
    server.close()

   
if __name__=='__main__':
    Main()
