from gevent import pywsgi
from vvip_video.wsgi import application

server = pywsgi.WSGIServer(('0.0.0.0', 8000), application)
application.debug = True
server.serve_forever()