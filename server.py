"""Spectra Hackathon project"""

from jinja2 import StrictUndefined

from flask import Flask, render_template, redirect, request, flash
from flask_debugtoolbar import DebugToolbarExtension
from helper_functions import reverse_geocode
from youtube_api import youtube_search 

# Set up Flask web app
app = Flask(__name__)
app.secret_key = "ABC123"

# Raise an error for undefined variable in Jinja2, rather than failing silently
app.jinja_env.undefined = StrictUndefined


@app.route('/')
def index():
    """Homepage."""

    return render_template("homepage.html")

@app.route('/get-videos.json', methods=['POST'])
def return_top_videos():

    latitude = request.form.get("latitude")
    longitude = request.form.get("longitude")

    country_code = reverse_geocode(latitude, longitude)
    videos = youtube_search(country_code)

    return jsonify(videos=videos)

if __name__ == "__main__":
    app.debug = True

    connect_to_db(app)

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run()