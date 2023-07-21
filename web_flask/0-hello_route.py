#!/usr/bin/python3
"""Runs an app with flask framework"""
from flask import Flask

app = Flask(__name__)
@app.route('/',strict_slashes=False)

def hello():
  """Returnn 'Hello HBNB!'"""
    return “Hello HBNB!”

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
