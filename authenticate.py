import smtplib
import ssl
import random


def authenticate(server, sender_email, password):
    try:
        server.login(sender_email, password)
    except Exception:
        return None
    return server
