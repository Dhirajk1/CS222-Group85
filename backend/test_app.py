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
        with tested_app.app.app_context():
            tested_app.database.drop_all()
            tested_app.database.create_all()

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
            {"Login": False, "log": "invalid credentials"},
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
        """Retrieving events"""
        with tested_app.app.app_context():
            tested_app.database.create_all()
            test_id = str(uuid.uuid1())
            entry = tested_app.CalendarClass(
                identification=test_id,
                times=(
                    "2022-08-25T09:00:00-05:00=>2022-08-25T11:30:00-05:00,"
                    "2022-08-25T09:00:00-05:00=>2022-08-25T11:30:00-05:00"
                ),
                user_id="testmeplz",
                details="EVENT,YO",
            )
            # next lines are not recognized as member actions by pylint
            tested_app.database.session.add(entry)  # pylint: disable=maybe-no-member
            tested_app.database.session.commit()  # pylint: disable=maybe-no-member
            req = self.app.get("calendar/events/find", data={"user_id": "testmeplz"})
            self.assertEqual(
                req.json,
                {
                    "events": [
                        {
                            "title": "EVENT",
                            "start": "2022-08-25T09:00:00-05:00",
                            "end": "2022-08-25T11:30:00-05:00",
                        },
                        {
                            "title": "YO",
                            "start": "2022-08-25T09:00:00-05:00",
                            "end": "2022-08-25T11:30:00-05:00",
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

    def test_add_event(self):
        """add event for valid user"""
        with tested_app.app.app_context():
            tested_app.database.create_all()
            test_id = str(uuid.uuid1())
            entry = tested_app.CalendarClass(
                identification=test_id,
                times=(
                    "2022-08-25T09:00:00-05:00=>2022-08-25T11:30:00-05:00,"
                    "2022-08-25T09:00:00-05:00=>2022-08-25T11:30:00-05:00"
                ),
                user_id="testmeplz",
                details="EVENT,YO",
            )
            # next lines are not recognized as member actions by pylint
            tested_app.database.session.add(entry)  # pylint: disable=maybe-no-member
            events = self.app.get(
                "calendar/events/find", data={"user_id": "testmeplz"}
            ).json
            to_add = {
                "title": "New Added Event",
                "start": "2022-10-25T09:00:00-05:00",
                "end": "2022-10-25T09:00:00-10:00",
            }
            events["events"].append(to_add)
            req = self.app.post(
                "/calendar/events/add",
                data={"user_id": "testmeplz", **to_add},
            )
            self.assertEqual(req.json, {"success": True})
            req = self.app.get("calendar/events/find", data={"user_id": "testmeplz"})
            self.assertEqual(req.json, events)

    def test_remove_event_exists(self):
        """Testing removing an event"""
        with tested_app.app.app_context():
            tested_app.database.create_all()
            test_id = str(uuid.uuid1())
            entry = tested_app.CalendarClass(
                identification=test_id,
                times=(
                    "2022-08-25T09:00:00-05:00=>2022-08-25T11:30:00-05:00,"
                    "2022-08-25T09:00:00-06:00=>2022-09-25T11:30:00-05:00"
                ),
                user_id="testmeplz",
                details="EVENT,YO",
            )
            # next lines are not recognized as member actions by pylint
            tested_app.database.session.add(entry)  # pylint: disable=maybe-no-member
            req = self.app.post(
                "calendar/events/remove",
                data={"user_id": "testmeplz", "date": "2022-08-25T09:00:00-05:00"},
            )
            events = self.app.get(
                "calendar/events/find", data={"user_id": "testmeplz"}
            ).json
            self.assertEqual(
                events["events"],
                [
                    {
                        "end": "2022-09-25T11:30:00-05:00",
                        "start": "2022-08-25T09:00:00-06:00",
                        "title": "YO",
                    }
                ],
            )
            self.assertEqual(req.json, {"success": True})

    def test_remove_event_invalid(self):
        """try to remove"""
        with tested_app.app.app_context():
            tested_app.database.create_all()
            test_id = str(uuid.uuid1())
            entry = tested_app.CalendarClass(
                identification=test_id,
                times=(
                    "2022-08-25T09:00:00-07:00=>2022-08-25T11:30:00-05:00,"
                    "2022-08-25T09:00:00-06:00=>2022-09-25T11:30:00-05:00"
                ),
                user_id="testmeplz",
                details="EVENT,YO",
            )
            # next lines are not recognized as member actions by pylint
            tested_app.database.session.add(entry)  # pylint: disable=maybe-no-member
            req = self.app.post(
                "calendar/events/remove",
                data={"user_id": "testmeplz", "date": "2022-08-25T09:00:00-05:00"},
            )
            events = self.app.get(
                "calendar/events/find", data={"user_id": "testmeplz"}
            ).json
            self.assertEqual(
                events["events"],
                [
                    {
                        "end": "2022-08-25T11:30:00-05:00",
                        "start": "2022-08-25T09:00:00-07:00",
                        "title": "EVENT",
                    },
                    {
                        "end": "2022-09-25T11:30:00-05:00",
                        "start": "2022-08-25T09:00:00-06:00",
                        "title": "YO",
                    },
                ],
            )
            self.assertEqual(req.json, {"success": True})

    def test_edit_event(self):
        """Testing editing event"""
        with tested_app.app.app_context():
            tested_app.database.create_all()
            test_id = str(uuid.uuid1())
            entry = tested_app.CalendarClass(
                identification=test_id,
                times=(
                    "2022-08-25T09:00:00-05:00=>2022-08-25T11:30:00-05:00,"
                    "2022-08-25T09:00:00-06:00=>2022-09-25T11:30:00-05:00"
                ),
                user_id="testmeplz",
                details="EVENT,YO",
            )
            # next lines are not recognized as member actions by pylint
            tested_app.database.session.add(entry)  # pylint: disable=maybe-no-member
            req = self.app.post(
                "calendar/events/edit",
                data={
                    "user_id": "testmeplz",
                    "date": "2022-08-25T09:00:00-05:00",
                    "detail": "changed:)",
                },
            )
            events = self.app.get(
                "calendar/events/find", data={"user_id": "testmeplz"}
            ).json
            self.assertEqual(
                events["events"],
                [
                    {
                        "end": "2022-08-25T11:30:00-05:00",
                        "start": "2022-08-25T09:00:00-05:00",
                        "title": "changed:)",
                    },
                    {
                        "end": "2022-09-25T11:30:00-05:00",
                        "start": "2022-08-25T09:00:00-06:00",
                        "title": "YO",
                    },
                ],
            )
            self.assertEqual(req.json, {"success": True})


if __name__ == "__main__":
    unittest.main()
