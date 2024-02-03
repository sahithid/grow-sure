from smtplib import SMTP
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

SMTP_HOST = "localhost"
SMTP_PORT = 1025
SENDER_EMAIL = "21f1003337@ds.study.iitm.ac.in"
SENDER_PASSWORD = "1234"


def send_email(to, subject, body):
    message = MIMEMultipart()
    message["To"] = to
    message["From"] = SENDER_EMAIL
    message["Subject"] = subject
    message.attach(MIMEText(body,'html'))
    smtp_client = SMTP(host=SMTP_HOST, port=SMTP_PORT)
    smtp_client.send_message(msg=message)
    smtp_client.quit()