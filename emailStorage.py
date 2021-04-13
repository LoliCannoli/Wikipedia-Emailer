from cryptography.fernet import Fernet
import sqlite3
import dotenv
import os

dotenv.load_dotenv()

#Setting up database
database = sqlite3.connect('emails.db')
cursor = database.cursor()

#Try to make table unless table already exist
try:
    cursor.execute('CREATE TABLE emails (email text)')
except sqlite3.OperationalError:
    pass

class Email():

    def __init__(self, email, ishashed = False):
        self.email = email
        self.ishashed = ishashed

    def encryption(self, key):
        #Convert to bytes and encrypt
        encodedEmail = self.email.encode()
        encrypted = key.encrypt(encodedEmail)
        self.email = str(encrypted).split('\'')[1]
        self.hashed = True

    def decryption(self, key):
        #Decrypt and convert to string
        decrypted = key.decrypt(self.email)
        decrypted = (str(decrypted)).split('\'')[1]
        self.email = decrypted
        self.hashed = False

    def storeEmail(self):
        #If not hashed hashed then try to insert in database
        if self.ishashed == False:
            self.encryption(Fernet((os.environ.get('Key').split('\'')[1]).encode()))
        try:
            cursor.execute("INSERT INTO emails VALUES (?)", (self.email,))
            database.commit()
        except:
            print('An error occured during the commit to the database')
