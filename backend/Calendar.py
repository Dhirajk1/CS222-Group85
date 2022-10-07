"""
Python objects for storing the calendar
"""
import datetime
from typing import List


class Calendar:
    """
    Calendar class
    """

    def __init__(self, calendar):
        self.busy = []
        self.time_details = []
        self.user_id = calendar.user_id
        for time in calendar.times.split(","):
            self.busy.append(datetime.datetime.fromisoformat(time))
        for detail in calendar.details.split(","):
            self.time_details.append(detail)

    def print(self):
        """
        Print the user and times
        """
        print(f"User: {self.user_id}")
        print("\nTimes:")
        print([time.strftime("%c") for time in self.busy])
        print(self.time_details)

    def get_user(self) -> str:
        """
        Get Calendar's User
        """
        return self.user_id

    def get_busy_times(self) -> List[datetime.datetime]:
        """
        Returns a list of all busy times
        """
        return self.busy
