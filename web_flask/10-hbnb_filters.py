#!/usr/bin/python3
"""
Start a Flask web applicat
"""
from flask import Flask
from flask import render_template
from models import storage

app = Flask(__name__)

@app.route("/hbnb_filters", strict_slashes=False)
def hbnb_filters():
    """show the HBnB filters HTML page."""
    states = storage.all("State")
    amenities = storage.all("Amenity")
    return render_template("10-hbnb_filters.html",
                           states=states, amenities=amenities)
@app.teardown_appcontext
def teardown(excpt=None):
    """Remove the present SQLAlchemy Session."""
    storage.close()

if __name__ == "__main__":
    app.run(host="0.0.0.0")
