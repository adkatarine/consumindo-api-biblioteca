from flask import Blueprint, render_template, redirect, url_for, request
from src.consumer_api.consumer_api_library import (
    get_works,
    post_work,
    put_work,
    delete_work,
)
from src.helper.helper import helper_adjust_authors

library_blueprint = Blueprint(
    "library", __name__, template_folder="templates", static_folder="static"
)


@library_blueprint.route("/", methods=["GET"])
def index():
    works = helper_adjust_authors(get_works())
    return render_template("index.html", works=works, error=False)


@library_blueprint.route("/create", methods=["POST"])
def create():
    work = {
        "title": request.form["insert-title"],
        "publishing_company": request.form["insert-publishing_company"],
        "photo": request.form["insert-photo"],
        "authors": request.form["insert-authors"].split(", "),
    }
    error = post_work(work)
    works = helper_adjust_authors(get_works())
    return redirect(url_for("library.index", works=works, error=error))


@library_blueprint.route("/update", methods=["POST"])
def update():
    work = {
        "title": request.form["update-title"],
        "publishing_company": request.form["update-publishing_company"],
        "photo": request.form["update-photo"],
        "authors": request.form["update-authors"].split(", "),
    }
    error = put_work(request.form["id"], work)
    works = helper_adjust_authors(get_works())
    return redirect(url_for("library.index", works=works, error=error))


@library_blueprint.route("/remove/<id>", methods=["GET"])
def remove(id: str):
    error = delete_work(id)
    works = helper_adjust_authors(get_works())
    return redirect(url_for("library.index", works=works, error=error))
