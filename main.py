from sendEmail import sendEmail
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import wikipedia
import requests
import smtplib
import os

load_dotenv()

RANDOMLINK = 'https://en.wikipedia.org/wiki/Special:Random'
EMAIL = 'dailywikipediaarticle@gmail.com'
HOST = 'smtp.gmail.com'
PORT = 587

template = 'messageTemplate.txt'

server = smtplib.SMTP( host = HOST, port = PORT)
server.starttls()
server.login(EMAIL, os.environ.get('Password'))

request = requests.get(RANDOMLINK)
content = BeautifulSoup(request.content, 'html.parser')

title, summary = None, None
while title is None and summary is None:
    try:
        title = content.find(id = 'firstHeading').text
        summary = wikipedia.summary(title)
    except:
        pass


url = 'https://en.wikipedia.org/wiki/%s' %title.replace(' ', '_')

sendEmail(title, summary, url, template, server)
