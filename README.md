#TrendTube
TrendTube is a web app that allows users to click on the world map to see the trending videos for a specific country. Be aware of what's happening around you and around the world!
Note: This app was created during the one-day [Spectra Hackathon](http://sospectra.com) at YouTube.
### Table of Contents
1. [Technologies](#technologies)
2. [Features](#features)
3. [Installation](#installation)
4. [Team](#team)
## <a name="technologies"></a>Technologies
**Front-end:** [HTML5](http://www.w3schools.com/html/), [CSS](http://www.w3schools.com/css/), [Bootstrap](http://getbootstrap.com), [Javascript](https://developer.mozilla.org/en-US/docs/Web/JavaScript), [jQuery](https://jquery.com/)
**Back-end:** [Python](https://www.python.org/), [Flask](http://flask.pocoo.org/)
**APIs:** [Google Maps Javascript](https://developers.google.com/maps/documentation/javascript)
          [Google Maps Geocoding](https://developers.google.com/maps/documentation/geocoding)
          [Youtube Data Search](https://developers.google.com/youtube/v3)
## <a name="features"></a>Features
###Homepage:
+ Users can click on the world map to see the top 10 trending videos for a specific country.
+ Users can click on a video to watch on the screen directly. 
+ (Coming soon) Users can use the search engine by entering a country to see the top 10 trending videos, instead of clicking on the map.
## <a name="installation"></a>Installation
As TrendTube has not yet been deployed, please follow these instructions to run TrendTube locally on your machine:
### Set up TrendTube:
Clone this repository:
```$ git clone https://github.com/afraysse/spectra_project.git```
Create a virtual environment and activate it:
```
$ virtualenv env
$ source env/bin/activate
```
Install the dependencies:
```$ pip install -r requirements.txt```
Get an API key from Google and store in a secrets.sh, make sure to put the file in your `.gitignore`.
Finally, to run the app, start the server:
```$ python server.py```
Go to `localhost:5000` in your browser to check out TrendTube and see what's happening around the world!
- 
## <a name="team"></a>Team 
Ashley Hsiao is a Software Engineer living in the San Francisco Bay Area.
[Email](mailto:aiyihsiao@gmail.com) | [LinkedIn](https://linkedin.com/in/ashleyhsia0) | [Twitter](http://twitter.com/ashleyhsia0).
Annie Fraysse is a Software Engineer living in the San Francisco Bay Area.
[Email](mailto:fraysse.anne@gmail.com) | [LinkedIn](https://www.linkedin.com/in/annefraysse) | [Twitter](http://twitter.com/passtheteapls). 
Katie Tarng is a Software Engineer living in the San Francisco Bay Area.
[Email](mailto:katietarng@gmail.com) | [LinkedIn](https://www.linkedin.com/in/katietarng) | [Twitter](http://twitter.com/katiecodes23).
Allison Scofield is a Software Engineer living in Southern California. 
[Email](mailto:allisonscofield@gmail.com) | [LinkedIn](https://www.linkedin.com/in/allisonscofield).