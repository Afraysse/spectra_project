import os
import requests

GOOGLE_API_KEY = os.environ["GOOGLE_API_KEY"]


def reverse_geocode(latitude, longitude):
    """Return a JSON response from Google Maps Reverse Geocoding API."""

    url = "https://maps.googleapis.com/maps/api/geocode/json?latlng={},{}&rkey={}".format(latitude, longitude, GOOGLE_API_KEY)
    response = requests.get(url)

    return response.json()


def get_country_code(json_response):
    """Parse the JSON response to get the country code."""

    for result in json_response.get("results", []):
        for component in result["address_components"]:
            if "country" in component["types"]:
                return component["short_name"]
