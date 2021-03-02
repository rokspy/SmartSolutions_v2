import socket
import threading 
import sys
import time 

### FUNCTIONS ###

def func_FlashLED():
	while True:
		print("Flashing LEDs in opposite phases")
		time.sleep(1)

def func_DisplayManiuplation():
	while True:
		print("Receives input from client and changes the display accordingly")
		time.sleep(1)
				

def clientThread(connection):
	print("New Connection established")
	global LED_func_status, Display_func_status
	connection.send("\n\nWelcome to my server ".encode())	
	
	data = connection.recv(4096)	
	if data == "LED" and LED_func_status == 0:
		while True:
			try:
				func_FlashLED()	
			except KeyboardInterrupt:
				break
	elif data == "Display" and LED_func_status == 0:
		while True:
			try:
				func_DisplayManipulation()
			except KeyboardInterrupt:
				break
	else:
		connection.sendall("No valid function".encode())

	connection.sendall("Close".encode())	
	connection.close()
	print("Connection Closed")


### MAIN CODE ####


port = 8888 
host = "localhost"
IP_addr = socket.gethostbyname(host)

if len(sys.argv) > 1:
	port = int(sys.argv[1])

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((IP_addr, port))
s.listen(10) 			# Number of possible connections


try:
	while True:
		print("Waiting for conncetion...")
		connection, address = s.accept()
		print("New connection...")
				

		new_thread = threading.Thread(target=clientThread, args = (connection,), daemon=True)
		new_thread.start()
except KeyboardInterrupt:
	time.sleep(1)
	print("Socket closed")
	# Additional GPIO cleanup
	s.close()	

