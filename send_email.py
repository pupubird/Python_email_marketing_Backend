import smtplib
import ssl
import csv
import getpass
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

sender_email = input("Your email: ")
password = getpass.getpass("Type your password and press enter:")
input("Save the template email into template.txt, press enter to continue...")
input("Save the target emails and data into targets.csv, press enter to continue...")

receiver_emails = []
links = []
first_names = []
with open('target_emails.csv', 'r') as f:
    csv_reader = csv.reader(f)

    for row in csv_reader:
        receiver_emails.append(row[0])
        first_name = row[1].split(" ")[0]
        first_names.append(first_name)
        links.append(row[2])

# Create secure connection with server and send email
context = ssl.create_default_context()
subject = "STC WordPress Workshop | Generated Wpsandbox Link"
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    print("Starting server")
    server.login(sender_email, password)
    print("Logged in")
    for i in range(len(receiver_emails)):
        message = MIMEMultipart("alternative")
        message["Subject"] = subject
        message["From"] = sender_email
        message["To"] = receiver_emails[i]

        # Create the plain-text and HTML version of your message
        text = ""

        html = ""

        # Turn these into plain/html MIMEText objects
        part1 = MIMEText(text, "plain")
        part2 = MIMEText(html, "html")

        # Add HTML/plain-text parts to MIMEMultipart message
        # The email client will try to render the last part first
        message.attach(part1)
        message.attach(part2)

        print(f"Sending to: {receiver_emails[i]}")
        server.sendmail(
            sender_email, receiver_emails[i], message.as_string()
        )
print("Done")
