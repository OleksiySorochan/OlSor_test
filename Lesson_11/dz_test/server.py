import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('', 56000))
sock.listen(10)
print('Server is runnung')
while True:
    conn, adrr = sock.accept()
    print('connected', adrr)
    data = conn.recv(1024)
    print(str(data))
    conn.send(data.upper())
conn.close()
