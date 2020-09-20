import socket

s = socket.socket()
print("socket succesfully installed")

port = 12345

# not specifying the ip
# lets the server listen to requests
# coming from other computers on the network
print(socket.gethostname())
s.bind(('',port))
print('socket binded to %s'%(port))

s.listen(5)
print('socket is litening')

# a forever loop until we interrupt it
# or an error occurs
while True:
    clientsocket,addr = s.accept()
    print(f"connection from {addr} has been established")
    clientsocket.send(bytes('Welcome to the Server!','utf-8'))
    clientsocket.close()


