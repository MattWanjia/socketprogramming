import socket
import time

client_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    msg = 'Hi server? I am client'
    client_sock.sendto(bytes(msg, 'utf-8'), ('0.0.0.0', 5000))

    data, addr = client_sock.recvfrom(1024)
    print(data.decode('utf-8'))
    time.sleep(3)
