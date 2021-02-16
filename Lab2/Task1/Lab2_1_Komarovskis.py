import socket
import sys
import threading 


port = 65432
IP_addr = '172.17.55.194'
print(socket.gethostbyname('raspberrypi'))

if len(sys.argv) == 2:
    IP_addr = sys.argv[1]
elif len(sys.argv) == 3:
    IP_addr = sys.argv[1]
    port = sys.argv[2]

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print(IP_addr, port)


s.connect((IP_addr, port))


