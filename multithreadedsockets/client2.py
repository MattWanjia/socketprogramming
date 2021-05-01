import socket
import time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(('0.0.0.0', 5000))

while True:
    s.send(bytes('hi server, i am client 2', 'utf-8'))

    data = s.recv(1024)
    decoded = data.decode('utf-8')

    print(decoded)

    time.sleep(3)
