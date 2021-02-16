import RPi.GPIO as GPIO
import threading 
import time 
import random

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

pins = (12,13,16,18,22,15,11) # a,b,c,d,e,f,g
input_pin = 24
state = 1

def thread_routine():
    global input_pin, state
    while True:
        if GPIO.input(input_pin) == 0:
            time.sleep(0.5)
            state += 1
            if state == 4:
                state = 1
    


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
GPIO.setup(input_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

button_state = 0
count = 0

button_thread = threading.Thread(target=thread_routine, args=(), daemon = True)
button_thread.start()
try:
    while True:
        if state == 1:
            count += 1
        elif state == 2:
            count -= 1     
        elif state == 3:
            count = random.randint(0,9) 


        if count == 10:     count = 0
        elif count == -1:   count = 9

        GPIO.output(pins, digits[str(count)])
        time.sleep(0.5)
except KeyboardInterrupt:
    GPIO.cleanup(pins)
