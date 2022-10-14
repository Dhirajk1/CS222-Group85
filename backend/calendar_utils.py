"""Utilities for the calendar class to use"""

from dataclasses import dataclass
import datetime
from typing import List
from ics import Calendar


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
        return (
            f"Event: {self.title}; "
            f"Starts at: {self.start.strftime('%c')}; Ends at: {self.end.strftime('%c')}"
        )


def file_is_good(file_path: str) -> bool:
    """
    Returns whether a file can be successfully opened
    """
    if not file_path.endswith(".ics"):
        print("Error: Sorry I can only parse .ics files :(")
        return False
    try:
        open(file_path, "r", encoding="utf-8")
        return True
    except IOError:
        print("Error: File does not appear to exist.")
        return False


def parse_ical(i_cal_file_path: str) -> List[CalendarEntry]:
    """
    Parse the ical file into a list of events and list of times
    """
    events = []
    with open(i_cal_file_path, "r", encoding="utf-8") as file:
        cal_contents = file.read()
        cal = Calendar(cal_contents)
        for event in cal.events:
            events.append(
                CalendarEntry(
                    title=event.name,
                    start=datetime.datetime.fromisoformat(str(event.begin)),
                    end=datetime.datetime.fromisoformat(str(event.end)),
                )
            )
    return events


if __name__ == "__main__":
    F_PATH = "./ICS Parsing Sample/uiuc_calendar.ics"
    if file_is_good(F_PATH):
        parsed_events = parse_ical(F_PATH)
        if not parsed_events:
            print("no events found")
        for entry in parsed_events:
            print(entry.to_str())
    else:
        print("failed to open")
