import socket
import threading 
import sys
import time 
import RPi.GPIO as GPIO

### FUNCTIONS ###

def LEDThread():
    #GPIO.output(led)
    global led_talk, LED_func_status
    local_state = None 
    leds = 1
    switching = 1
    freq = 1
    falsh_state = 1
    while True:
        if led_talk == "close" or len(led_talk) == 0:
            GPIO.output((led_pin1, led_pin2), 0)
            break
        if local_state != led_talk:
            print(led_talk)
            local_state = led_talk
            if led_talk=="off":
                leds = 0
            elif led_talk == "on":
                leds = 1
            else:
                try:
                    if float(led_talk) < 2:
                        freq = float(led_talk)
                except:
                    print("No valid use")
        if leds == 1:
           GPIO.output(led_pin1, switching)
           switching ^= 1
           GPIO.output(led_pin2, switching)
           time.sleep(freq)
        else:
            GPIO.output((led_pin1, led_pin2), 0)
    LED_func_status = 0


def clientThread(connection):
        global led_talk
        print("New Connection established")
        global LED_func_status, Display_func_status
        connection.send("\n\nWelcome to my server ".encode())   
        
        local_state = "none"
        
        data = connection.recv(4096).decode()
    
        if data == "LED" and LED_func_status == 0:
            led_thread.start()
            LED_func_status = 1
            while True:
                if LED_func_status == 0:
                    print("I see that it goes to zero")
                    break
                led_talk = connection.recv(4096).decode()


        elif data == "Display":
            print("Display stuff")

        else:
            connection.sendall("No valid function or the function is taken".encode())

        connection.close()
        print("Connection Closed")


### RASPI GPIO SETUP
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

led_pin1 = 11
led_pin2 = 13
led_state1 = 0
led_state2 =1 

GPIO.setup(led_pin1, GPIO.OUT, initial=0)
GPIO.setup(led_pin2, GPIO.OUT, initial=0)

LED_func_status = 0
Display_func_status = 0
flash_toggle = 1

led_talk = "on"
led_thread = threading.Thread(target=LEDThread, args = (), daemon=False)

### MAIN CODE ####

port = 8888 
host = "localhost"
IP_addr = socket.gethostbyname(host)

if len(sys.argv) == 2:
        IP_addr = sys.argv[1]
elif len(sys.argv) == 3:
        IP_addr = sys.argv[1]
        port = int(sys.argv[2])

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((IP_addr, port))
print("IP_address: " + IP_addr)
print("Port: " + str(port) + "\n")
s.listen(10)                    # Number of possible connections


try:
        while True:
                print("Waiting for conncetion...")
                connection, address = s.accept()
                print("New connection...")
                                

                new_thread = threading.Thread(target=clientThread, args = (connection,), daemon=True)
                new_thread.start()
except KeyboardInterrupt:
        time.sleep(0.1)
        print("Socket closed")
        GPIO.cleanup()
        s.close()       

