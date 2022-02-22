from flask import Blueprint, render_template, redirect, url_for, request
from src.consume_api.consume_api_library import get_works, post_work, put_work

# from flask_cors import cross_origin

library_blueprint = Blueprint(
    "library", __name__, template_folder="templates", static_folder="static"
)


@library_blueprint.route("/", methods=["GET"])
# @cross_origin(origin='localhost', headers=['Content- Type', 'Authorization'])
def index():
    works = get_works()
    return render_template("index.html", works=works)


@library_blueprint.route("/create", methods=["POST"])
def create():
    work = {
        "title": request.form["insert-title"],
        "publishing_company": request.form["insert-publishing_company"],
        "photo": request.form["insert-photo"],
        "authors": request.form["insert-authors"].split(", "),
    }
    post_work(work)
    works = get_works()
    return redirect(url_for("library.index", works=works))


@library_blueprint.route("/update", methods=["POST"])
def update():
    work = {
        "title": request.form["update-title"],
        "publishing_company": request.form["update-publishing_company"],
        "photo": request.form["update-photo"],
        "authors": request.form["update-authors"].split(", "),
    }
    put_work(request.form["id"], work)
    works = get_works()
    return redirect(url_for("library.index", works=works))
