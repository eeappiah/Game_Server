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


def read_pos(str):
    str = str.split(",")
    return int(str[0]), int(str[1])


def make_pos(tup):
    return str(tup[0]) + "," + str(tup[1])


pos = [(0, 0), (100, 100)]


def thread_client(connect, currentPlayer):
    conn.send(str.encode(make_pos(pos[currentPlayer])))
    reply = ""
    while True:
        try:
            data = read_pos(conn.recv(2048).decode())
            pos[currentPlayer] = data


            if not data:
                print("Disconnected")
                break
            else:
                if currentPlayer == 1:
                    reply = pos[0]
                else:
                    reply = pos[1]
                print("Received: ", reply)
                print("Sending: ", reply)
            connect.sendall(str.encode(make_pos(reply)))
        except:
            break

    print("Lost Connection")
    conn.close()


currentPlayer = 0

while True:
    conn, addr = s.accept()
    print("Connected to:", addr)

    start_new_thread(thread_client, (conn, currentPlayer))
    currentPlayer += 1
