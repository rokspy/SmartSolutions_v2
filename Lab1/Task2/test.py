#import RPi.GPIO as GPIO
import time 
import threading 

#GPIO.setmode(GPIO.BOARD)

#mode = GPIO.getmode()
#GPIO.setwarnings(False)

def thread_routine(button_change):
	#button_change = 0
	#direction ^= 1
	print("Was Here")
	time.sleep(0.5)


pins = (12,13,16,18,22,15,11) # a,b,c,d,e,f,g
input_pin = 24
direction = 0

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

#GPIO.setup(pins, GPIO.OUT)
#GPIO.setup(input_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

button_state = 0
count = 0

if __name__ == "__main__":

	x = threading.Thread(target=thread_routine, args=(1,))
	try:
		while True:
			if direction == 0: 	count += 1
			else:			count -= 1 			
	except KeyboardInterrupt:
		print("\n\nExiting")	

