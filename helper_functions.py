import os
import requests

GOOGLE_API_KEY = os.environ["GOOGLE_API_KEY"]

def reverse_geocode(latitude, longitude):
    reverse_geocoding_response = requests.get("https://maps.googleapis.com/maps/api/geocode/json?latlng="+str(latitude)+","+str(longitude)+"&key="+GOOGLE_API_KEY)
    geocode_json = reverse_geocoding_response.json()

    country_code = geocode_json['results'][0]['address_components'][-2]['short_name']

    return country_code
