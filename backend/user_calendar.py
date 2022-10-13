"""
Python objects for storing the calendar
"""
import datetime
from typing import List
from .calendar_utils import file_is_good, parse_ical


class UserCalendar:
    """
    Calendar class for users
    """

    def __init__(self, calendar):
        self.busy = []
        self.time_details = []
        self.user_id = calendar.user_id
        for time in calendar.times.split(","):
            self.busy.append(datetime.datetime.fromisoformat(time))
        for detail in calendar.details.split(","):
            self.time_details.append(detail)

    def import_ical(self, i_cal_file: str):
        """
        Recieves an ical file, parses it and adds it to the calendar
        """
        if file_is_good(i_cal_file):
            self.time_details, self.busy = parse_ical(i_cal_file)

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

    def get_event_details(self) -> List[str]:
        """
        Return a list of all the event's details
        """
        return self.time_details
