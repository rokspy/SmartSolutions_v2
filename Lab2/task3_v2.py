import threading
import sys
import socket
import numpy as np
import time
import subprocess

def sendToFunction(conn, sock, subprocess, function_clear, data):
        should_break = 0
        try:
                conn.sendall(data.encode())     
                return should_break, function_clear
        except:
                print("No connection to the function")
                function_clear = 0
                sock.close()
                subprocess.kill()
                should_break = 1
                return should_break, function_clear

def startFunction(function_name, port, client_connection):
    function_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    function_socket.bind(("localhost",port))
    function_socket.listen(2)
    func_subproc = subprocess.Popen(function_name)
    function_connection,_ = function_socket.accept()
    listen_to_function = threading.Thread(target=listenToFunction, args=(function_connection, client_connection,), daemon=True)
    listen_to_function.start()
    
    return function_socket, function_connection, func_subproc
        
def listenToFunction(connection, client_connection):
    while True:
            try:
                received = connection.recv(4096).decode()
                if not received:
                    break
                client_connection.sendall(received.encode())
            except:
                break
                

def clientThread(connection, connection_index):
		# led/display_taken are to check or tell gloablly that the corresponding function is taken 
        global tickets, led_taken, display_taken
		# led/display_started used to remember which function was started within this thread
        led_started = 0
        display_started = 0
        connection.send("\n\nWelcome to my server ".encode())
        try:
            while True:
                	# Wait for data fromt the client
                        try: data = connection.recv(4096).decode()
                        except: data = "kill"
                        # Check if data valid, if not run kill routine 
                        if not data:
                            connection.close()
                            tickets[connection_index] = 0
                            print("client ctrl+c...")
                            try:
                                if display_started==1 or led_started == 1: function_connection.sendall("kill".encode())
                            except: continue
                            time.sleep(1)
                            try:
                                function_connection.close()
                                function_socket.close()
                            except: continue
                            if led_started == 1:
                                led_taken=0
                                led_func.kill()
                            elif display_started == 1:
                                display_taken=0
                                display_func.kill()     
                            break
                        if data == "kill":
                            try:
                                if display_started==1 or led_started == 1: function_connection.sendall("kill".encode())
                            except: continue
                            time.sleep(1)
                            

                       	# If led function was chosen in the previous loops, the following condition will be met  
                        elif led_started == 1:
							# This function tries to send the data received from the client to the function, if fails then closes the connections and returns a variable that indicates that while loop has to be killed
                            check, led_taken = sendToFunction(function_connection, function_socket, led_func, led_taken, data)
                            if check == 1: break
                        elif display_started == 1:
                            check, display_taken = sendToFunction(function_connection, function_socket, display_func, display_taken, data)
                            if check == 1: break	
		        # If the previous loops any functions has not been started, following condtions are specific messages from the client that will start the function, also checks if the function is not already taken
                        elif data == "LED" and led_taken == 0:
                            function_socket,function_connection, led_func = startFunction("./led_func.py", 8889, connection)
                            led_taken = 1       # Tells globally that the function is taken 
                            led_started = 1     # For memorising which function is being taken in this thread
                        elif data == "LED" and led_taken == 1:
                            connection.sendall("LED function is not available".encode())
                        elif data == "DISPLAY" and display_taken == 0:
                            function_socket,function_connection, display_func = startFunction("./display_func.py", 8890, connection)
                            display_taken = 1       # Tells globally that the function is taken 
                            display_started = 1     # For memorising which function is being taken in this thread
                        elif data == "DISPLAY" and display_taken == 1:
                            connection.sendall("DISPLAY function is not available".encode())


        except KeyboardInterrupt:
			
            print("Kill connection")
            connection.close()
            tickets[connection_index] = 0
            try:    
                    function_connection.close()
                    function_socket.close()
                    if led_started == 1:
                        led_taken=0
                        led_func.kill()
                    elif display_started == 1:
                        display_taken = 0
                        display_func.kill()
            except:pass 

if len(sys.argv) == 2:
	ip_address = sys.argv[1]
	port = 8888
elif len(sys.argv) == 3:
	ip_address = sys.argv[1]
	port = int(sys.argv[2])
else:
	ip_address = "localhost"
	port = 8888


led_port = 8889
display_port = 8890
led_taken = 0
display_taken = 0

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((ip_address, port))
s.listen(10)

# Using a list to keep track of connections and order of connections 
tickets = np.zeros(2)
connections = [0,0]

try:
    while True:
        next_ticket = np.where(tickets==0)              # Look for usable connection locations 
        if 0 in tickets:                                # If there are usable locations start thread for the client 
            print("Waiting for connection...")  
            free_loc = np.where(tickets==0)[0][0]
            connections[free_loc], address = s.accept() # All connections are saved in a list 
            new_thread = threading.Thread(target=clientThread, args=(connections[free_loc],free_loc), daemon=True)
            new_thread.start()
            tickets[free_loc] = 1                   # Set the connection location to taken
            print("New Connetion...")
        else:                                           # If there are no location spots available, then wait
            print("...Can't take more clients...")
            print()
            time.sleep(10)

except KeyboardInterrupt:
    for k in range(len(connections)):
        if connections[k] != 0:
                connections[k].close()
        s.close()






