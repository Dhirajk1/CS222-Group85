from app import *
import requests

def signup_test():

    """Test case for signup"""
    req = requests.post("http://127.0.0.1:5000", {"email" : "sohamsk2@illinois.edu", "username" : "kulksoh21", "password" : "sohamcs222"})
    print(req.content)
    


def login_test():
    """tests basic login functionality"""
    req = requests.post("http://127.0.0.1:5000", {"email" : "amash2@illinois.edu", "username" : "Aryan", "password" : "cs222Aryan"})
    print(req.content)


def calendar_home_test():
    """tests homepage"""
    assert calendar_home() == jsonify({"Loaded Calendar page" : True})






