import requests
import socket
import time
from threading import *

max_connection = 5
host = '127.0.0.1'
port = 8002


def thread(conn, addr):
    # print("the thread number", get_ident())
    data = conn.recv(1024).decode("utf-8")
    # print(data)
    first_line = data.split('\n')[0]
    op = first_line.split(' ')[0]
    url = first_line.split(' ')[1]
    host = str(data.split('\n')[1].split(' ')[1]).strip('\r')
    print("*" * 140)
    print(type(host), host)
    print(host == 'www.shabanali.com')
    print("*" * 140)
    if host == 'www.shabanali.com':
        conn.sendto("HTTP/1.1\r200\rOK\r\n\r\n you are filterd ".encode(), addr)
        print("#"*170)

    else:
        data = requests.get(url)
        conn.sendto(data.content, addr)
        print(data.content)
    time.sleep(12)


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((host, port))

    while True:
        s.listen(max_connection)
        conn, addr = s.accept()

        Thread(group=None, target=thread, name="thread", args=[conn, addr]).start()
