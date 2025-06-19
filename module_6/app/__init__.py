from flask import Flask
from app import pages

def create_app():
    """
    Instantiates a Flask application and applies the blueprint from pages.py
    """
    app = Flask(__name__)
    app.register_blueprint(pages.bp)
    return app