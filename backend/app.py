<<<<<<< HEAD
=======
"""imports of necessary modules for app initilization and user class functionality"""
from flask import Flask
from flask import jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_login import UserMixin

database = SQLAlchemy()

app = Flask(__name__)

app.config["SECRET_KEY"] = "cs222"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.sqlite"

from app import database


class UserClass(database.Model, UserMixin):
    """
    user class that inherits from UserMixin for default methods
    for flask login lib and from the SQLAlchemy
    """
    identification = database.Column(database.String(99), primary_key = True)
    username = database.Column(database.String(12), unique = True)
    email = database.Column(database.String(99), unique = True)
    password = database.Column(database.String(99))

login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    """
    required method for flask login lib functionality that returns
    the userid
    """
    return UserClass.get(user_id)

@app.route('/')
def calendar_home():
    """
    meant to open up a standard blankslate homepage for now
    """
    return jsonify({"Loaded calendar page" : True})


from login import login_

app.register_blueprint(login_, url_prefix='')

if __name__ == "__main__":
    app.run(debug = True)
>>>>>>> 370d4f0688a6afd351452b0d404e8c2ac867e08b
