import threading
import socket
import numpy as np
import time
import subprocess


def clientThread(connection, connection_index):
    global tickets, led_taken, display_taken
        socket_started = 0
	led_started = 0
	display_started = 0

        connection.send("\n\nWelcome to my server ".encode())
        try:
            while True:
                # Wair for data fromt the client
                data = connection.recv(4096).decode()

                # Check if data valid, if not run kill routine
                if not data:
                    connection.close()
                    tickets[connection_index] = 0
                    try:	function_socket.close()
                    except: 	continue
                    if led_started == 1:
                        led_taken=0
                    	led_func.kill()
                    elif display_started == 1:
			display_taken = 0
			display_func.kill()
                    break
 
		# If either LED function or display function is started by this thread then forward the data received from the client to the function
                if led_started == 1 or display_started == 1:
                    function_socket.sendall(data.encode())

                if data == "LED":
                    function_socket = socket.Socket(socket.AF_INET, socket.SOCK_STREAM)
                    s.bind(("local_host",8889))
                    led_func = subprocess("./led_func.py")

        except KeyboardInterrupt:
            print("Kill connection")
                connection.close()
                try:	function_socket.close()
                        if led_started == 1:
                            led_taken=0
                                led_func.kill()
                        elif display_started == 1:	display_taken = 0
                except: continue


led_port = 8889
display_port = 8890
led_taken = 0
display_taken = 0

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("localhost", 8888))
s.listen(10)

# Using a list to keep track of connections and order of connections 
tickets = np.zeros(2)
connections = [0,0]

try:
    while True:
        next_ticket = np.where(tickets==0)		# Look for usable connection locations 
                if 0 in tickets:				# If there are usable locations start thread for the client 
                    print("Waiting for connection...")	
                        free_loc = np.where(tickets==0)[0][0]
                        connections[free_loc], address = s.accept() # All connections are saved in a list 
                        new_thread = threading.Thread(target=clientThread, args=(connections[free_loc],free_loc), daemon=True)
                        new_thread.start()
                        tickets[free_loc] = 1			# Set the connection location to taken
                        print("New Connetion...")
                else:						# If there are no location spots available, then wait
                    print("...Can't take more clients...")
                        print()
                        time.sleep(10)

except KeyboardInterrupt:
    for k in range(len(connections)):
        print(connections[k])
                if connections[k] != 0:
                    connections[k].close()
        s.close()






