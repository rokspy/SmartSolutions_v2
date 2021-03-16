#!/usr/bin/python3
import threading 
import RPi.GPIO as GPIO
import socket
import time

def functionThread():
        global function_state, s, frequency
        leds = [37, 35]
        led_state = 1
        GPIO.setup(leds, GPIO.OUT)
        while True:
            if function_state == 1:
                GPIO.output(leds[0], led_state)
                led_state ^= 1
                GPIO.output(leds[1], led_state)
                time.sleep(frequency/2)
            else:
                GPIO.output(leds, 0)

            
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

function_state = 1
frequency = 1

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("localhost", 8889))

new_thread = threading.Thread(target=functionThread, args=(), daemon=True)
new_thread.start()

while True:
    try:
        data = s.recv(4096).decode()
        if data == "stop":              function_state = 0
        elif data == "start":           function_state = 1
        elif data == "state":
            if function_state == 0:     s.sendall("IS OFF".encode())
            elif function_state == 1:   s.sendall("IS ON".encode())
        elif data == "kill":            break
        else:
            try:                        frequency = float(data)
            except:                     print("No valid solution for the message") 
    except KeyboardInterrupt:
        s.close()
        GPIO.cleanup()
s.close()
GPIO.cleanup()

