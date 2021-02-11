import RPi.GPIO as GPIO
import time 

GPIO.setmode(GPIO.BOARD)

mode = GPIO.getmode()
GPIO.setwarnings(False)

led_pin1 = 11
led_state1 = 0

GPIO.setup(led_pin1, GPIO.OUT, initial=0)

try:
    while True:
        led_state1 ^= 1
        GPIO.output(led_pin1, led_state1)
        time.sleep(0.5)
except KeyboardInterrupt:
    GPIO.cleanup((led_pin1,led_pin2))
