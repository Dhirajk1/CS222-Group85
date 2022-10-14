"""
Experimenting with .ics file parsing in python
"""
import pprint as pp
from ics import Calendar


def calendar_summary(calendar: Calendar):
    """
    Print out some summary items for the given calendar
    """
    print("This is a:", end=" ")
    pp.pprint(calendar)

    print("\nEvents:\n")
    for event in calendar.events:
        print(event.name)
        print(f"Starts: {event.begin}", end="\t")
        print(f"Ends: {event.end}", end="\n\n")


if __name__ == "__main__":
    with open("uiuc_calendar.ics", "r", encoding="utf-8") as file:
        cal_contents = file.read()
        cal = Calendar(cal_contents)
        calendar_summary(cal)
