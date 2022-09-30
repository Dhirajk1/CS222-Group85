import json
from flask import Flask
from flask import jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_login import UserMixin

from admin.login_ import login_

database = SQLAlchemy()

app = Flask(__name__)
app.register_blueprint(login_, url_prefix='')

app.config["SECRET_KEY"] = "cs222"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.sqlite"

database.init.app(app)

login_manager = LoginManager()
login_manager.init_app(app)

class UserClass(database.Model, UserMixin):
    identification = database.Column(database.Integer, primary_key = True)
    username = database.Column(database.String(12), unique = True)
    email = database.Column(database.String(99), unique = True)
    password = database.Column(database.String(99))

@login_manager.user_loader
def load_user(user_id):
    return UserClass.get(user_id)

@app.route('/')
def calendar_home():
    return jsonify({"Loaded calendar page" : True})

if __name__ == "__main__":
    app.run(debug = True)
