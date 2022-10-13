"""Utilities for the calendar class to use"""

from typing import List, Tuple
from ics import Calendar


def file_is_good(file_path) -> bool:
    """
    Returns whether a file can be successfully opened
    """
    if not file_path.endswith(".ics"):
        return False
    try:
        open(file_path, "r", encoding="utf-8")
        return True
    except IOError:
        print("Error: File does not appear to exist.")
        return False


def parse_ical(i_cal_file_path: str) -> Tuple[List[str], List[str]]:
    """
    Parse the ical file into a list of events and list of times
    """
    events = []
    times = []
    with open(i_cal_file_path, "r", encoding="utf-8") as file:
        cal_contents = file.read()
        cal = Calendar(cal_contents)
        for event in cal.events:
            events.append(event.name)
            times.append(f"{event.start}=>{event.end}")
    return (events, times)
