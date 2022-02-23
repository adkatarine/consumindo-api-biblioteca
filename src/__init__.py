from flask import Flask
from src.blueprints.library.library import library_blueprint


app = Flask(__name__)


app.register_blueprint(library_blueprint)
