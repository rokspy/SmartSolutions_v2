import serial
import matplotlib.pyplot as plt
import neopixel
import threading 
import sys
import time
import board

def threadRoutine(ser):
    time_count = 0
    the_time = []
    temp = []

    while True:
        msg = ser.read(5).decode()
        try:
            print(msg)
            led_set(float(msg))
            writeFile(msg)


        except: continue
        the_time.append(time_count)
        temp.append(msg)         
        plt.plot(the_time, temp, 'b')
        plt.grid()
        plt.pause(0.001)
        plt.grid()
        time_count += 1    


def writeFile(data):
    f = open("temperature.txt", "w")
    f.write(str(data)+"\n")
    f.close()

def led_set(rx_data):
    global pixels
    # Range is from 0 to 1023
    if rx_data > 18 and rx_data < 35:
        rx_data = (rx_data-18)*60
        red = rx_data * 255/1023
        blue = 255 - red
        pixels[0] = (red, 0, blue)

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
        time.sleep(1)
        ser.write("9".encode())
    except KeyboardInterrupt:
        ser.close()
        pixels[0] = (0,0,0)
        
