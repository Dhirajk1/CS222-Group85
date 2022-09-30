import json
from flask import Flask
from flask import jsonify
from flask import Blueprint
from flask import request
from werkzeug.security import generate_password_hash, check_password_hash

login_ = Blueprint("login_", __name__)

@app.route("/login", methods = ["GET", "POST"])
def login(): 
    if request.method == "POST":
        password = request.form.get("password")
        email = request.form.get("email")
        user = UserClass.query.filter_by(email = email).first()
    elif request.method = "GET":
        return jsonify({"Return login page" : True})

    
    if not check_password_hash(user.password, password) and not user:
        return jsonify({"Login Fail, username and password are incorrect or don't match" : False})

    return jsonify({"Login True" : True})

@app.route("/logout")
def logout():
    return jsonify({{"Logout Success": True}})


