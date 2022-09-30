from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from models import User
from auth import auth as auth_blueprint
from main import main as main_blueprint

db = SQLAlchemy()

f create_app():
    app = Flask(app.py)
    app.config['Secret_Key'] = 'cs222'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'backend\Create_LoginPage\db.sqlite'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    login = LoginManager()
    login.login_view = 'auth_login'
    login.init_app(app)

    @login.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))
    
    app.register_blueprint(auth_blueprint)
    app.register_blueprint(main_blueprint)
    
    return app

print('hello word')