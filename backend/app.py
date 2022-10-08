"""imports of necessary modules for app initilization and user class functionality"""
import uuid
from flask import Flask
from flask import jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_login import UserMixin
from user_calendar import Calendar

app = Flask(__name__)

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
        times="2011-11-04 00:05:23.283+00:00,2014-01-14 00:15:23.283+00:00",
        user_id="myUser:)",
        details="EVENT,Event2",
    )
    database.session.add(new_calendar)
    database.session.commit()

    calendar = CalendarClass.query.filter_by(identification=test_id).first()
    my_calendar = Calendar(calendar)
    my_calendar.print()

    return jsonify(
        {
            "result": "Success?",
            "user_id": my_calendar.get_user(),
            "busy-times": [
                time.strftime("%c") for time in my_calendar.get_busy_times()
            ],
            "event-details": my_calendar.get_event_details(),
        }
    )


from login import login_

app.register_blueprint(login_, url_prefix="")

from signup import signup_

app.register_blueprint(signup_, url_prefix="")


if __name__ == "__main__":
    app.run(debug=True)
