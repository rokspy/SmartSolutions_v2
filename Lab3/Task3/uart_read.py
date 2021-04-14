import serial
import neopixel
import threading 
import sys
import time
import board

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
ser.port = '/dev/serial0'
ser.timeout = 1
ser.write_timeout = 1
ser.open()

pixels = neopixel.NeoPixel(board.D18,1)   # GPIO1, 12 pin on the board
pixels[0] = (0,0,0) 



new_thread = threading.Thread(target=threadRoutine, args = (ser,), daemon=True)
new_thread.start()
while True:
        try:
            msg =input("Send message: ")
            ser.write(msg.encode())
        except KeyboardInterrupt: 
                ser.close()
                print('...Exit command')
                sys.exit()
        read_serial = ''

