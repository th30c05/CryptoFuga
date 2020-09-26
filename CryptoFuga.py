from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

def Bytes_Gen(Bytes):
    Bytes = bytes(get_random_bytes(Bytes))
    return Bytes


def Bytes_Load(File_Name):
    Bytes_File = open(File_Name, "rb")
    Bytes = bytes(Bytes_File.read())
    Bytes_File.close()
    return bytes(Bytes)


def Bytes_Save(Bytes, File_Name):
    Bytes_File = open(File_Name, "wb")
    Bytes_File.write(bytes(Bytes))
    Bytes_File.close()


def Cipher_Gen(Key, IV):
    Cipher = AES.new(bytes(Key), AES.MODE_EAX, bytes(IV))
    return Cipher


def Data_Encrypt(Cipher, Data):
    Encrypt = Cipher.encrypt_and_digest(Data)
    return Encrypt


def Data_Decrypt(Cipher, Data):
    Decrypt = Cipher.decrypt_and_verify(Data)
    return Decrypt
