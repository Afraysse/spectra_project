"use strict";

function initMap() {
  
    // Specify where the map is centered (currently set as Sunnyvale)t
    var myLatLng = {lat: 39.0119, lng: -98.4842};

    var map = new google.maps.Map(document.getElementById('map'), {
        center: myLatLng,
        zoom: 4,
        mapTypeControl: true,
        mapTypeControlOptions: {
            style: google.maps.MapTypeControlStyle.DROPDOWN_MENU
        },
        streetViewControl: true,
        streetViewControlOptions: {
            position: google.maps.ControlPosition.LEFT_CENTER
        },
        zoomControl: true,
        zoomControlOptions: {
            position: google.maps.ControlPosition.LEFT_CENTER
        },
    });
  
}