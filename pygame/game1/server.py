import socket
from _thread import *
import sys
# 172.26.185.92 
server = "172.26.185.92"
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server,port))
except socket.error as e:
    print(e)

s.listen(2) # allow only 2 people to connect to the server
print("Waiting for connection, Server Started!")

def threaded_client(conn):
    reply = ""

    conn.send(str.encode("Connected!"))
    while True:

        try:
            data = conn.recv(2048)
            reply = data.decode("utf-8")

            if not data:
                print("Disconnected!")
                break
            else:
                print("Received: ", reply)
                print("Sending: ", reply)
            
            conn.sendall(str.encode(reply))
        except:
            break
    print("Lost Connection!")
    conn.close()
        
while True:
    conn,addr = s.accept()
    print("Connected to",addr)

    start_new_thread(threaded_client, (conn, ))

