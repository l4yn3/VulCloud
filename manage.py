#!/usr/bin/env python3
import os
from app import create_app,scheduler
#from flask_script import Manager, Server

from gevent import pywsgi
from geventwebsocket.handler import WebSocketHandler

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
#manager = Manager(app)

server = pywsgi.WSGIServer(listener=("0.0.0.0",6000), application=app, handler_class=WebSocketHandler)
#manager.add_command("runserver", server)
application = app


if __name__ == '__main__':
    scheduler.start()
    server.serve_forever()
