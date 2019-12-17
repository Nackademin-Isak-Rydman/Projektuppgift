import socket 
import _thread
import threading 
  
print_lock = threading.Lock() 
  
def threaded(c): 
    while True: 
        data = c.recv(1024) 
        if not data: 
            print('Hejdå') 
            print_lock.release() 
            break

        c.send(data) 
    c.close() 
  
  
def Main(): 
    host = "" 
    port = 12345
    my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    my_socket.bind((host, port)) 
    print("socket bunden till port", port) 
    my_socket.listen(5) 
    print("socket lyssnar") 
  
    while True: 
        c, addr = my_socket.accept() 
  
        print_lock.acquire() 
        print("Ansluten till: ", addr[0], ":", addr[1]) 
        _thread.start_new_thread(threaded, (c,)) 
    my_socket.close() 
  
  
if __name__ == '__main__': 
    Main() 