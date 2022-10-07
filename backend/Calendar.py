'''
Python objects for storing the calendar
'''
import datetime
from typing import List
from flask_login import UserMixin
from sqlalchemy import ForeignKey
from app import database


class CalendarClass(database.Model, UserMixin):
    """
    A class for the Calendar object as stores in the database (time entries are a csv string)
    """

    identification = database.Column(database.String(99), primary_key=True)
    user_id = database.Column(database.String(99), ForeignKey("user.identification"))
    times = database.Column(database.Text)


class Calendar:
    """
    Calendar class
    """

    def __init__(self, user: str, times_csv: str):
        self.busy = []
        self.user = user
        for time in times_csv.split(","):
            self.busy.append(datetime.datetime.fromisoformat(time))

    def print(self):
        """
        Print the user and times
        """
        print(f"User: {self.user}")
        print("\nTimes:")
        print(self.busy)

    def get_user(self):
        """
        Get Calendar's User
        """
        return self.user

    def get_busy_times(self) -> List[datetime.datetime]:
        """
        Returns a list of all busy times
        """
        return self.busy
