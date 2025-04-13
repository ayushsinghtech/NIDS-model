# app/__init__.py
from flask import Flask

def create_app():
    app = Flask(__name__)
    from app.routes import api
    # Register the blueprint with a URL prefix (here "/api")
    app.register_blueprint(api, url_prefix="/api")
    return app
