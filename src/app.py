from flask import Flask
from werkzeug.middleware.proxy_fix import ProxyFix
from flask_session import Session
import logging

app = Flask(__name__)
debug = True
if debug:
    app.config['DEBUG'] = True

# Configured to run behind load balancer
app.wsgi_app = ProxyFix(app.wsgi_app, x_for=1, x_host=1)

# Use flask sessions
Session(app)

gunicorn_logger = logging.getLogger('gunicorn.error')
app.logger.handlers = gunicorn_logger.handlers
app.logger.setLevel(gunicorn_logger.level)

from routes import home
from routes import health
from routes import cloner
from routes import selector
from routes import echo


# Start the server on port 5000
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
