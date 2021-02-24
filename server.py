import socket
import cryptocode
def server():
    host = "127.0.0.1"
    port = 5000
    s = socket.socket()  
    s.bind((host, port)) 
    s.listen(2)
    conn, address = s.accept() 
    print("New Connection From:" + str(address))
    while True:
        data = conn.recv(1024).decode()
        if not data:
            break
        server()