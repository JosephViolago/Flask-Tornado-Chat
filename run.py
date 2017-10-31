import os
import sys
from tornado.ioloop import PeriodicCallback,IOLoop
from tornado.web import Application, FallbackHandler, StaticFileHandler
from tornado.wsgi import WSGIContainer

from flask_app import app, db
from chatserver import NowHandler


def startTornado():
    #PeriodicCallback(NowHandler.echo_now,1000).start()
    #redis = redis.StrictRedis(host="0.0.0.0", port=5000, db=0)

    server.listen(port)
    IOLoop.instance().start()

def stopTornado():
    print("\nKeyboardInterrupt; Tornado is shutting down now.")
    IOLoop.instance().stop()
    sys.exit(0)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))

    container = WSGIContainer(app)
    server = Application([
        (r'/(favicon.ico)', StaticFileHandler, {'path': 'static/img'}),
        (r'/now', NowHandler),
        (r'.*', FallbackHandler,{'fallback': container})
    ])

    try:
        startTornado()
    except (KeyboardInterrupt, SystemExit):
        stopTornado()
