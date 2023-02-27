from flask import Blueprint, render_template, request
from shop import db, Category




category_bp = Blueprint('category', __name__, template_folder='templates', static_folder='static',
                        static_url_path='/static/category')


@category_bp.route("/create_category")
def create():
    # create_news = Category(title="tes1117t123",img="Sasha Grey")
    # db.session.add(create_news)
    # db.session.flush()
    # db.session.commit()
    return render_template("create_category.html")
