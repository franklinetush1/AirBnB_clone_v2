#!/usr/bin/python3
from flask import Flask, render_template
from models import storage

app = Flask(__name__)

@app.teardown_appcontext
def teardown_app(exception):
    """Remove session"""
    storage.close()

@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """Display html page"""
    states = storage.all("State")
    return render_template("8-cities_by_states.html", states=states)
