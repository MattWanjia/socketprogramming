import socket
from _thread import *

server_EP = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = '0.0.0.0'
port = 5000
threadcount = 0

server_EP.bind((host,port))
server_EP.listen(5)

def client_thread(connection):
    connection.send(bytes('welcome to the server', 'utf-8'))

    while True:
        data = connection.recv(1024)
        print(data.decode('utf-8'))
        reply = 'hello i am server'
        connection.send(bytes(reply, 'utf-8'))

while True:
    client, addr = server_EP.accept()
    print(f'connectec to {addr[0]} and {addr[1]}')

    start_new_thread(client_thread, (client, ))
    threadcount += 1