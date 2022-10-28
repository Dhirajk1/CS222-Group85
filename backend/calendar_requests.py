"""imports of necessary modules for getting calandar events functionality"""
from flask import jsonify
from flask import Blueprint
from flask import request
from requests import RequestException
from user_calendar import UserCalendar

# cyclic import avoided by import placement within file
# pylint: disable=cyclic-import
from app import CalendarClass

calendar_requests_ = Blueprint("calendar_requests_", __name__)


@calendar_requests_.route("/events/find", methods=["GET"])
def get_events():
    """ "This gives events to the frontend in order for the calendars to be able to be displayed"""
    user = request.form.get("user_id")
    calendar = CalendarClass.query.filter_by(user_id=user).first()
    if calendar:
        my_calendar = UserCalendar(calendar)
        return jsonify(
            {
                "found": True,
                "events": [
                    {
                        "title": entry.title,
                        "start": entry.start.isoformat(),
                        "end": entry.end.isoformat(),
                    }
                    for entry in my_calendar.get_entries()
                ],
            }
        )

    return jsonify({"found": False})


@calendar_requests_.route("/events/add", methods=["POST"])
def add_events():
    """add event to user's calendar"""
    user = request.form.get("user_id")
    calendar = CalendarClass.query.filter_by(user_id=user).first()
    if not calendar:
        return jsonify({
            "sucess": False,
            "error": "user's calendar not found"
        })
    
    return jsonify({"Implemented": False})
