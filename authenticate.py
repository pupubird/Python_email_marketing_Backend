import smtplib
import ssl
import random
import tornado
import start_smtp_server


class authenticateHandler(tornado.web.RequestHandler):
    def post(self):
        server = start_smtp_server.start_server()
        server = authenticate(server, self.get_body_argument(
            'sender_email_field'), self.get_body_argument('app_password_field'))

        if server:
            self.redirect('/edit')
        else:
            self.write('<h1>Incorrect information</h1>')


class Config:
    __instance = None
    @staticmethod
    def getInstance():
        if Config.__instance == None:
            Config()
        return Config.__instance

    def __init__(self):
        if Config.__instance != None:
            raise Exception(
                "Singleton class cannot be instantiate with more than one class")
        else:
            Config.__instance = self

    @property
    def Server(self):
        return self._Server

    @Server.setter
    def Server(self, new_server):
        self._Server = new_server

    @property
    def Email(self):
        return self._Email

    @Email.setter
    def Email(self, new_email):
        self._Email = new_email


def authenticate(server, sender_email, password):
    try:
        server.login(sender_email, password)
        config = Config()
        config.Server = server
        config.Email = sender_email
    except smtplib.SMTPAuthenticationError:
        server.close()
        return None
    return server
