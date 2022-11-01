"""imports of necessary modules for app initilization and user class functionality"""
from flask import Flask, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_login import UserMixin

app = Flask(__name__)
CORS(app)
# pylint: disable=too-few-public-methods
# methods are broken up into different files

app.config["SECRET_KEY"] = "cs222"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.sqlite"
database = SQLAlchemy()
database.init_app(app)
login_manager = LoginManager()
login_manager.init_app(app)


class UserClass(database.Model, UserMixin):
    """
    user class that inherits from UserMixin for default methods
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


@login_manager.user_loader
def load_user(user_id):
    """
    required method for flask login lib functionality that returns
    the userid
    """
    return UserClass.get(user_id)


@app.route("/")
def calendar_home():
    """
    meant to open up a standard blankslate homepage for now
    """
    return jsonify({"Loaded calendar page": True})


# We need to do some peculiar things with our import so that our app
# has access to the database and user schemas (hence the disablising of the linter here)


# pylint: disable=wrong-import-position
from login import login_

app.register_blueprint(login_, url_prefix="")

from signup import signup_

app.register_blueprint(signup_, url_prefix="")

from calendar_requests import calendar_requests_

app.register_blueprint(calendar_requests_, url_prefix="/calendar")
# pylint: enable=wrong-import-position

if __name__ == "__main__":
    app.run(debug=True)
