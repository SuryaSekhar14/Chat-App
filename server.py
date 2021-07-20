import socket
import threading

HOST = '127.0.0.1'  #replace with server ip if over internet
PORT= 9090


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))

server.listen()

clients = []
nickname = []

#broadcast chats


#recieve new connections


#handle connections




