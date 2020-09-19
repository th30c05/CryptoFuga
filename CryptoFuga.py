from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes


def Key_Generator(Bytes):
    key: bytes = get_random_bytes(Bytes)
    return key


    def Key_Loader(self, Name):
        key_file = open(Name, "rb")
        self.key = key_file.read()
        key_file.close()
        return self.key

    def Key_Save(self):
        key_file = open("key", "wb")
        key_file.write(self.key)
        key_file.close()
