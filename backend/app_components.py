"""Component for the Flask app"""
from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_login import UserMixin

# methods are broken up into different files
# pylint: disable=too-few-public-methods

app = Flask(__name__)
CORS(app)

app.config["SECRET_KEY"] = "cs222"

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.sqlite"
database = SQLAlchemy()
database.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)


################### Database Schemas #########################
class UserClass(database.Model, UserMixin):
    """
    User class that inherits from UserMixin for default methods
    for flask login lib and from the SQLAlchemy
    """

    identification = database.Column(database.String(99), primary_key=True)
    username = database.Column(database.String(12), unique=True)
    email = database.Column(database.String(99), unique=True)
    password = database.Column(database.String(99))


class CalendarClass(database.Model):
    """
    A class for the Calendar object as stores in the database (time entries are a csv string)
    """

    identification = database.Column(database.String(99), primary_key=True)
    user_id = database.Column(database.String(99))
    times = database.Column(database.Text)
    details = database.Column(database.Text)
