from flask import Flask
import os, sys
import logging


try:
    # Define the Flask application object
    app = Flask(__name__)
    from app import routes

    # Setup gunicorn logger
    '''
    gunicorn_logger     = logging.getLogger("gunicorn.error")
    app.logger.handlers = gunicorn_logger.handlers
    app.logger.setLevel(gunicorn_logger.level)
    '''
    app.logger.info("Server started successfully")

except Exception as e:
    app.logger.critical(e)
