"""imports of necessary modules for login/logout functionality"""
from flask import jsonify
from flask import Blueprint
from flask import request
from werkzeug.security import check_password_hash

# cyclic import avoided by import placement within file
# pylint: disable=cyclic-import
from app import UserClass

login_ = Blueprint("login_", __name__)


@login_.route("/login", methods=["POST"])
def login():

    """login function that checks credentials"""
    password = request.form.get("password")
    email = request.form.get("email")

    user = UserClass.query.filter_by(email=email).first()

    if user and check_password_hash(user.password, password):
        return jsonify({"Login": True}), 201

    return jsonify({
        "Login": False,
        "Log": "invalid credentials"
    })
