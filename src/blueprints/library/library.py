from flask import Blueprint, render_template
from src.consume_api.consume_api_library import get_works

# from flask_cors import cross_origin

library_blueprint = Blueprint(
    "library",
    __name__,
    template_folder="templates",
    static_folder="static",
    static_url_path="/library/static",
)


@library_blueprint.route("/")
# @cross_origin(origin='localhost', headers=['Content- Type', 'Authorization'])
def index():
    works = get_works()
    return render_template("index.html", works=works)
