
import smtplib
import ssl


def start_server():
        # Create secure connection with server and send email
    context = ssl.create_default_context()
    # SMTP server has to be at 465
    port = 465

    server = smtplib.SMTP_SSL("smtp.gmail.com", port, context=context)
    print("Starting SMTP Server at", port)
    return server
