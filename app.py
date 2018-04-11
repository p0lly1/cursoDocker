#from flask import Flask
#app = Flask(__name__)

#@app.route("/")
#def hello():
#    return "Hello World!"


#import logging
#from flask import Flask, request
#from logging.handlers import RotatingFileHandler

#app = Flask(__name__)

#handler = RotatingFileHandler('foo.log', maxBytes=10000, backupCount=1)
#handler.setLevel(logging.INFO)
#app.logger.addHandler(handler)

#@app.route("/")
#def hello():
#    app.logger.error(('The referrer was {}'.format(request.referrer)))
#    return "Hello World!"

import logging
from flask import Flask, request
from logging.handlers import RotatingFileHandler

from flask.ext.redis import FlaskRedis

app = Flask(__name__)
redis_store = FlaskRedis(app)

handler = RotatingFileHandler('/tmp/foo.log', maxBytes=10000, backupCount=1)
handler.setLevel(logging.INFO)
app.logger.addHandler(handler)

@app.route("/")
def hello():
    app.logger.error(('The referrer was {}'.format(request.referrer)))
    return "Hello World!"

