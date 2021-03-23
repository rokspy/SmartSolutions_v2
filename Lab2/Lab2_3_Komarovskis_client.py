import socket 
import threading 
import time
import sys

def listenThread():
        global s, thread_lost
        while True:
            data = s.recv(4096).decode()
            if not data:
                thread_lost = 1
                s.close()
                break
            print(data)

ip_address = "localhost"
port = 8888

if len(sys.argv) == 2:
    ip_address = sys.argv[1]
elif len(sys.argv) == 3:
    ip_address = sys.argv[1]
    port = int(sys.argv[2])


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((ip_address, port))
thread_lost = 0

listen_thread = threading.Thread(target=listenThread, daemon=True)
listen_thread.start()

try:
    while True:
        send_msg = input("Send data: ")
        s.sendall(send_msg.encode())
        time.sleep(0.5)
        if send_msg == "kill":
            s.close()
            break
        if thread_lost == 1:
            s.close()
            break
except KeyboardInterrupt:
    s.close()
    print("Thats it")

