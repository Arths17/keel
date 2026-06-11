from cryptography.fernet import Fernet

print(Fernet.generate_key())

#ciph = Fernet(key.encode())