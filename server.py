import socket
import cryptocode
import hmac
import hashlib
digest_maker = hmac.new(b'secret-key', b'msg', hashlib.sha512)
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
def server():
    host = "127.0.0.1"
    port = 5001
    s = socket.socket()    
    s.bind((host, port))  
    s.listen(2)
    conn, address = s.accept()
    print("New Connection From:" + str(address))
    while True:    
        data = conn.recv(1024).decode()
        if not data:      
            break
        data = str(data)
        data = cryptocode.decrypt(data, "mysecret")
        print("User: " + str(data))
        data = input('>')
        data = cryptocode.encrypt(data, "mysecret")
        conn.send(data.encode()) 
    conn.close()
if __name__ == '__main__':
    server()
