from flask import jsonify
from flask import Blueprint
from flask import request
from werkzeug.security import generate_password_hash
from app import UserClass
from app import database

signup_ = Blueprint("signup_", __name__)

@signup_.route('/signup', methods=['GET', 'POST'])
def signup():

    """signup function that creates users"""


    if(request.method == 'GET'):
        return jsonify({"Return signup page" : True})
    
    password = request.form.get("password")
    email = request.form.get("email")
    username = request.form.get("username")
    user = UserClass.query.filter_by(email = email).first()

    if user:
        return jsonify({{"user already exists": True}}) 

    new_current_user = UserClass(email = email, username = username, password = generate_password_hash(password, method='sha256'))    
        
    database.session.add(new_current_user)
    database.session.commit()
        
    return jsonify({{"home page": True}}) 


