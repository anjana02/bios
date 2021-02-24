import socket
import cryptocode
def client():
    host = "127.0.0.1"
    port = 5002
    client_socket = socket.socket()
    client_socket.connect((host, port))
    message = input("Input:: ")
    while message.lower().strip() != 'end':
        message = cryptocode.encrypt(message, "mysecret")
        client_socket.send(message.encode())
        data = client_socket.recv(1024).decode()
        data = cryptocode.decrypt(message, "mysecret")
        print('Server message: ' + data)
        message = input(" >")
    client_socket.close()
if __name__ == '__main__':
    client()