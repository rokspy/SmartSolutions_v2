import cv2
import urllib.request
import matplotlib.pyplot as plt
import numpy as np
import threading
import time 


def timerThread():
	global frame, background 
	flash = True
	while True:
		if np.mean(frame) > np.mean(background)+5:
			flash = True 
			print(flash)
		if np.mean(frame) < np.mean(background)-5:
			flash = False	
			print(flash)
						

cap = cv2.VideoCapture('http://172.20.10.9:81/stream')
cv2.namedWindow('Video Feed', cv2.WINDOW_NORMAL)
frame = np.zeros(10)
background = np.zeros(10)
timer_thread = threading.Thread(target=timerThread, daemon=True)

initial_count = 0

while(True):
	
	ret, frame = cap.read()
	if initial_count <11:
		initial_count += 1
	if initial_count == 10:
		timer_thread.start()	

	
	background = np.roll(background,1)
	background[0] = np.mean(frame)	

	cv2.imshow('Video Feed',frame)
	if ord('q')==cv2.waitKey(10):
		exit(0)

