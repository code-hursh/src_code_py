import socket

class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_NET,socket.SOCK_STREAM)
        self.server = "192.168.1.34"
        self.port = 5555
        self.addr = (self.server, self.port)
        self.id = self.connect()
        print(self.id)
    
    def connect(self):
        try:
            self.client.connect(self.addr)
            self.return(self.client.recv(2048).decode())
        except:
            pass

n = Network()

