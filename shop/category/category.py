from uuid import uuid4
import os
from flask import Blueprint, render_template, request
from shop import db, Category

category_bp = Blueprint('category', __name__, template_folder='templates', static_folder='static',
                        static_url_path='/static/category')

ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg"}

UPLOAD_FOLDER = os.path.join("img", "uploads")


@category_bp.route("/create_category", methods=["GET", "POST"])
def create():
    if request.method == "POST":
        title = request.form["title"]

        file = request.files["file"]

        file_extensions = file.filename

        file.filename = f'{uuid4()}.{file.filename.split(".")[-1].lower()}'

        file.save(os.path.join("static", UPLOAD_FOLDER, file.filename))

        create_news = Category(title=title, img=file.filename)
        db.session.add(create_news)
        db.session.flush()
        db.session.commit()

    return render_template("create_category.html")
