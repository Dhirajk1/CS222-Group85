from flask import Blueprint, render_template, flash
from flask_login import login_required, current_user
from _init_ import create_app

main = Blueprint('main', app.py)

@main.route('/')
def index():
    return 'index'

@main.route('/profile')
def profile():
    return 'profile'

