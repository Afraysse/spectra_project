"use strict";

var map, marker, latitude, longitude;

// Create marker or change position of existing marker
// Source: http://jsfiddle.net/bryan_weaver/gtgw8/
function placeMarker(location) {
    if (marker) {
        marker.setPosition(location);
    } else {
        marker = new google.maps.Marker({          
            position: location,
            map: map,
            draggable: true
        });
    }

    // Keep track of latitude and longitude
    latitude = marker.position.lat();
    longitude = marker.position.lng();
}

function initMap() {
    var centerOfUS = {lat: 39.0119, lng: -98.4842};  // Coordinates for Kansas

    var options = {
        zoom: 4,
        center: centerOfUS,
    };

    map = new google.maps.Map($('#map')[0], options);

    // Add marker to map when clicked
    google.maps.event.addListener(map, 'click', function (evt) {
        placeMarker(evt.latLng);
    });
}

