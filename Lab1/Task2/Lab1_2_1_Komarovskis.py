import RPi.GPIO as GPIO
import time 

GPIO.setmode(GPIO.BOARD)

mode = GPIO.getmode()
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
try:
    while True:
        for k in range(10):
            GPIO.output(pins, digits[str(k)])
            time.sleep(0.5)
except KeyboardInterrupt:
    GPIO.cleanup(pins)
