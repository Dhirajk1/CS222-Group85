"""
Python objects for storing the calendar
"""
import datetime
from typing import List
from dataclasses import dataclass
from .calendar_utils import file_is_good, parse_ical


@dataclass
class CalendarEntry:
    """
    Object to store entries
    """

    title: str
    start: datetime
    end: datetime

    def to_str(self) -> str:
        """
        String representation of the Calendar Entry
        """
        return f"Event: {self.title}; \
            Starts at: {self.start.strftime('%c')}; Ends at {self.end.strftime('%c')}"


class UserCalendar:
    """
    Calendar class for users
    """

    def __init__(self, calendar):
        self.entries = []
        self.user_id = calendar.user_id

        titles = calendar.details.split(",")
        times = calendar.times.split(",")
        if len(times) != len(titles):
            raise ValueError("Title and Time Counts don't match")

        for title, time in zip(titles, times):
            start, end = time.split("=>")
            self.entries.append(
                CalendarEntry(
                    title,
                    datetime.datetime.fromisoformat(start),
                    datetime.datetime.fromisoformat(end),
                )
            )

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
