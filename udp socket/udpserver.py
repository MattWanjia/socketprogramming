import socket
import time

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('0.0.0.0', 5000))

while True:
    data, addr = sock.recvfrom(1024)

    print(data.decode('utf-8'))

    msg = 'Hi client'
    sock.sendto(bytes(msg, 'utf-8'),addr)
    time.sleep(3)