import tornado.ioloop
import tornado.web
from tornado.options import parse_command_line,options,define

define('port',default=80,type=int)

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('hello,tornado')

def make_app():
    return tornado.web.Application(handlers=[
        (r'/',MainHandler),
    ])


if __name__ == '__main__':
    parse_command_line()
    app = make_app()
    app.listen(options.port)
    tornado.ioloop.IOLoop.current().start()