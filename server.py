"""Spectra Hackathon project"""

from jinja2 import StrictUndefined

from flask import Flask, render_template, redirect, request, flash
from flask_debugtoolbar import DebugToolbarExtension

# Set up Flask web app
app = Flask(__name__)
app.secret_key = "ABC123"

# Raise an error for undefined variable in Jinja2, rather than failing silently
app.jinja_env.undefined = StrictUndefined


@app.route('/')
def index():
    """Homepage."""

    return render_template("homepage.html")


if __name__ == "__main__":
    app.debug = True

    connect_to_db(app)

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run()