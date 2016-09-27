import os
from tornado import web
from tornado import ioloop
from tornado.options import options, define


define('port', default=9988, help='Run on the default port', type=int)


class IndexHandler(web.RequestHandler):
    def get(self):
        self.render('index.html')


def make_app():
    app = web.Application([
            (r'/', IndexHandler),
            ],
            debug=True,
            template_path = os.path.join(os.path.dirname(__file__), 'templates'),
            static_path = os.path.join(os.path.dirname(__file__), 'static')
        )
    return app



if __name__ == '__main__':
    app = make_app()
    options.parse_command_line()
    app.listen(options.port)
    ioloop.IOLoop.current().start()
