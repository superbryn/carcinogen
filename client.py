import socket
import threading

ipaddrs = 'https://carcinogen.onrender.com'

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((ipaddrs, 55555))

nickname = input("ENTER THE NICKNAME : ")

def recieve():
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            if message == "balls":
                client.send(nickname.encode('utf-8'))
            else:
                print(message)
        except:
            print("404")
            client.close()
            break

def write():
    while True:
        message = f"{nickname} : {input("")}"
        client.send(message.encode('utf-8'))

recieve_thread = threading.Thread(target=recieve)
recieve_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()