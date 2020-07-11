import socket

HOST = '192.168.0.133'
PORT = 65432
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b'Privet Olya')
    data = s.recv(1024)

print('Received', repr(data))