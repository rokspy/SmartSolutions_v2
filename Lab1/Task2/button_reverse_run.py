import RPi.GPIO as GPIO
import time 

GPIO.setmode(GPIO.BOARD)

mode = GPIO.getmode()
GPIO.setwarnings(False)

pins = (12,13,16,18,22,15,11) # a,b,c,d,e,f,g
input_pin = 24

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

while True:
    if GPIO.input(input_pin) == 0: button_state ^= 1
    if button_state == 1:   count += 1
    else:                   count -= 1
    if count == 10:         count = 0
    elif count == -1:       count = 9

    print(count)
    GPIO.output(pins, digits[str(count)])
    time.sleep(0.5)

GPIO.cleanup(pins)
