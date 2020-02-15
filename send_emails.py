import smtplib
import ssl
import authenticate.authenticate as authenticate
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def send_email(server, sender_email, receiver_email, subject, text, html, **kwargs):
    message = MIMEMultipart("alternative")
    message["Subject"] = subject
    message["From"] = sender_email
    message["To"] = receiver_email

    # Turn these into plain/html MIMEText objects
    part1 = MIMEText(text, "plain")
    part2 = MIMEText(html, "html")

    # Add HTML/plain-text parts to MIMEMultipart message
    # The email client will try to render the last part first
    message.attach(part1)
    message.attach(part2)

    print(f"Sending to: {receiver_email}")
    server.sendmail(
        sender_email, receiver_email, message.as_string()
    )
    print("Done")
