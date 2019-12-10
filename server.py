import socket 
import _thread
import threading

print_lock = threading.Lock()

def if_threaded(c):

    while True:
        data = c.recv(1024)
        if not data:
            print("Hejdå")
            print_lock.release()
            break

        data = data[::-1]
        c.send(data)

    c.close()

host = ""
port = 12345
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((host, port))
print("socket bunden till port", port)

sock.listen(4)

