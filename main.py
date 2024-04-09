import socket

def Main():
    typeOfPlayer = "host", # or client
    if ( typeOfPlayer == "host") :

        host = '192.168.0.12' #Server ip
        port = 4000

        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.bind((host, port))

        print("Server Started")
        while True:
            data, addr = s.recvfrom(1024)
            data = data.decode('utf-8')
            print("Message from: " + str(addr))
            print("From connected user: " + data)
            data = data.upper()
            print("Sending: " + data)
            s.sendto(data.encode('utf-8'), addr)
    else :
        host='192.168.0.13' #client ip
        port = 4005
        
        server = ('192.168.0.12', 4000)
        
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.bind((host,port))
        
        message = input("-> ")
        while message !='q':
            s.sendto(message.encode('utf-8'), server)
            data, addr = s.recvfrom(1024)
            data = data.decode('utf-8')
            print("Received from server: " + data)
            message = input("-> ")
    s.close()
   
if __name__=='__main__':
    Main()
