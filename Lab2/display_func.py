#!/usr/bin/python3
import RPi.GPIO as GPIO
import threading 
import socket 
import time 
import random


def threadRoutine():
    global data, pins, digits
    local_data = "up"
    count = 0
    while True:
        time.sleep(0.5)
        if data in ["up", "down", "random"]:
            local_data = data
        if local_data == "up":
            count += 1
            if count == 10: count = 0
            GPIO.output(pins, digits[str(count)])
        elif local_data == "down":
            count -= 1
            if count == -1: count = 9
            GPIO.output(pins, digits[str(count)])
        elif local_data == "random":
            count = random.randint(0,9)
            GPIO.output(pins, digits[str(count)])

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

pins = (12,13,16,18,22,15,11) # a,b,c,d,e,f,g

digits = {'': (1,1,1,1,1,1,1),
        '1':  (1,0,0,1,1,1,1),
        '2':  (0,0,1,0,0,1,0),
        '3':  (0,0,0,0,1,1,0),
        '4':  (1,0,0,1,1,0,0),
        '5':  (0,1,0,0,1,0,0),
        '6':  (0,1,0,0,0,0,0),
        '7':  (0,0,0,1,1,1,1),
        '8':  (0,0,0,0,0,0,0),
        '9':  (0,0,0,0,1,0,0),
        '0':  (0,0,0,0,0,0,1)
        }
GPIO.setup(pins, GPIO.OUT)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("localhost", 8890))

data = "up"
new_thread = threading.Thread(target=threadRoutine, args=(), daemon = True)
new_thread.start()

while True:
    try:
       data = s.recv(4096).decode() 
       print(data)
       if not data:
            GPIO.cleanup()
            s.close()
       print(data)
       if data == "kill":
           GPIO.cleanup()
           s.close()
           break
    
    except KeyboardInterrupt:
        GPIO.cleanup(pins)
        s.close()
