import socket
SERVER =  "172.16.58.53"
PORT = 8080
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((SERVER, PORT))
client.sendall(bytes("this is from client", 'UTF-8'))
while True:
    in_data = client.recv(1024)
    print("from server : ", in_data.decode())
    out_data = input()
    client.sendall(bytes(out_data, 'UTF-8'))
    if out_data == 'bye':
        break
client.close()