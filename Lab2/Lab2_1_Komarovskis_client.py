import socket
import time
import sys
import threading 

def listenThread():
	global s
	while True:
		data = s.recv(4096).decode()
		if not data:
			break
		print(data)


port = 8888
host = "localhost"
IP_addr = socket.gethostbyname(host)

if len(sys.argv) == 2:
    IP_addr = sys.argv[1]
elif len(sys.argv) == 3:
    IP_addr = sys.argv[1]
    port = int(sys.argv[2])

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((IP_addr, port))


listen_thread = threading.Thread(target=listenThread, daemon=True)
listen_thread.start()
time.sleep(1)
try:
	while True:
		msg = input("Input message: ")	
		s.sendall(msg.encode())
		print("Sent: " + msg)
		time.sleep(0.1)



except KeyboardInterrupt:
	s.close()

