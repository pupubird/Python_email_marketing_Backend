import smtplib
import ssl
import tornado
import base64
import send_emails
import authenticate
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class editPageHandler(tornado.web.RequestHandler):
    def get(self):
        config = authenticate.Config.getInstance()
        server = config.Server
        sender_email = config.Email

        if not sender_email:
            self.set_status(400)
            self.write({"status": 400})
            return

        self.render('email_content.html')
