//https://github.com/bobby-didcoding/did_django_google_maps_api
$.getScript( "https://maps.googleapis.com/maps/api/js?key=" + google_api_key + "&libraries=places")
.done(function( script, textStatus ) {
    google.maps.event.addDomListener(window, "load", initMap)

})


function initMap() {
    var directionsService = new google.maps.DirectionsService;
    var directionsDisplay = new google.maps.DirectionsRenderer;
    var map = new google.maps.Map(document.getElementById('map-route'), {
        zoom: 7,
        center: {lat: lat_a, lng: long_a}
    });
    directionsDisplay.setMap(map);
    calculateAndDisplayRoute(directionsService, directionsDisplay);
    const data = [
      {'latitude': 38.035296426566426, 'longitude': -78.50360833130435},
      {'latitude': 38.036391644762894, 'longitude': -78.50589947123407}
    ]
    const markers = data?.map((i) => {
      const marker = new google.maps.Marker({
          position: { lat: parseFloat(i.latitude), lng: parseFloat(i.longitude)},
          map: map,
      })
  });
}

function calculateAndDisplayRoute(directionsService, directionsDisplay) {
    directionsService.route({
        origin: origin,
        destination: destination,
        travelMode: 'WALKING'
    }, function(response, status) {
      if (status === 'OK') {
        directionsDisplay.setDirections(response);


      } else {

        alert('Directions request failed due to ' + status);
        window.location.assign("/route")
      }
    });
}