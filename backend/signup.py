from flask import jsonify
from flask import Blueprint
from flask import request
from werkzeug.security import generate_password_hash
from app import UserClass
from app import database
import uuid

signup_ = Blueprint("signup_", __name__)


@signup_.route("/signup", methods=["GET", "POST"])
def signup():
    database.create_all()
    """signup function that creates users"""

    if request.method == "GET":
        return jsonify({"Return signup page": True})

    password = request.form.get("password")
    email = request.form.get("email")
    username = request.form.get("username")
    
    user_email = UserClass.query.filter_by(email=email).first()
    user_username = UserClass.query.filter_by(username=username).first()

    if user_email or user_username:
        return jsonify({"user already exists": True})
    new_current_user = UserClass(
        identification=str(uuid.uuid1()),
        email=email,
        username=username,
        password=generate_password_hash(password, method="sha256"),
    )

    database.session.add(new_current_user)
    database.session.commit()

    return jsonify({"home page": True})
