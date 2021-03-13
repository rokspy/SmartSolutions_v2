import socket 
import threading 
import time

def listenThread():
	global s
	while True:
			data = s.recv(4096).decode()
			if not data:
				s.close()
				break
			print(data)


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("localhost", 8888))


listen_thread = threading.Thread(target=listenThread, daemon=True)
listen_thread.start()

try:
	while True:
		send_msg = input("Send data: ")
		s.sendall(send_msg.encode())
except KeyboardInterrupt:
	s.close()
	print("Thats it")
	
