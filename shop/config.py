import os

UPLOAD_FOLDER = os.path.join("img", "uploads")

class Config(object):
    SECRET_KEY = "qwe"
    SQLALCHEMY_DATABASE_URI = "sqlite:///app.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    UPLOAD_FOLDER = UPLOAD_FOLDER
    DEBUG = True
