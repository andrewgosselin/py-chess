import socket
from _thread import *
import sys

# Create Server
server = "192.168.1.6"
port = 5555
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen(5)
print("Server started, listening for connections...")

def threaded_client(conn):
    conn.send(str.encode("Connected."))
    reply = ""
    while True:
        try:
            data = conn.recv(2048)
            reply = data.decode("utf-8")

            if not data:
                print("Diconnected.")
                break
            else:
                print("Recieved: ", reply)
                print("Sending: ", reply)
            conn.sendall(str.encode(reply))
        except:
            break
    print("Connection lost..")
    conn.close()

while True:
    conn, addr = s.accept()
    print("Connected client: ", addr)
    start_new_thread(threaded_client, (conn,))
