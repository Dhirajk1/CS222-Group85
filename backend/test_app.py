"""Testing for backend code"""
import unittest
import uuid

# pylint
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

    def test_get_events_fail(self):
        """
        Test to see if get calendar events work for wrong user
        """
        req = self.app.get("/calendar/events/find", data={"user_id": "myUser"})
        self.assertEqual(
            req.json,
            {"found": False},
        )

    def test_get_events(self):
        """keep"""
        with tested_app.app.app_context():
            tested_app.database.create_all()
            test_id = str(uuid.uuid1())
            entry = tested_app.CalendarClass(
                identification=test_id,
                times=(
                    "2022-08-25T09:00:00-05:00=>2022-08-25T11:30:00-05:00,"
                    "2022-08-25T09:00:00-05:00=>2022-08-25T11:30:00-05:00"
                ),
                user_id="test123",
                details="EVENT,YO",
            )
            # next lines are not recognized as member actions by pylint
            tested_app.database.session.add(entry)  # pylint: disable=maybe-no-member
            tested_app.database.session.commit()  # pylint: disable=maybe-no-member
            req = self.app.get("calendar/events/find", data={"user_id": "test123"})
            self.assertEqual(
                req.json,
                {
                    "events": [
                        {
                            "end": "2022-08-25T11:30:00-05:00",
                            "start": "2022-08-25T09:00:00-05:00",
                            "title": "EVENT",
                        },
                        {
                            "end": "2022-08-25T11:30:00-05:00",
                            "start": "2022-08-25T09:00:00-05:00",
                            "title": "YO",
                        },
                    ],
                    "found": True,
                },
            )

    def test_add_event_no_user(self):
        """add event for user not present"""
        req = self.app.post("/calendar/events/add", data={"user_id": "sdkfljnalsf"})
        self.assertEqual(
            req.json, {"sucess": False, "error": "user's calendar not found"}
        )


if __name__ == "__main__":
    unittest.main()
