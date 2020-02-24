import os
import tornado.ioloop
import tornado.web as web
import webbrowser
import start_smtp_server
import compile_external_html
import git
import send_emails
import authenticate
import editPageHandler

public_root = os.path.dirname(os.path.realpath(__file__)) + r'\\static\\'
ROOT = os.path.dirname(os.path.realpath(__file__)) + r'\\public\\'
OUTPUT_STATIC = os.path.dirname(os.path.realpath(__file__)) + r'\\static\\'


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('index.html')


handlers = [
    (r'/', MainHandler),
    (r'/authenticate', authenticate.authenticateHandler),
    (r'/edit', editPageHandler.editPageHandler),
    (r'/sendEmails', send_emails.sendEmailsHandler),
    (r'/', web.StaticFileHandler, {'path': public_root}),
]

settings = dict(
    static_path=public_root,
    template_path=public_root
)

if __name__ == "__main__":
    application = web.Application(handlers, **settings)

    # Automatically update git
    backend = git.cmd.Git('.')
    print("Updating server content from", backend.remote(
        verbose=True).split("(fetch")[0].replace("origin\t", ""))
    backend.pull()
    print("Updated backend server content")

    frontend = git.cmd.Git(ROOT)
    print("Updating website content from", frontend.remote(verbose=True).split("(fetch)")
          [0].replace("origin\t", ""))
    frontend.pull()

    print("Updated website content.")

    # Clean up every file for later compiling
    os.makedirs(OUTPUT_STATIC, exist_ok=True)
    for filename in os.listdir(OUTPUT_STATIC):
        if '.html' in filename:
            os.remove(OUTPUT_STATIC+filename)

    # compiling into a single html file
    compile_external_html.main()

    http_port = 7777
    print("""
    _________ __                 __   
 /   _____//  |______ ________/  |_ 
 \\_____  \\\\   __\\__  \\\\_  __ \\   __\\
 /        \\|  |  / __ \\|  | \\/|  |  
/_______  /|__| (____  /__|   |__|  
        \\/           \\/             
    """)
    print(f"Starting HTTP Server at port {http_port}")
    application.listen(http_port)

    webbrowser.open_new_tab(f"http://localhost:{http_port}/")

    tornado.ioloop.IOLoop.instance().start()
