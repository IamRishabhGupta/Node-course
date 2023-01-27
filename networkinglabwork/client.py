import socket

client_socket = socket.socket()

server_ip = "127.0.0.1"
server_port = 12345

client_socket.connect((server_ip, server_port))

name = input("Enter your name: ")
num = int(input("Enter an integer between 1 and 100: "))

message = name + " " + str(num)
client_socket.sendall(message.encode())

data = client_socket.recv(1024).decode()
print(data)

client_socket.close()