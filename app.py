import os
import tornado.ioloop
import tornado.web as web
import webbrowser

public_root = os.path.join(os.path.dirname(__file__), 'public')


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('index.html')


handlers = [
    (r'/', MainHandler),
    (r'/(.*)', web.StaticFileHandler, {'path': public_root}),
]

settings = dict(
    static_path=public_root,
    template_path=public_root
)

application = web.Application(handlers, **settings)

if __name__ == "__main__":
    print("Listening to port 8888")
    application.listen(8888)
    print("Server starts")
    webbrowser.open_new_tab("http://localhost:8888/")
    tornado.ioloop.IOLoop.instance().start()
