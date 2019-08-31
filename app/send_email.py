import smtplib, ssl
from config import Config
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

sender_email = Config.EMAIL_SENDER # Enter your address
password = Config.EMAIL_PW
smtp_server = "smtp.gmail.com"
port = 465  # For SSL

def send_email(to: str, message: str):
    receiver_email = to
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)

def send_html(to: str, subject:str, message_text:str):
    receiver_email = to

    message = MIMEMultipart("alternative")
    message["Subject"] = subject
    message["From"] = sender_email
    message["To"] = receiver_email

    # Turn these into plain/html MIMEText objects
    part1 = MIMEText(message_text, "plain")
    part2 = MIMEText(message_text, "html")

    # Add HTML/plain-text parts to MIMEMultipart message
    # The email client will try to render the last part first
    message.attach(part1)
    message.attach(part2)

    # Create secure connection with server and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(
            sender_email, receiver_email, message.as_string()
        )