#!/usr/bin/python3
"""Runs app with flask framework"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """Displays 'Hello HBNB!'"""
    return ("Hello HBNB!")


@app.route("/hbnb", strict_slashes=False)
def hello_hbnb():
    """Displays'HBNB'"""
    return "HBNB"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
