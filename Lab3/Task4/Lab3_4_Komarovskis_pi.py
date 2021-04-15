import serial
import threading 
import sys
import time
import busio

import I2C_LCD_driver
#https://www.circuitbasics.com/raspberry-pi-i2c-lcd-set-up-and-programming/

import RPi.GPIO as GPIO
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

mylcd = I2C_LCD_driver.lcd()

while True:
    msg = float(ser.read(5).decode())/1000
    msg = str(msg)
    print(msg)
    mylcd.lcd_display_string("Voltage,V: "+msg, 1)


