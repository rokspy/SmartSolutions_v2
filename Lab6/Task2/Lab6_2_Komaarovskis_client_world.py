import serial

ser = serial.Serial("/dev/ttyAMA0", baudrate=9600, timeout=2)
while True:

    msg = ser.read(ser.inwaiting()).decode()
    if len(msg) != 0:
        print(msg)


