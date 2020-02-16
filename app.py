import os
import tornado.ioloop
import tornado.web as web
import webbrowser
import start_smtp_server
import compile_css_js_into_html
import git

public_root = os.path.join(os.path.dirname(__file__), './static/')


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('index.html')


class authenticateHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('email_content.html')


handlers = [
    (r'/', MainHandler),
    (r'/authenticate', authenticateHandler),
    (r'/', web.StaticFileHandler, {'path': public_root}),
]

settings = dict(
    static_path=public_root,
    template_path=public_root
)

application = web.Application(handlers, **settings)

if __name__ == "__main__":

    print("------Updating website content..------")

    # Automatically update the public folder
    frontend = git.cmd.Git('./public')
    frontend.pull()

    print("------Updated website content.------")

    # Clean up every file for later compiling
    files = os.listdir("./static")
    for file_name in files:
        os.remove("./static/"+file_name)
    # compiling into a single html file
    compile_css_js_into_html.main()

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
    server = start_smtp_server.start_server()

    webbrowser.open_new_tab(f"http://localhost:{http_port}/")

    tornado.ioloop.IOLoop.instance().start()
