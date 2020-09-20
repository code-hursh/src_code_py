import socket
import sys

try:
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    print("Socket successfully installed")
except socket.error as err:
    print("Socket creation failed with error %s"%(err))

port = 80

try:
    host_ip = socket.gethostbyname('www.google.com')
except socket.gaierror:

    # this means that couldn't resolve the host
    print("there was an error in resolving the host")
    sys.exit()

# connecting to the server
s.connect((host_ip, port))

print("""the socket has successfully connected to google
        on post == %s"%(host_ip)""")

