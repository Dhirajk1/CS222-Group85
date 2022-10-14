from ast import Assert
from app import *
from signup import signup
from login import login, logout
from flask import url_for
from flask import jsonify
import requests

def test_signup():
    """Test case for signup"""
    req = requests.post("http://127.0.0.1:5000", {"email" : "sohamsk2@illinois.edu",
                                                  "username" : "kulksoh21",
                                                  "password" : "sohamcs222"})
    print(req.content)



# def test_login():
#     """tests basic login functionality"""
#     req = requests.post("http://127.0.0.1:5000", {"email" : "amash2@illinois.edu",
#                                                   "username" : "Aryan",
#                                                   "password" : "cs222Aryan"})
#     print(req.content)

# def test_calendar_home():
#     """tests homepage"""
#     assert calendar_home() == jsonify({"Loaded Calendar page" : True})

# # def test_logout(): 
# #     """testing logout functionality"""
# #     assert logout() == jsonify({"Logout Success": True})

# def test_login_only_after_signup():
#     """make sure login can only happen after signup"""
#     # assert login() == jsonify({{"User does not exist" : True}})
#     # assert signup() == jsonify({"Return signup page" : True})
#     req = requests.post("http://127.0.0.1:5000", {"email" : "amash2@illinois.edu",
#                                                   "username" : "Aryan",
#                                                   "password" : "cs222Aryan"})
#     print(req.content)
#     req2 = requests.post("http://127.0.0.1:5000", {"email" : "amash2@illinois.edu",
#                                                    "username" : "Aryan",
#                                                    "password" : "cs222Aryan"})
#     print(req2.content)
#     # assert signup() == jsonify({"user already exists" : True})
#     # assert login() == jsonify({"login success" : True})

# def test_login_without_signup():
#     """make sure you can't login without signing up"""
#     req = requests.post("http://127.0.0.1:5000", {"email" : "amash2@illinois.edu",
#                                                   "username" : "Aryan",
#                                                   "password" : "cs222Aryan"})
#     print(req.content)
#     # assert login() == jsonify({"User does not exist" : True})


# def test_logout_after_login():
#     """test that we can logout after logging in"""
#     req = requests.post("http://127.0.0.1:5000", {"email" : "sohamsk2@illinois.edu",
#                                                   "username" : "Soham",
#                                                   "password" : "sohamcs222"})
#     print(req.content)
#     # assert logout() == jsonify({"Logout Success": True})
