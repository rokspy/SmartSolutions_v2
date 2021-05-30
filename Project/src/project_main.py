import cv2
from pynput.keyboard import Listener, Key
import threading
import socket
import sys
import time


port = 8888
ip_address = "172.20.10.9"

if len(sys.argv) == 2:
		ip_address = sys.argv[1]
if len(sys.argv) == 3:
		ip_address = sys.argv[1]
		port = sys.argv[2]

key_state = "STOP"
listener = Listener()
def on_press(key):
	global key_state
	key_state = format(key)
def on_release(key):
	global key_state
	key_state = "STOP"
def KeyThread(listener):
	with Listener(on_press=on_press, on_release=on_release) as listener:
		listener.join()

def WifiThread():
	global key_state
	global esp_socket
	while True:
		if key_state == "STOP":
			message = "0"
			esp_socket.sendall(message.encode())
			esp_socket.recv(1)
		elif key_state == "Key.right":
			message = "1"
			esp_socket.sendall(message.encode())
			esp_socket.recv(1)
		elif key_state == "Key.left":
			message = "2"
			esp_socket.sendall(message.encode())
			esp_socket.recv(1)
		elif key_state == "'f'":
			message = "3"
			esp_socket.sendall(message.encode())
			esp_socket.recv(1)

esp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
esp_socket.connect((ip_address, port))

cap = cv2.VideoCapture('http://172.20.10.9:81/stream')
wifi_thread = threading.Thread(target=WifiThread, args = (), daemon = True)
cv2.namedWindow('ESP Feed', cv2.WINDOW_NORMAL)
ret, frame = cap.read()

count = 0 
while True:
	ret, frame = cap.read()
	frame = cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE)
	cv2.imshow("ESP Feed", frame)
	cv2.waitKey(10)
	if count == 0:
		count = 1
		key_listener = threading.Thread(target=KeyThread, args = (listener,), daemon=True)
		key_listener.start()	
		wifi_thread.start()
esp_socket.close()
