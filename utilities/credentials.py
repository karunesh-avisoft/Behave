from cryptography.fernet import Fernet
import os, dotenv
from utilities.test_data import TestData

dotenv.load_dotenv()

def get_fernet():
    key = os.getenv("FERNET_KEY")
    return Fernet(key.encode())

def decrypt(value: str)->str:
    return get_fernet().decrypt(value.encode()).decode()

def get_user(user_key: str):
    encrypted = TestData.ENCRYPTED_USERS
    if user_key not in encrypted:
        return None
    return decrypt(encrypted.get(user_key))

def get_passwd():
    return decrypt(TestData.ENCRYPTED_PASSWD)     