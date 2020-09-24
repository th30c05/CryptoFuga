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


def Data_Decrypt(Cipher, Data):
    Decrypt = Cipher.decrypt_and_verify(Data)
    return Decrypt
