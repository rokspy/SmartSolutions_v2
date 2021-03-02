import socket
import threading 
import sys


def clientThread(connection):
	connection.send("\n\nWelcome to my server ".encode())	
	while True:
		try:	
			data = connection.recv(4096)	
			if not data:
				break
			reply = "Your message was " + data.decode()
			print("Received: " + data.decode())
			connection.sendall(reply.encode())
		except socket.error as error_msg:
			print(error_msg)
			break
	connection.close()

port = 8888 
host = "localhost"
IP_addr = socket.gethostbyname(host)

if len(sys.argv) > 1:
	port = int(sys.argv[1])

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((IP_addr, port))
s.listen(2) 			# Number of possible connections


try:
	while True:
		print("Waiting for conncetion...")
		connection, address = s.accept()
		print("New connection...")
				

		new_thread = threading.Thread(target=clientThread, args = (connection,), daemon=False)
		new_thread.start()
except KeyboardInterrupt:
	s.close()	

