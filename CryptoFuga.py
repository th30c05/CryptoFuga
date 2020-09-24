from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes


def Bytes_Gen(Bytes):
    Bytes = get_random_bytes(Bytes)
    return Bytes


def Bytes_Load(File_Name):
    Bytes_File = open(File_Name, "rb")
    Bytes = Bytes_File.read()
    Bytes_File.close()
    return Bytes


def Bytes_Save(Bytes, File_Name):
    Bytes_File = open(File_Name, "wb")
    Bytes_File.write(Bytes)
    Bytes_File.close()


def Cipher_Gen(Key, IV):
    Cipher = AES.new(Key, AES.MODE_EAX, IV)
    return Cipher


def Data_Encrypt(Cipher, Data):
    Encrypt = Cipher.encrypt_and_digest(Data)
    return Encrypt


def Encrypted_Load(File_Name, Key):
    data_encrypted = open(File_Name, "rb")
    nonce, tag, Ciphertext = [data_encrypted.read(x) for x in (16, 16, -1)]
    Cipher = AES.new(Key, AES.MODE_EAX, nonce)
    Cipher = [Cipher, Ciphertext, tag]
    return Cipher


def Data_Decrypt(Cipher):
    data = Cipher.decrypt_and_verify(Cipher[1], Cipher[2])
    return data
