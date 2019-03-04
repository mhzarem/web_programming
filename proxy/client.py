import socket
import time

host = '127.0.0.1'
port = 8002
count = 0

while True:
        count += 1
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host, port))
        s.sendto(b'hello word', (host, port))
        print("number: ", count, s.getpeername(), s.getsockname())
        # data = s.recv(1024).decode("utf-8")
        # print(repr(data))
        time.sleep(10)



