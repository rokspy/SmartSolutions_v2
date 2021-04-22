import serial
import time
import threading
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

led_pin = 40
GPIO.setup(led_pin, GPIO.OUT)

ser = serial.Serial()
ser.baudrate = 9600
ser.port = '/dev/ttyS0'
ser.timeout = 1
ser.open()

LED_pin = 40

print()

while True:
    try:

        msg = ser.read(10).decode()[0:-1]
        #msg = ser.read(10).decode()
        if msg!="":
            if msg=="1":
                GPIO.output(led_pin, 1)
                print("LED is ON")
                message = 'ON'.encode()
                ser.write(message)
                ser.write(10)
                time.sleep(1)
            elif msg=="0":
                GPIO.output(led_pin, 0)
                print('LED is OFF')
                message = 'OFF'.encode()
                ser.write(message)
                ser.write(10)
                time.sleep(1)
    except KeyboardInterrupt:
        ser.close()
        GPIO.cleanup()
