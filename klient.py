import socket

def check_message(data):
    if len(data) > 0:
        return True
    else:
        return False
  
def Main(): 
    host = "127.0.0.1"
    port = 12345
    my_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM) 
    my_socket.connect((host,port)) 
  
    message = "Välkommen"
    while True: 
        message = input("-> ")
        my_socket.send(message.encode('utf-8')) 
        data = my_socket.recv(1024)
        true_or_false = check_message(data)
        if true_or_false:
            print("Mottaget från servern:",str(data.decode('utf-8')))
        else:
            print("Meddelandet var tomt.")

    my_socket.close() 
  
if __name__ == '__main__':
    Main() 