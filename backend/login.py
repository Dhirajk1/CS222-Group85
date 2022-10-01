"""imports of necessary modules for login/logout functionality"""
from flask import jsonify
from flask import Blueprint
from flask import request
from werkzeug.security import check_password_hash
from app import UserClass

login_ = Blueprint("login_", __name__)

#login route, handles get/post methods
@login_.route("/login", methods = ["GET", "POST"])
def login():

    """login function that checks credentials"""

    if request.method == "POST":
        password = request.form.get("password")
        email = request.form.get("email")
        user = UserClass.query.filter_by(email = email).first()
    elif request.method == "GET":
        return jsonify({"Return login page" : True})
    if not check_password_hash(user.password, password) and not user:
        return jsonify({"Login Fail, username and password are incorrect or don't match" : False})
    return jsonify({"Login True" : True})

@login_.route("/logout")
def logout():

    """function that logs the user out, outputs if successful"""

    return jsonify({{"Logout Success": True}})
