import serial
import threading
import RPi.GPIO as GPIO

def threadRoutine(ser):
    while True:
        msg = ser.read().decode()
        if msg!="":
            if msg=="1":
                print("LED is ON")
            elif msg=="0":
                print("LED is OFF")

ser = serial.Serial()
ser.baudrate = 9600
ser.port = '/dev/ttyAMA0'
ser.timeout = 2
ser.open()

new_thread = threading.Thread(target=threadRoutine, args = (ser,), daemon=True)
new_thread.start()

while True:
    try:
        msg = input("Send: ")
        ser.write(msg.encode())
    except KeyboardInterrupt:
        ser.close()
        GPIO.cleanup()
