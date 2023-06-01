import socket
while True:
    mes = input('Input same massege: ')
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(('localhost', 56000))
    sock.send(bytes(mes, encoding="UTF-8"))
    data = sock.recv(1024)
    sock.close()
    print(data)
    if mes == 'stop':
        break
