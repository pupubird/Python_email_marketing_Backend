import smtplib
import ssl
import tornado
import base64
import send_emails
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class editPageHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('email_content.html')
