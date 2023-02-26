from flask import Blueprint
from shop import db,Category

news_bp = Blueprint("news", __name__,template_folder="templates")

@news_bp.route("/")
def index():
    create_news = Category(title="tes1117t123",img="Sasha Grey")
    db.session.add(create_news)
    db.session.flush()
    db.session.commit()
    return "123"