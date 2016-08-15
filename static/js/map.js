"use strict";

var map, marker, latitude, longitude;

function showVideos(result) {

    var videos = result;

    $.each(videos, function(i, video) {

        var videoDiv = ('<a href="https://www.youtube.com/watch?v=' + video.vid_id + '" class="list-group-item popup-link">' +
                            '<div class="media">' +
                                '<div class="media-left">' +
                                    '<img class="media-object" src="' + video.vid_tn_url + '" style="width: 100px;" alt="' + 'Video for ' + video.vid_title + '">' +
                                '</div>' +
                                '<div class="media-body">' +
                                    '<h4 class="media-heading">' + video.vid_title + '</h4>' +
                                        '<p>' + video.vid_desc + '</p>' +
                                '</div>' +
                            '</div>' +
                        '</a>');

        $(".list-group").append(videoDiv);
    });
}


// Create marker or change position of existing marker on map
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

    latitude = marker.position.lat();
    longitude = marker.position.lng();

    var coordinates = {
        "latitude": latitude,
        "longitude": longitude
    };

    $(".list-group").empty();

    // Pass the coordinates to the server in order to get a list of videos
    $.post("/get-videos.json",
           coordinates,
           showVideos
           );
}

function initMap() {
    var centerOfWorld = {lat: 41.8719, lng: 12.5674};  // Coordinates for Italy

    var options = {
        zoom: 2,
        center: centerOfWorld,
    };

    map = new google.maps.Map($("#map")[0], options);

    // Add marker to map when clicked
    google.maps.event.addListener(map, "click", function (evt) {
        placeMarker(evt.latLng);
    });
}

