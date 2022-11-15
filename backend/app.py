"""imports of necessary modules for app initilization and user class functionality"""
# Extra imports here for testing flexibility
from app_components import app, database, CalendarClass  # pylint: disable=unused-import
from flask import jsonify
from login import login_
from signup import signup_
from calendar_requests import calendar_requests_

# Registering paths contains in other python files
app.register_blueprint(login_, url_prefix="")
app.register_blueprint(signup_, url_prefix="")
app.register_blueprint(calendar_requests_, url_prefix="/calendar")

@app.route("/")
def calendar_home():
    """
    Check valid load
    """
    return jsonify({"Default Load": True})

if __name__ == "__main__":
    app.run(debug=True)
