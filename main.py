import socket

def Main():
    typeOfPlayer = "client" # or client
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    if  typeOfPlayer == "host":

        host = '127.0.0.1' #Server ip
        port = 4000

        s.bind(('127.0.0.1', 4000))
        # s.bind((host, port))

        print("Server Started")
        while True:
            
            data, addr = s.recvfrom(1024)
            print(addr)
            data = data.decode('utf-8')
            print("Message from: " + str(addr))
            print("From connected user: " + data)
            data = data.upper()
            print("Sending: " + data)
            s.sendto(data.encode('utf-8'), addr)
    else :
        host='192.168.229.110' #client ip
        port = 4005
        
        server = ('192.168.229.30', 4000)
        
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((host, port))
        print ('Connexion vers ' + host + ':' + str(port) + ' reussie.')
        
        message = input("-> ")
        while message !='q':
            client.sendto(message.encode('utf-8'), server)
            data, addr = client.recvfrom(1024)
            data = data.decode('utf-8')
            print("Received from server: " + data)
            message = input("-> ")
    s.close()
   
if __name__=='__main__':
    Main()
