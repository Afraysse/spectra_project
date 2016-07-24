import os
import requests

GOOGLE_API_KEY = os.environ["GOOGLE_API_KEY"]

def reverse_geocode(latitude, longitude):
    url = "https://maps.googleapis.com/maps/api/geocode/json?latlng={},{}&key={}".format(latitude, longitude, GOOGLE_API_KEY)

    reverse_geocoding_response = requests.get(url)
    geocode_json = reverse_geocoding_response.json()

    # print geocode_json
    # return geocode_json

    country_code = geocode_json['results'][0]['address_components'][4]['short_name']

    return country_code
