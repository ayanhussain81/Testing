from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
import random
from datetime import datetime
import smtplib, ssl
import sys

 
now = datetime.now()
num = random.randint(1, 101)
with open('/tmp/rand.txt', 'a') as f:
    f.write('{} - Your random number is {}\n'.format(now, num)) 
def emailnew():
    sender_email = "ayanhussain821@gmail.com" 
    receiver_email = "ayanhussain746@gmail.com"
    password = 'hxhzadjpltglkift'
    message = MIMEMultipart("alternative")
    message["Subject"] = "Testting"
    message["From"] = sender_email
    message["To"] = receiver_email

    text = """\
    New stuff in today!"""
#     html = df.to_html(index=False)
    part1 = MIMEText(text, "plain")
#     part2 = MIMEText(html, "html")

    message.attach(part1)
#     message.attach(part2)


    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(
            sender_email, receiver_email, message.as_string()
        )

emailnew()
