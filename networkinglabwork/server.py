import socket
import random

server_socket = socket.socket()
server_ip = "127.0.0.1"
server_port = 12345
server_socket.bind((server_ip, server_port))

server_socket.listen(1)

while True:
    client_socket, client_address = server_socket.accept()
    print("Connected by", client_address)

    data = client_socket.recv(1024).decode()
    name, num = data.split()
    num = int(num)

    if num < 1 or num > 100:
        break

    print("Client's name:", name)
    print("Server's name: HEllo JI")

    server_num = random.randint(1, 100)
    print("Client's number:", num)
    print("Server's number:", server_num)
    print("Sum:", num + server_num)

    message = "Chai peelo frnds " + str(server_num)
    client_socket.sendall(message.encode())

    client_socket.close()

server_socket.close()