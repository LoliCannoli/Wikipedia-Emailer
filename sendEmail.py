from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from string import Template

def readTemplate(file):
    with open(file, 'r', encoding = 'utf-8') as templateFile:
        templateContent = templateFile.read()
    return Template(templateContent)

def sendEmail(title, summary, url, template, server):

    messageTemplate = readTemplate(template)

    message = MIMEMultipart()

    message['From'] = 'DailyWikipedia dailywikipediaarticle@gmail.com'
    message['To'] = 'damerowij@gmail.com'
    message['Subject'] = 'Your daily topic is: %s ' %title

    unformatHtml = '''\
    <html>
        <head></head>
        <body>
            <h2 style="text-align: center;">{Title}</h2>
            <p style="text-align: center;">{Summary}</p>

            <footer>
                <p style="text-align: center;">If you wish to continue reading this article, go to: {URL}</p>
            </footer>
        </body>

    </html>
    '''

    html = unformatHtml.format(Title = title, Summary = summary, URL = url)
    message.attach(MIMEText(html, 'html'))
    #message.attach(MIMEText(text, 'plain'))
    server.send_message(message)
