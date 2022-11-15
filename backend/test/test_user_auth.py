""" Test for user authentication """
import unittest
from .flask_tester import FlaskTester


class FlaskAppTests(FlaskTester):
    """
    Class to test user auth features
    """

    def test_login_new_user(self):
        """tests basic login functionality"""
        req = self.app.post(
            "/signup",
            data={
                "email": "Aryan@gmail.com",
                "username": "aryan",
                "password": "fjdanksjn",
            },
        )
        assert req.json
        req = self.app.post(
            "/login",
            data={
                "email": "Aryan@gmail.com",
                "username": "aryan",
                "password": "fjdanksjn",
            },
        )
        self.assertEqual(req.json, {"Login": True})

    def test_login_incorrect(self):
        """Incorrect user login"""
        req = self.app.post(
            "/login",
            data={
                "email": "Aryan@gmail.com",
                "username": "aryan",
                "password": "fjdanksn",
            },
        )
        self.assertEqual(
            req.json,
            {"Login": False, "Log": "invalid credentials"},
        )


if __name__ == "__main__":
    unittest.main()
