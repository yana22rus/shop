from .config import Config
from datetime import datetime
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate(db)


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    migrate.init_app(app, db, render_as_batch=True)
    from shop.news.news import news_bp
    app.register_blueprint(news_bp)

    return app


class Goods(db.Model):
    __tablename__ = 'goods'
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    price = db.Column(db.Integer, db.CheckConstraint('number_stock>=1'), nullable=False)
    title = db.Column(db.String(255), nullable=False, unique=True)
    subtitle = db.Column(db.String(255), nullable=True)
    description = db.Column(db.String(1000), nullable=True)
    guarantee = db.Column(db.String(500), nullable=True)
    category = db.Column(db.String(255), nullable=False)
    brand = db.Column(db.String(255), nullable=False)
    color = db.Column(db.String(255), nullable=False)
    number_stock = db.Column(db.Integer, db.CheckConstraint('number_stock>=0'), nullable=False)
    created_on = db.Column(db.DateTime, default=datetime.now)
    updated_on = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)
    img = db.Column(db.String(255), nullable=False)


class Category(db.Model):
    __tablename__ = 'category'
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    title = db.Column(db.String(255), nullable=False, unique=True)
    img = db.Column(db.String(255), nullable=False)
    created_on = db.Column(db.DateTime, default=datetime.now)
    updated_on = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)
