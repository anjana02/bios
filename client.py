import socket
import cryptocode
import hmac
import hashlib
digest_maker = hmac.new(b'secret-key', b'msg', hashlib.sha1)
print ("Hexdigest: " + digest_maker.hexdigest())
digest_maker.update(b'another msg')
print ("Hexdigest after update: " + digest_maker.hexdigest())
print ("Digest size: " + str(digest_maker.digest_size) + " bytes")
print ("Block size: " + str(digest_maker.block_size) + " bytes")
print ("Canonical name: " + digest_maker.name)
print ("Digest: ", end =" ")
print (digest_maker.digest())
digest_clone = digest_maker.copy()
print ("Hexdigest of clone: " + digest_clone.hexdigest())
def client():
    host = "127.0.0.1"
    port = 5001
    c = socket.socket()
    c.connect((host, port))
    message = input("Input:: ")
    while message.lower().strip() != 'end':
        message = cryptocode.encrypt(message, "mysecret")
        c.send(message.encode())
        data = c.recv(1024).decode()
        data = cryptocode.decrypt(message, "mysecret")
        print('Server message: ' + data)
        message = input(" >")
    c.close()
if __name__ == '__main__':
    client()
