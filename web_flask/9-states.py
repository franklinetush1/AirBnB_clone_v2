#!/usr/bin/python3
from flask import Flask, render_template
from models import storage

app = Flask(__name__)

@app.teardown_appcontext
def session(exception):
    """Close session"""
    storage.close()

@app.route('/states', strict_slashes=False)
def Display_states():
    """Display html"""
    states = storage.all("State")
    return render_template("9-states.html", state=states)

@app.route('/states', strict_slashes=False)
def states_id(id):
    """Display html with id"""
    for state in storage.all("State").values():
        if state.id == id:
            return render_template("9-states.html", state=state)
    return render_template("9-states.html")
    
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
