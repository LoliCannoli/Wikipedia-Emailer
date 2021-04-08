import sqlite3
import bcrypt
from dotenv import load_dotenv
import os

load_dotenv()

from cryptography.fernet import Fernet

class Email():

    def __init__(self, email):
        self.email = email

    def encryption(self, key):
        encodedEmail = self.email.encode()
        encrypted = key.encrypt(encodedEmail)
        self.email = str(encrypted).split('\'')[1]

    def decryption(self, key):
        decrypted = key.decrypt(self.email)
        decrypted = (str(decrypted)).split('\'')[1]
        self.email = decrypted
