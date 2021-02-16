import RPi.GPIO as GPIO
import time 

GPIO.setmode(GPIO.BOARD)

mode = GPIO.getmode()
GPIO.setwarnings(False)

led_pin1 = 11
led_pin2 = 13
led_state1 = 0
led_state2 =1 

GPIO.setup(led_pin1, GPIO.OUT, initial=0)
GPIO.setup(led_pin2, GPIO.OUT, initial=0)

try:
    while True:
        led_state1 ^= 1
        led_state2 ^= 1
        GPIO.output(led_pin1, led_state1)
        GPIO.output(led_pin2, led_state2)
        time.sleep(0.5)
except KeyboardInterrupt:
    GPIO.cleanup((led_pin1,led_pin2))
