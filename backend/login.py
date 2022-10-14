"""imports of necessary modules for login/logout functionality"""
from flask import jsonify
from flask import Blueprint
from flask import request
from werkzeug.security import check_password_hash

# cyclic import avoided by import placement within file
# pylint: disable=cyclic-import
from app import UserClass

login_ = Blueprint("login_", __name__)


@login_.route("/login", methods=["GET", "POST"])
def login():

    """login function that checks credentials"""

    if request.method == "POST":
        password = request.form.get("password")
        email = request.form.get("email")
        user = UserClass.query.filter_by(email=email).first()
        print(user)
        if user and check_password_hash(user.password, password):
            return jsonify({"Login True": True})
        return jsonify(
            {"Login Fail, username and password are incorrect or don't match": False}
        )
    return jsonify({"Return login page": True})


@login_.route("/logout")
def logout():

    """function that logs the user out, outputs if successful"""

    return jsonify({"Logout Success": True})
