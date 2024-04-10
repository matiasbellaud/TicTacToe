import socket

from Display import Display
from inputList import inputList

def Main():

    client = ('192.168.229.110', 4005)

    server = socket.socket( socket.SOCK_DGRAM)
    server.bind(('192.168.229.30', 4000))
    server.listen(200)

    

    isGame = True
    while isGame :
        client_socket, client_address = server.accept()
        donnees = client_socket.recv(1024).decode('utf-8')
        Display(donnees)

        liste = inputList(donnees,2)
        client.sendto(liste.encode('utf-8'), client)
        Display(donnees)
        
    client_socket.close()
    server.close()

   
if __name__=='__main__':
    Main()
