from flask import Flask

# from flask_cors import CORS


app = Flask(__name__)
# app.config['SECRET_KEY'] = 'the quick brown fox jumps over the lazy   dog'
# app.config['CORS_HEADERS'] = 'Content-Type'
#
# cors = CORS(app, resources={r"/": {"origins": "http://127.0.0.1:5000"}})

from src.blueprints.library.library import library_blueprint

app.register_blueprint(library_blueprint)
