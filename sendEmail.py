from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def sendEmail(title, summary, url, template, adress):

    #Setting up email server
    import smtplib
    from dotenv import load_dotenv
    import os

    load_dotenv()

    EMAIL = 'dailywikipediaarticle@gmail.com'
    HOST = 'smtp.gmail.com'
    PORT = 587

    server = smtplib.SMTP( host = HOST, port = PORT)
    server.starttls()
    server.login(EMAIL, os.environ.get('EmailPassword'))

    #Assemble MetaData
    message = MIMEMultipart()

    message['From'] = 'DailyWikipedia dailywikipediaarticle@gmail.com'
    message['To'] = adress
    message['Subject'] = 'Your daily topic is: %s ' %title

    #Assemble and send Message
    html = open(template).read().format(Title = title,
                                        Summary = summary,
                                        URL = url)
    message.attach(MIMEText(html, 'html'))
    server.send_message(message)
