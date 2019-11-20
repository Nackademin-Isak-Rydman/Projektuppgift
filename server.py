import socket 
import _thread

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_list = []

host = '127.0.0.1'
port = 12345

server.bind((host, port))
print('Sockets binded to port: ', port)
server.listen(10)
