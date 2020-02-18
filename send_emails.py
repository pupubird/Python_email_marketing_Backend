import smtplib
import ssl
import tornado
import base64
import authenticate
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class sendEmailsHandler(tornado.web.RequestHandler):
    def post(self):
        config = authenticate.Config.getInstance()
        server = config.Server
        sender_email = config.Email

        if not sender_email:
            self.write('<h1> Unauthenticated action </h1>')
            return

        if self.request.files.get('media', False):
            media = self.handling_media()

        subject = self.get_body_argument('subject_field')
        text = self.get_body_argument('content_field')

        # While yielding

        send_email(server, sender_email,
                   'frankeyc777@gmail.com', subject, text, text)
        self.write(
            'Check email! <a href="/">Click here to return to home page</a>')

    def csv_file(self):
        # open the csv file, save in self
        pass

    def get_csv_column(self):
        # get csv column header
        pass

    def row_generator(self):
        # yield row
        pass

    def message_generator(self):
        # yield message and receiver email (convert from template, return the output message)
        pass

    def handling_media(self):
        output = ""
        for i in range(len(self.request.files['media'])):
            encoded = base64.b64encode(self.request.files['media'][i]['body'])
            data_uri = bytes(
                f'data:{self.request.files["media"][i]["content_type"]};base64,', encoding='utf-8') + encoded
            output += '<img src="'+data_uri.decode("utf-8")+'">'


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
