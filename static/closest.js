$.getScript("https://maps.googleapis.com/maps/api/js?key=" + window.key + "&callback=initMap&v=weekly&libraries=places").done(function (script, textStatus) {
	google.maps.event.addListener(window, "load", showClosest)
})

function showClosest() {
    var b = populateStartAddressWithUserLocation()
}

