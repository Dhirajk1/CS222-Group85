"""Template Class for setting up flask testing"""
import unittest

import app as tested_app


class FlaskTester(unittest.TestCase):
    """
    Class for streamlining tests on the `app.py` (flask)
    """

    def setUp(self):
        tested_app.app.config["TESTING"] = True
        self.app = tested_app.app.test_client()
        with tested_app.app.app_context():
            tested_app.database.drop_all()
            tested_app.database.create_all()
