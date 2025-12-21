from os import getenv, path
from flask_sqlalchemy import SQLAlchemy
from app import app

DB_PATH = path.dirname(path.abspath(__file__))
DB_URL = "sqlite:///" + path.join(DB_PATH, getenv("DATABASE_NAME"))

app.config["SQLALCHEMY_DATABASE_URI"] = DB_URL
db = SQLAlchemy(app)
