"""
Functions for handling user signup
"""
import uuid
from flask import jsonify, Blueprint, request
from werkzeug.security import generate_password_hash

# cyclic import avoided by import placement within file
# pylint: disable=cyclic-import
from app import UserClass, database

signup_ = Blueprint("signup_", __name__)


@signup_.route("/signup", methods=["POST"])
def signup():
    """signup function that creates users"""
    database.create_all()

    password = request.form.get("password")
    email = request.form.get("email")
    username = request.form.get("username")

    user_email = UserClass.query.filter_by(email=email).first()
    user_username = UserClass.query.filter_by(username=username).first()

    if user_email or user_username:
        return jsonify({"User Added": False, "Log": "User already exists"})

    new_current_user = UserClass(
        identification=str(uuid.uuid1()),
        email=email,
        username=username,
        password=generate_password_hash(password, method="sha256"),
    )

    # next lines are not recognized as member actions by pylint
    database.session.add(new_current_user)  # pylint: disable=maybe-no-member
    database.session.commit()  # pylint: disable=maybe-no-member

    return jsonify({"User Added": True})
