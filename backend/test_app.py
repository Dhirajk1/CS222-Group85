"""Testing for backend code"""
import unittest
import app as tested_app


class FlaskAppTests(unittest.TestCase):
    """
    Class for streamlining tests on the `app.py` (flask)
    """

    def setUp(self):
        tested_app.app.config["TESTING"] = True
        self.app = tested_app.app.test_client()

    def test_default_route(self):
        """
        Test to make sure default route successfully return
        """
        res = self.app.get("/")
        self.assertEqual(res.json, {"Loaded calendar page": True})

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
        self.assertEqual(req.json, {"Login True": True})

    def test_login_incorrect(self):
        """Inocorrect user login"""
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
            {"Login Fail, username and password are incorrect or don't match": False},
        )

    def test_sample_calendar(self):
        """
        Test to see if calendar works
        """
        req = self.app.get("/test/calendar")
        expected = {
            "calendar_info": {
                "entries": [
                    "Event: EVENT; Starts at: Thu Aug 25 09:00:00 2022; "
                    "Ends at: Thu Aug 25 11:30:00 2022",
                ],
                "user_id": "myUser:)",
            },
            "result": "Success?",
        }
        self.assertEqual(req.json, expected)

    def test_get_events(self):
        """
        Test to see if get calendar events work
        """
        req = self.app.get('/test/events', data={
                "user_id": "myuser:(",
            },)
        expected = {
            "info": {
                "entries": [
                    "Event: EVENT; Starts at: Thu Aug 25 09:00:00 2022; "
                    "Ends at: Thu Aug 25 11:30:00 2022",
                ],
            },
            "result": "Success?",
        }
        self.assertEqual(req.json, expected)


if __name__ == "__main__":
    unittest.main()
