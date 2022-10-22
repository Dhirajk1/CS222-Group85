"""imports of necessary modules for app initilization and user class functionality"""
from urllib import request
import uuid
from flask import request # pylint: disable=reimported
from flask import Flask, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_login import UserMixin
from user_calendar import UserCalendar

app = Flask(__name__)
CORS(app)
# pylint: disable=too-few-public-methods
# methods are broken up into different files

app.config["SECRET_KEY"] = "cs222"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.sqlite"
database = SQLAlchemy()
database.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)


class UserClass(database.Model, UserMixin):
    """
    user class that inherits from UserMixin for default methods
    for flask login lib and from the SQLAlchemy
    """

    identification = database.Column(database.String(99), primary_key=True)
    username = database.Column(database.String(12), unique=True)
    email = database.Column(database.String(99), unique=True)
    password = database.Column(database.String(99))


class CalendarClass(database.Model):
    """
    A class for the Calendar object as stores in the database (time entries are a csv string)
    """

    identification = database.Column(database.String(99), primary_key=True)
    user_id = database.Column(database.String(99))
    times = database.Column(database.Text)
    details = database.Column(database.Text)


@login_manager.user_loader
def load_user(user_id):
    """
    required method for flask login lib functionality that returns
    the userid
    """
    return UserClass.get(user_id)


@app.route("/")
def calendar_home():
    """
    meant to open up a standard blankslate homepage for now
    """
    return jsonify({"Loaded calendar page": True})

@app.route("/test/calendar")
def test_calendar():
    """
    Serves as test of the calendar app
    """
    database.create_all()
    test_id = str(uuid.uuid1())
    new_calendar = CalendarClass(
        identification=test_id,
        times="2022-08-25T09:00:00-05:00=>2022-08-25T11:30:00-05:00",
        user_id="myUser:)",
        details="EVENT",
    )
    # next lines are not recognized as member actions by pylint
    database.session.add(new_calendar)  # pylint: disable=maybe-no-member
    database.session.commit()  # pylint: disable=maybe-no-member

    calendar = CalendarClass.query.filter_by(identification=test_id).first()
    my_calendar = UserCalendar(calendar)
    my_calendar.print()
    return jsonify(
        {
            "result": "Success?",
            "calendar_info": {
                "user_id": my_calendar.get_user(),
                "entries": [entry.to_str() for entry in my_calendar.get_entries()],
            },
        }
    )

@app.route("/test/events", methods=["GET"])
def test_events():
    """testing whether the events aare sendable"""
    database.create_all()
    test_id = str(uuid.uuid1())
    user = request.form.get("user_id")
    new_calendar = CalendarClass(
        identification=test_id,
        times="2022-08-25T09:00:00-05:00=>2022-08-25T11:30:00-05:00",
        user_id=user,
        details="EVENT",
    )
    # next lines are not recognized as member actions by pylint
    database.session.add(new_calendar)  # pylint: disable=maybe-no-member
    database.session.commit()  # pylint: disable=maybe-no-member
    # user = "myUser:)"
    print(request.form)
    user2 = "user_id"
    calendar = CalendarClass.query.filter_by(user_id = user).first()
    print(type(user2))
    print(type(user))
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


# We need to do some peculiar things with our import so that our app
# has access to the database and user schemas (hence the disablising of the linter here)


# pylint: disable=wrong-import-position
from login import login_

app.register_blueprint(login_, url_prefix="")

from signup import signup_

app.register_blueprint(signup_, url_prefix="")
# pylint: enable=wrong-import-position

if __name__ == "__main__":
    app.run(debug=True)
