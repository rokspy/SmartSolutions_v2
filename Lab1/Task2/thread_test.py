import threading 
import time

def thread_routine():
	while True:
		time.sleep(2)
		print("Was in thread")
	
if __name__ == "__main__":
	x = threading.Thread(target=thread_routine, args=(), daemon = True)
	x.start()
	time.sleep(1)
	print("Thread has been started")
	while True:
		print("Normal loop stuff")
		time.sleep(2)
