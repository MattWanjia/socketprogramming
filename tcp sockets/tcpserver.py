import socket

server_EP = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_EP.bind(('0.0.0.0', 5000))
server_EP.listen(5)

while True:
    print("Server waiting...")
    client_EP, client_addr = server_EP.accept()
    print(f'client connected from {client_addr}')

    while True:
        data = client_EP.recv(1024)
        if not data or data.decode('utf-8') == 'END':
            break
        print(f'received data: {data.decode("utf-8")}')
        try:
            client_EP.send(bytes('Hey client','utf-8'))
        except:
            print("Exited")


