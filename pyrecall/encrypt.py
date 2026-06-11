from cryptography.fernet import Fernet
from dotenv import load_dotenv
import os


class Encryptor:
    def __init__(self):
        load_dotenv()
        self.key = os.getenv("ENCRYPT_KEY")
        
        if self.key is None:
            raise ValueError("ENCRYPTION KEY WAS NOT FOUND, MAKE SURE YOU HAVE SET YOUR KEY IN YOUR .env FILE")
        
        self.cipher = Fernet(self.key.encode())

    def encrypt(self, text: str) -> str:
        data = self.cipher.encrypt(text.encode())
        return data.decode()
    def decrypt(self, encrypted_text: str) -> str:
        data_decrypted = self.cipher.decrypt(encrypted_text.encode())
        return data_decrypted.decode()
