#!/usr/bin/python3
"""Starts a Flask application"""
from models import storage, render_template
from flask import Flask

app = Flask(__name__)


@app.route("/hbnb_filters", strict_slashes=False)
def hbnb_filters():
    """Displays the filters"""
    amen = storage.all("Amenity")
    st = storage.all("State")
    return render_template("10-hbnb_filters.html",
                           states=st, amenities=amen)


@app.teardown_appcontext
def teardown(err):
    """Remove the current SQLAlchemy session."""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0")
