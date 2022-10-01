from app import *
import requests

def signup_test():

    """Test case for signup"""
    req = requests.post("http://127.0.0.1:5000", {"email" : "sohamsk2@illinois.edu", "username" : "kulksoh21", "password" : "sohamcs222"})
    print(req.content)







