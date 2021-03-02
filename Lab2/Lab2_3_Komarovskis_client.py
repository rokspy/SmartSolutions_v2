import socket
import time
import sys
import threading 

def listenThread():
	global s, connection_status
	while True:
		try:
			data = s.recv(4096).decode()
			if len(data) > 0: print(data)
		except:
			connection_status = 0
			break



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
connection_status = 1

listen_thread = threading.Thread(target=listenThread, daemon=False)
listen_thread.start()
time.sleep(1)
try:
	while True:
		if connection_status == 0:
			print("No more Connection")
			s.close()
			break
		msg = input("Input message: ")	
		s.sendall(msg.encode())
		print("Sent: " + msg)
		time.sleep(0.2)



except KeyboardInterrupt:
	s.close()

