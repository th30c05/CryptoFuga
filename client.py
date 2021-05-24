import socket
from json import dumps
from base64 import b64encode
from Cryptodome.Cipher import AES
from Cryptodome.Random import get_random_bytes

# take the server name and port name
host = 'local host'
port = 5000

# create a socket at server side
# using TCP / IP protocol
s = socket.socket(socket.AF_INET,
                  socket.SOCK_STREAM)

# bind the socket with server
# and port number
s.bind(('', port))

# allow maximum 1 connection to
# the socket
s.listen(1)

# wait till a client accept
# connection
c, addr = s.accept()

# display client address
print("CONNECTION FROM:", str(addr))
key = get_random_bytes(32 * 2)
print(key)
Bytes_File = open("key", "wb")
Bytes_File.write(bytes(key))
Bytes_File.close()

# send message to the client after
# encoding into binary string
while True:
    msg = input("Dale Wacho: ")

    header = b"@author th30c05"
    nonce = get_random_bytes(64)

    cipher = AES.new(key, AES.MODE_SIV, nonce=nonce)
    cipher.update(header)
    ciphertext, tag = cipher.encrypt_and_digest(bytes(msg, "utf-8"))

    json_k = ['nonce', 'header', 'ciphertext', 'tag']
    json_v = [b64encode(x).decode('utf-8') for x in (nonce, header, ciphertext, tag)]

    result = dumps(dict(zip(json_k, json_v)))
    result = b64encode(result.encode("utf-8"))

    c.send(result)
# disconnect the server
c.close()