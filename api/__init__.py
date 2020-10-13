#!/usr/bin/env python3
import os
import sys
import logging
import uuid

from flask import Flask, request, g
import redis
from rq import Queue

r = redis.Redis(
    host=os.environ.get('REDIS_HOST'),
    port=os.environ.get('REDIS_PORT'),
    db=os.environ.get('REDIS_DB')
)

q = Queue(connection=r)


def create_app():
    app = Flask(__name__, template_folder='templates')

    if not os.getenv('APP_SETTINGS'):
        app_settings = f"api.config.DevelopmentConfig"
    else:
        app_settings = f"api.config.{os.getenv('APP_SETTINGS')}Config"
    app.config.from_object(app_settings)

    # shell context for flask cli
    app.shell_context_processor({"api": app})

    # registering blueprints
    from .tasks.views import tasks as tasks_bp
    app.register_blueprint(tasks_bp)

    # log handler
    log_level = logging.INFO if not app.config.get("DEBUG") else logging.DEBUG
    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(log_level)
    handler.setFormatter(
        logging.Formatter("[%(asctime)s] %(levelname)s: %(message)s "
                          "[in %(pathname)s:%(lineno)d]"))

    logging.getLogger("flask_cors").level = logging.DEBUG

    for h in app.logger.handlers:
        app.logger.removeHandler(h)
    app.logger.addHandler(handler)
    app.logger.setLevel(log_level)

    app.logger.info("[WARMUP]: api successfully instantiated")

    @app.before_request
    def set_transaction_id():
        transaction_id = request.headers.get("X-Request-Id")
        g.transaction_id = transaction_id if transaction_id else str(
            uuid.uuid4().hex)

    return app
