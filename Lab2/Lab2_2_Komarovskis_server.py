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
ip_address = "localhost"

if len(sys.argv) == 2:
	ip_address = sys.argv[1]
if len(sys.argv) == 3:
	ip_address = sys.argv[1]
	port = sys.argv[2]

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((ip_address, port))
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

