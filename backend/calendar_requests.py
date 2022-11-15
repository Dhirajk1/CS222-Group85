"""imports of necessary modules for getting calandar events functionality"""
from flask import jsonify
from flask import Blueprint
from flask import request
from user_calendar import UserCalendar

# cyclic import avoided by import placement within file
# pylint: disable=cyclic-import
from app import CalendarClass, database

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
    database.create_all()
    user = request.form.get("user_id")
    calendar = CalendarClass.query.filter_by(user_id=user).first()

    if not calendar:
        return jsonify({"sucess": False, "error": "user's calendar not found"})

    # appending to database entry
    title = request.form.get("title")
    start = request.form.get("start")
    end = request.form.get("end")

    calendar.details += f",{title}"
    calendar.times += f",{start}=>{end}"

    return jsonify({"success": True})


@calendar_requests_.route("/events/remove", methods=["POST"])
def remove_event():
    """Remove an event (by time) from the calendar"""
    database.create_all()

    user = request.form.get("user_id")
    date = request.form.get("date")  # iso format date string

    calendar = CalendarClass.query.filter_by(user_id=user).first()
    if not calendar:
        return jsonify({"sucess": False, "error": "user's calendar not found"})

    # appending to database entry
    times = []
    details = []
    for time, detail in zip(calendar.times.split(","), calendar.details.split(",")):
        if not time.startswith(date):
            times.append(time)
            details.append(detail)

    calendar.times = ",".join(times)
    calendar.details = ",".join(details)
    return jsonify({"success": True})


@calendar_requests_.route("/events/edit", methods=["POST"])
def edit_event():
    """Edit an existing event"""
    database.create_all()
    user = request.form.get("user_id")
    date = request.form.get("date")  # iso format date string (key)
    new_detail = request.form.get("detail")

    calendar = CalendarClass.query.filter_by(user_id=user).first()
    if not calendar:
        return jsonify({"Sucess": False, "Log": "user's calendar not found"})

    # appending to database entry
    times = []
    details = []
    for time, detail in zip(calendar.times.split(","), calendar.details.split(",")):
        times.append(time)
        if time.startswith(date):
            details.append(new_detail)
        else:
            details.append(detail)

    calendar.times = ",".join(times)
    calendar.details = ",".join(details)

    return jsonify({"Suceess": True})
