import socket
HOST = '127.0.0.1'
PORT = 6789
msg = "Hello"
sock_client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock_client.sendto(bytes(msg, encoding='utf-8'), (HOST, PORT))

