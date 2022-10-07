"""necessary imports for test"""
from app import calendar_home, jsonify
from signup import signup
from login import login, logout
import requests

def signup_test():

    """Test case for signup"""
    req = requests.post("http://127.0.0.1:5000", {"email" : "sohamsk2@illinois.edu",
                                                  "username" : "kulksoh21",
                                                  "password" : "sohamcs222"})
    print(req.content)



def login_test():
    """tests basic login functionality"""
    req = requests.post("http://127.0.0.1:5000", {"email" : "amash2@illinois.edu",
                                                  "username" : "Aryan",
                                                  "password" : "cs222Aryan"})
    print(req.content)

def calendar_home_test():
    """tests homepage"""
    assert calendar_home() == jsonify({"Loaded Calendar page" : True})

def logout_test():
    """testing logout functionality"""
    assert logout() == jsonify({"Logout Success": True})

def login_only_after_signup():
    """make sure login can only happen after signup"""
    assert login() == jsonify({{"User does not exist" : True}})
    assert signup() == jsonify({"Return signup page" : True})
    req = requests.post("http://127.0.0.1:5000", {"email" : "amash2@illinois.edu",
                                                  "username" : "Aryan",
                                                  "password" : "cs222Aryan"})
    print(req.content)
    req2 = requests.post("http://127.0.0.1:5000", {"email" : "amash2@illinois.edu",
                                                   "username" : "Aryan",
                                                   "password" : "cs222Aryan"})
    print(req2.content)
    assert signup() == jsonify({"user already exists" : True})
    assert login() == jsonify({"login success" : True})

def login_without_signup():
    """make sure you can't login without signing up"""
    req = requests.post("http://127.0.0.1:5000", {"email" : "amash2@illinois.edu",
                                                  "username" : "Aryan",
                                                  "password" : "cs222Aryan"})
    print(req.content)
    assert login() == jsonify({"User does not exist" : True})
