import os
import requests
​
GOOGLE_API_KEY = os.environ["GOOGLE_API_KEY"]
​
latitude = str(43.068887774169625)
longitude = str(-103.095703125)
​
reverse_geocoding_response = requests.get("https://maps.googleapis.com/maps/api/geocode/json?latlng="+latitude+","+longitude+"&key="+GOOGLE_API_KEY)
​
print reverse_geocoding_response.json()