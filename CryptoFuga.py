from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes


def Key_Generator(Bytes):
    key = get_random_bytes(Bytes)
    return key
