"""Testing for backend code"""
import json
import requests
from flask import jsonify
from app import app, calendar_home

# disabled for testing purposes
# pylint: disable=missing-timeout
def test_signup():
    """Test case for signup"""
    req = requests.post(
        "http://127.0.0.1:5000/signup",
        {"email": "dhiraj2@illinois.edu", "username": "dhiraj", "password": "1234"},
    )
    assert req.content


def test_login():
    """tests basic login functionality"""
    req = requests.post(
        "http://127.0.0.1:5000/login",
        {
            "email": "dhiraj2@illinois.edu",
            "username": "dhiraj",
            "password": "1234",
        },
    )
    assert json.loads(req.content) == {"Login True": True}


def test_calendar_home():
    """tests homepage"""
    with app.app_context():
        res = calendar_home()
        print(res.json)
        assert res.json == {"Loaded calendar page": True}


def test_sample_calendar():
    """
    Test to see if calendar works
    """
    with app.app_context():
        res = requests.get("http://127.0.0.1:5000/test/calendar")
        expected = jsonify(
            {
                "calendar_info": {
                    "entries": [
                        "Event: EVENT; Starts at: Thu Aug 25 09:00:00 2022; "
                        "Ends at: Thu Aug 25 11:30:00 2022",
                    ],
                    "user_id": "myUser:)",
                },
                "result": "Success?",
            }
        )
        assert expected.get_data(as_text=True) == res.text
