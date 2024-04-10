import socket

host='192.168.229.110' #client ip
port = 4005

server = ('192.168.229.30', 4000)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(server)
print ('Connexion vers ' + host + ':' + str(port) + ' reussie.')

message = input("-> ")
while message !='q':
    client.sendto(message.encode('utf-8'), server)
    data, addr = client.recvfrom(1024)
    data = data.decode('utf-8')
    print("Received from server: " + data)
    message = input("-> ")

