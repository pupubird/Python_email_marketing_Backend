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
            self.set_status(400)
            self.write({"status": 400})


class Config:
    __instance = None
    @staticmethod
    def getInstance():
        if Config.__instance == None:
            Config()
        return Config.__instance

    def __init__(self):
        self.Server = None
        self.Email = None
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
    config = Config
    try:
        server.login(sender_email, password)
        config.Server = server
        config.Email = sender_email
    except smtplib.SMTPAuthenticationError:
        config.Server = None
        config.Email = None
        server.close()
        return None
    return server
