import cv2
import urllib.request
import numpy as np

url=''
cap = cv2.VideoCapture('http://172.20.10.9:81/stream')
while True:
	ret, frame = cap.read()
	#imgResp=urllib.request.urlopen(url)
	#imgNp=np.array(bytearray(imgResp.read()),dtype=np.uint8)
	#img=cv2.imdecode(imgNp,-1)
	
	#print(img)
	# all the opencv processing is done here

	cv2.namedWindow('Version 1', cv2.WINDOW_NORMAL)
	cv2.imshow('Version 1',frame)
	if ord('q')==cv2.waitKey(10):
		exit(0)

