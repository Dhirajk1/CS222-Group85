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
        if not user:
            return jsonify({"User does not exist" : True})
        elif not check_password_hash(user.password, password):
            return jsonify({"Password incorrect" : True})
        else: 
            return jsonify({"login success" : True})
    elif request.method == "GET":
        return jsonify({"Return login page" : True})
    

@login_.route("/logout")
def logout():
    

    """function that logs the user out, outputs if successful"""

    return jsonify({"Logout Success": True})
