import socket
import threading
import random

def handle_client(client_socket):
    data = client_socket.recv(1024).decode()
    name, num = data.split()
    num = int(num)

    if num < 1 or num > 100:
        return

    print(f"Client's name: {name}")
    print("Server's name:  Sir")
    server_num = random.randint(1, 100)
    print(f"Client's number: {num}")
    print(f"Server's number: {server_num}")
    print(f"Sum: {num + server_num}")

    message = f" Sir {server_num}"
    client_socket.sendall(message.encode())

    client_socket.close()

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', 8000))
    server_socket.listen(5)
    print('Server listening on 0.0.0.0:8000...')

    while True:
        client_socket, client_address = server_socket.accept()
        print(f'Accepted connection from {client_address}')
        client_thread = threading.Thread(target=handle_client, args=(client_socket,))
        client_thread.start()

if __name__ == '_main_':
    main()