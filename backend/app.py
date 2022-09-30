from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_login import UserMixin

database = SQLAlchemy()

app = Flask(__name__) 
app.config["SECRET_KEY"] = "cs222"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.sqlite"

database.init.app(app)

login_manager = LoginManager()
login_manager.init_app(app)

class User(database.Model, UserMixin):
    identification = database.Column(database.Integer, primary_key = True)
    username = database.Column(database.String())

if __name__ == "__main__":
    app.run(debug = True)
