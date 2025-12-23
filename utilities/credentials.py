from cryptography.fernet import Fernet
from utilities.test_data import TestData as TD

def get_fernet():
    key = TD.FERNET_KEY
    return Fernet(key.encode())

def decrypt(value: str)->str:
    return get_fernet().decrypt(value.encode()).decode()

def get_user(user_key: str):
    encrypted = TD.ENCRYPTED_USERS
    if user_key not in encrypted:
        return None
    return decrypt(encrypted.get(user_key))

def get_passwd():
    return decrypt(TD.ENCRYPTED_PASSWD)     