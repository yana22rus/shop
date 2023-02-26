from .config import Config
from datetime import datetime
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)


class Goods(db.Model):
    __tablename__ = 'goods'
    id = db.Column(db.Integer(), primary_key=True)
    price = db.Column(db.Integer, db.CheckConstraint('number_stock>=1'), nullable=False)
    title = db.Column(db.String(255), nullable=False, unique=True)
    subtitle = db.Column(db.String(255), nullable=True)
    description = db.Column(db.String(2000), nullable=True)
    guarantee = db.Column(db.String(2000), nullable=True)
    category = db.Column(db.String(255), nullable=False)
    brand = db.Column(db.String(255), nullable=False)
    color = db.Column(db.String(255), nullable=False)
    number_stock = db.Column(db.Integer, db.CheckConstraint('number_stock>=0'), nullable=False)
    created_on = db.Column(db.DateTime, default=datetime.now)
    updated_on = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)


if __name__ == "__main__":
    app.run()
