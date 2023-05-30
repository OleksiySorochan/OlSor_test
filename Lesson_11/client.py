import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('localhost', 55000))
sock.send(bytes("This is client, answer me", encoding='UTF-8'))
data = sock.recv(1024)
sock.close()
print(data)