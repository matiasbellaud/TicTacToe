import socket

def Main():

    s = socket.socket( socket.SOCK_DGRAM)
    host = '192.168.229.30' #Server ip
    port = 4000
    s.bind(('192.168.229.30', 4000))
    print("test1")
    s.listen(5)
    print("test2")
    client_socket, client_address = s.accept()
    print("test3")
    donnees = client_socket.recv(1024).decode('utf-8')
    print("test4")
    print("Données reçues du client :", donnees)

    # Fermer la connexion avec le client
    client_socket.close()

    # Fermer le socket serveur
    s.close()
    # s.bind((host, port))


    # print("Server Started")
    # while True:
        
    #     data, addr = s.recvfrom(1024)
    #     print(addr)
    #     data = data.decode('utf-8')
    #     print("Message from: " + str(addr))
    #     print("From connected user: " + data)
    #     data = data.upper()
    #     print("Sending: " + data)
    #     s.sendto(data.encode('utf-8'), addr)
    # s.close()
   
if __name__=='__main__':
    Main()
