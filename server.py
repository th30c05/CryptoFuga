import socket
from json import loads
from base64 import b64decode, decodebytes
from Cryptodome.Cipher import AES

host = 'local host'
port = 5000

s = socket.socket(socket.AF_INET,
                  socket.SOCK_STREAM)

s.connect(('127.0.0.1', port))

msg = s.recv(1024)

Bytes_File = open("key", "rb")
key = bytes(Bytes_File.read())
Bytes_File.close()

while msg:
    json_input = decodebytes(msg)
    b64 = loads(json_input)

    json_k = ['nonce', 'header', 'ciphertext', 'tag']
    jv = {k: b64decode(b64[k]) for k in json_k}

    cipher = AES.new(key, AES.MODE_SIV, nonce=jv['nonce'])
    cipher.update(jv['header'])

    plaintext = cipher.decrypt_and_verify(jv['ciphertext'], jv['tag'])

    print('Recived:' + plaintext.decode("utf-8"))
    msg = s.recv(1024)

s.close()