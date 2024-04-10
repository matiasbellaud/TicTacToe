import socket

from inputList import inputList

def Main():

    client = ('192.168.229.110', 4005)

    server = socket.socket( socket.SOCK_DGRAM)
    server.bind(('192.168.229.30', 4000))
    server.listen(200)

    client_socket, client_address = server.accept()
    donnees = client_socket.recv(1024).decode('utf-8')
    print("Données reçues du client :", donnees)
    message = input("-> ")
    server.sendto(message.encode('utf-8'), client)

    client_socket.close()
    server.close()

   
if __name__=='__main__':
    Main()
