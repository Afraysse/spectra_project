"use strict";

var map, marker, latitude, longitude;

function showVideos(result) {

    console.log(result);

    // var videos = $.each(videos, function (key, value) {
    //                 $("#modal-" + result.id).find(".modal-body .matched-ing")
    //                 .append('<i class="fa fa-square-o" aria-hidden="true" style="font-size: x-small"></i>  ' + value.name + ' ' + (value.amount).toFixed(1) + ' ' + value.unit + '<br>');
    //              });

    for (var video in result) {

        console.log(video);
        console.log(video.channel);


    }

    // $("#left-col").html



}

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

    var coordinates = {
        "latitude": longitude,
        "longitude": latitude
    }

    // AJAX post request to server with coordinates to get videos
    $.get("/get-videos.json", coordinates, showVideos);
    // $.post("/get-videos.json",
    //        coordinates,
    //        showVideos
    //        );
}

function initMap() {
    var centerOfWorld = {lat: 41.8719, lng: 12.5674};  // Coordinates for Italy

    var options = {
        zoom: 2,
        center: centerOfWorld,
    };

    map = new google.maps.Map($('#map')[0], options);

    // Add marker to map when clicked
    google.maps.event.addListener(map, 'click', function (evt) {
        placeMarker(evt.latLng);
    });
}

