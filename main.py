from sendEmail import sendEmail
from bs4 import BeautifulSoup
from cryptography.fernet import Fernet
import emailStorage
import wikipedia
import requests



#Important Variables
RANDOMLINK = 'https://en.wikipedia.org/wiki/Special:Random'
TEMPLATE = 'WikiTemplate.html'

#Setup Database
import sqlite3

database = sqlite3.connect('emails.db')

#Load in .env
from dotenv import load_dotenv
import os

load_dotenv()

def main(database):
    import time

    cursor = database.cursor()
    cursor.execute('SELECT * FROM emails')

    for row in cursor:
        startTime = time.time()
        row = str(row).split('\'')[1]
        row = row.encode()


        email = emailStorage.Email(row)
        email.decryption(Fernet((os.environ.get('Key').split('\'')[1]).encode()))

        adress = email.email

        title, summary = None, None
        while title is None and summary is None:
            try:
                request = requests.get(RANDOMLINK)
                content = BeautifulSoup(request.content, 'html.parser')
                title = content.find(id = 'firstHeading').text
                summary = wikipedia.summary(title)
            except:
                pass

        url = 'https://en.wikipedia.org/wiki/%s' %title.replace(' ', '_')

        print('Email took: ', time.time()- startTime)

        sendEmail(title, summary, url, TEMPLATE, adress)
main(database)
