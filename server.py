import socket
from _thread import *

server = "192.168.1.74"
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen(2)
print("Waiting for connection, Server Started")


def thread_client(connect):
    conn.send(str.encode("Connected"))
    reply = ""
    while True:
        try:
            data = connect.recv(2048)
            reply = data.decode("utf-8")

            if not data:
                print("Disconnected")
                break
            else:
                print("Received: ", reply)
                print("Sending: ", reply)
            connect.sendall(str.encode(reply))
        except:
            break

    print("Lost Connection")
    conn.close()



while True:
    conn, addr = s.accept()
    print("Connected to:", addr)

    start_new_thread(thread_client, (conn,))
