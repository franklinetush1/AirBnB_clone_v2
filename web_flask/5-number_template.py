#!/usr/bin/python3
"""Runs an app with flask framework"""
from flask import Flask

app = Flask(__name__)

@app.route('/',strict_slashes=False)
def hello():
  """Displays 'Hello HBNB!'"""
    return “Hello HBNB!”

@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Displays'HBNB'"""
    return "HBNB"

@app.route("/c/<text>", strict_slashes=False)
def dispc(text):
    """Displays 'C' followed by <text>."""
    text = text.replace("_", " ")
    return "C {}".format(text)

@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text="is cool"):
    """Displays /python/<text>"""
    text = text.replace("_", " ")
    return "Python {}".format(text)

@app.route("/number/<int:n>", strict_slashes=False)
    def number(n):
    """Displays whether 'n is a number'"""
    return "{} is a number".format(n)

@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """ Function called with /number_template/<n> route """
    return render_template('5-number.html', num=n)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
