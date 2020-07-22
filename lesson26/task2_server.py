from lesson26.cesar_cipher import cesar
import socket

HOST = '127.0.0.1'
PORT = 54321

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)

            if not data:
                break
            data = cesar(data)
            conn.sendall(bytes(data, encoding='utf-8'))

