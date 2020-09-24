from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes


def Bytes_Gen(Bytes):
    Bytes = get_random_bytes(Bytes)
    return Bytes



def Key_Loader(File_Name):
    key_file = open(File_Name, "rb")
    key = key_file.read()
    key_file.close()
    return key


def Key_Save(Key):
    key_file = open("key", "wb")
    key_file.write(Key)
    key_file.close()


def Data_Load(File_Name):
    data_file = open(File_Name, "rb")
    data = data_file.read()
    data_file.close()
    return data


def Data_Encrypt(Data, Key):
    Cipher = AES.new(Key, AES.MODE_EAX)
    Ciphertext, tag = Cipher.encrypt_and_digest(Data)
    Cipher = [Cipher, Ciphertext, tag]
    return Cipher


def Data_Encrypt_Save(Cipher, File_Name):
    file_out = open(File_Name, "wb")
    [file_out.write(x) for x in (Cipher[0].nonce, Cipher[2], Cipher[1])]
    file_out.close()


def Encrypted_Load(File_Name, Key):
    data_encrypted = open(File_Name, "rb")
    nonce, tag, Ciphertext = [data_encrypted.read(x) for x in (16, 16, -1)]
    Cipher = AES.new(Key, AES.MODE_EAX, nonce)
    Cipher = [Cipher, Ciphertext, tag]
    return Cipher


def Data_Decrypt(Cipher):
    data = Cipher.decrypt_and_verify(Cipher[1], Cipher[2])
    return data
