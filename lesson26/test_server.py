import socket
HOST = '127.0.0.1'
PORT = 6789
sock_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock_server.bind((HOST, PORT))
while True:
    data, addr = sock_server.recvfrom(1024)
    print(f"Message: {data.decode('utf-8')}") # Добавив "decode" бо виводило "b" перед "Hello"
