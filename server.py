import socket
import threading

HOST = '127.0.0.1'  #replace with server ip if over internet
PORT= 9090


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))

server.listen()

clients = []
nicknames = []

#broadcast chats
def broadcast(message):
    for client in clients:
        client.send(message) 

#handle connections
def handle():
    

#recieve new connections
def recieve():
    while True:
        client, address = server.accept()
        print(f'Connected with {str(address)}')

        client.send("NICK".encode('utf-8'))
        nickname = clients.recv(1024)

        nicknames.append(nickname)
        clients.append(client)

        print(f"Nickname of the clienr is {nickname}")
        broadcast(f'{nickname} connecte to the server\n'.encode('utf-8'))

        client.send("Connected to the server".encode('utf-8'))

        thread = threading.Thread(target=handle, args=(client,))





