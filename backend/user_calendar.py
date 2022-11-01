"""
Python objects for storing the calendar
"""
import datetime
from typing import List, Tuple
from dataclasses import dataclass
from calendar_utils import CalendarEntry, file_is_good, parse_ical


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
            new_events = parse_ical(i_cal_file)
            self.entries.extend(new_events)

    def print(self):
        """
        Print the user and times
        """
        for entry in self.entries:
            print(entry.to_str())

    def get_user(self) -> str:
        """
        Get Calendar's User
        """
        return self.user_id

    def get_entries(self) -> List[CalendarEntry]:
        """
        Returns a list of all entries
        """
        return self.entries

    def get_db_input(self) -> Tuple[str, str]:
        """
        Return strings for database input
        """
        titles_lst = []
        times_lst = []
        for event in self.entries:
            titles_lst.append(event.title)
            times_lst.append(f"{event.start.isoformat()}=>{event.end.isoformat()}")

        return ",".join(titles_lst), ",".join(times_lst)


if __name__ == "__main__":

    @dataclass
    class TestInput:
        """
        Class to feed in a test input (w/out database entry)
        """

        user_id: str
        details: str
        times: str

    short_input = TestInput(
        times="2022-08-25T09:00:00-05:00=>2022-08-25T11:30:00-05:00",
        user_id="myUser:)",
        details="EVENT",
    )
    sample_calendar = UserCalendar(short_input)
    sample_calendar.print()

    sample_calendar.import_ical("./ICS Parsing Sample/uiuc_calendar.ics")
    db_details, db_times = sample_calendar.get_db_input()

    output_to_recreate = TestInput("1234", db_details, db_times)
    recreated_calendar = UserCalendar(output_to_recreate)
    recreated_calendar.print()
