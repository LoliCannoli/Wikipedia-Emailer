import requests
from bs4 import BeautifulSoup
import wikipedia
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from string import Template

from dotenv import load_dotenv
load_dotenv()

randomLink = 'https://en.wikipedia.org/wiki/Special:Random'

request = requests.get(randomLink)
content = BeautifulSoup(request.content, 'html.parser')

title = content.find(id = 'firstHeading').text
summary = wikipedia.summary(title)

url = 'https://en.wikipedia.org/wiki/%s ' %title

server = smtplib.SMTP( host = 'smtp.gmail.com', port = 587)
server.starttls()
server.login('dailywikipediaarticle@gmail.com', os.environ.get('Password'))


messageTemplateFile = open('messageTemplate.txt', 'r')
messageTemplate = messageTemplateFile.read()

message = MIMEMultipart()

message['From'] = 'DailyWikipedia dailywikipediaarticle@gmail.com'
message['To'] = 'camsboardprofile15@gmail.com'
message['Subject'] = 'Your daily topic is: %s ' %title

message.attach(MIMEText(messageTemplate, 'plain'))

server.send_message(message)
