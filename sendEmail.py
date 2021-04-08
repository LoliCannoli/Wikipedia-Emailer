from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from string import Template

def sendEmail(title, summary, url, template, server):

    message = MIMEMultipart()

    message['From'] = 'DailyWikipedia dailywikipediaarticle@gmail.com'
    message['To'] = 'camsboardprofile15@gmail.com'
    message['Subject'] = 'Your daily topic is: %s ' %title



    html = open(template).read().format(Title = title, Summary = summary, URL = url) #unformatHtml.format(Title = title, Summary = summary, URL = url)
    message.attach(MIMEText(html, 'html'))
    #message.attach(MIMEText(text, 'plain'))
    server.send_message(message)
