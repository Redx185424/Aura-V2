import base64
import hashlib
from cryptography.fernet import Fernet

def derive_key(password: str) -> bytes:
    return base64.urlsafe_b64encode(hashlib.sha256(password.encode()).digest())

def create_encrypted_key_file(password: str):
    base_key = Fernet.generate_key()
    fernet = Fernet(derive_key(password))
    encrypted_key = fernet.encrypt(base_key)
    with open("redx_key_protected.key", "wb") as f:
        f.write(encrypted_key)
    print("Encrypted memory key generated and saved as 'redx_key_protected.key'.")

if __name__ == "__main__":
    pw = input("Set a password for Redx Mode:redxalpha ")
    create_encrypted_key_file(pw)