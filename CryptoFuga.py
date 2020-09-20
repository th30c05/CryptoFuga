from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes


def Key_Generator(Bytes):
    key = get_random_bytes(Bytes)
    return key


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
    cipher = AES.new(Key, AES.MODE_EAX)
    ciphertext, tag = cipher.encrypt_and_digest(Data)
    cipher = [cipher, ciphertext, tag]
    return cipher


def Data_Encrypt_Save(Cipher, File_Name):
    file_out = open(File_Name, "wb")
    [file_out.write(x) for x in (Cipher[0].nonce, Cipher[2], Cipher[1])]
    file_out.close()


def Encrypted_Load(Name, Key):
    data_encrypted = open(Name, "rb")
    nonce, tag, ciphertext = [data_encrypted.read(x) for x in (16, 16, -1)]
    cipher = AES.new(Key, AES.MODE_EAX, nonce)
    cipher = [cipher, ciphertext, tag]
    return cipher


def Data_Decrypt(cipher):
    data = cipher.decrypt_and_verify(cipher[1], cipher[2])
    return data
