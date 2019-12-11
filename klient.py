import socket

host = "127.0.0.1"
port = 12345

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((host, port))

while True:
    data = sock.recv(1024)
    print("mottaget meddelande: ", str(data.decode('ascii')))

    ans = input('fortsätt? ja/nej:')
    if ans == "y":
        continue
    else:
        break
sock.close()