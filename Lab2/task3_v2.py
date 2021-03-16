import threading
import socket
import numpy as np
import time
import subprocess
import RPi.GPIO as GPIO

def clientThread(connection, connection_index):
        global tickets, led_taken, display_taken
        led_started = 0
        display_started = 0
        connection.send("\n\nWelcome to my server ".encode())
        try:
            while True:
                # Wait for data fromt the client
                        data = connection.recv(4096).decode()
                        # Check if data valid, if not run kill routine 
                        if not data:
                            connection.close()
                            tickets[connection_index] = 0
                            try:    function_socket.close()
                            except: continue
                            if led_started == 1:
                                led_taken=0
                                led_func.kill()
                            break

                        if led_started == 1:
                            try:
                                function_connection.sendall(data.encode())
                            except:
                                print("No connection to the function")
                                led_taken = 0
                                function_socket.close()
                                led_func.kill()
                                break
                        elif display_started == 1:
                            try:
                                function_connection.sendall(data.encode())
                            except:
                                print("No connection to the function")
                                display_taken = 0
                                function_socket.close()
                                display_func.kill()
                                break
                        elif data == "LED":
                            function_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                            function_socket.bind(("localhost",8889))
                            function_socket.listen(2)
                            led_func = subprocess.Popen("./led_func.py")
                            function_connection,_ = function_socket.accept()
                            led_taken = 1       # Tells globally that the function is taken 
                            led_started = 1     # For memorising which function is being taken in this thread
                        elif data == "DISPLAY":
                            function_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                            function_socket.bind(("localhost",8890))
                            function_socket.listen(2)
                            display_func = subprocess.Popen("./display_func.py")
                            function_connection,_ = function_socket.accept()
                            display_taken = 1       # Tells globally that the function is taken 
                            display_started = 1     # For memorising which function is being taken in this thread


        except KeyboardInterrupt:
            print("Kill connection")
            connection.close()
            try:    
                    function_socket.close()
                    if led_started == 1:
                        led_taken=0
                        led_func.kill()
                    elif display_started == 1:      display_taken = 0
            except:pass 


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






