import socket 
import threading 
import time

def listenThread():
        global s, thread_lost
        while True:
            data = s.recv(4096).decode()
            if not data:
                thread_lost = 1
                s.close()
                break
            print(data)


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("localhost", 8888))
thread_lost = 0

listen_thread = threading.Thread(target=listenThread, daemon=True)
listen_thread.start()

try:
    while True:
        send_msg = input("Send data: ")
        s.sendall(send_msg.encode())
        if send_msg == "kill":
            s.close()
            break
        if thread_lost == 1:
            s.close()
            break
except KeyboardInterrupt:
    s.close()
    print("Thats it")

