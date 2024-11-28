import socket
import threading
import os

host =  "0.0.0.0"
port = int(os.environ.get("PORT", 8080))

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host,port))
server.listen()

clients = []
nicknames = []

def broadcast(message, sender_client = None):
    for client in clients:
        if client != sender_client:
            try:
                client.send(message)
            except:
                client.close()
                remove_client(client)

def handle(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            remove_client(client)
            break

def remove_client(client):
    if client in clients:
        index = clients.index(client)
        clients.remove(client)
        nickname = nicknames[index]
        broadcast(f"{nickname} left the chat".encode('utf-8'))
        nicknames.remove(nickname)
        client.close()

def recieve():
    while True:
        client, address = server.accept()
        print(f"Connected with {str(address)}")

        client.send('balls'.encode('utf-8'))
        nickname = client.recv(1024).decode('utf-8')
        nicknames.append(nickname)
        clients.append(client)

        print(f"Nickname of the client is {nickname} ")
        broadcast(f"{nickname} joined the chat".encode('utf-8'))
        client.send('connected to the server'.encode('utf-8'))

        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

print("server is up and running")
recieve()
        
