"""imports of necessary modules for getting calandar events functionality"""
from flask import jsonify
from flask import Blueprint
from flask import request
from user_calendar import UserCalendar

from app import CalendarClass

events_ = Blueprint("events_", __name__)

@events_.route("/send/events", methods=["GET"])
def get_events():
    """"This gives events to the frontend in order for the calendars to be able to be displayed"""
    user = request.form.get("user_id")
    calendar = CalendarClass.query.filter_by(user_id = user).first()
    my_calendar = UserCalendar(calendar)
    my_calendar.print()

    return jsonify(
        {
            "result": "Success?",
            "calendar_info": {
                "entries": [entry.to_str() for entry in my_calendar.get_entries()],
            },
        }
    )
