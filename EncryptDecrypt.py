from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import os

class Encryption:
    def __init__(self, key):
        self.key = key

    def encrypt(self, data):
        iv = os.urandom(16)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        ciphertext = cipher.encrypt(pad(data.encode(), AES.block_size))
        return iv + ciphertext

    def decrypt(self, data):
        iv = data[:16]
        ciphertext = data[16:]
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)
        return plaintext.decode()

if __name__ == "__main__":
    key = os.urandom(16)
    enc = Encryption(key)
    encrypted = enc.encrypt("Secret Message")
    print("Encrypted:", encrypted)
    decrypted = enc.decrypt(encrypted)
    print("Decrypted:", decrypted)
