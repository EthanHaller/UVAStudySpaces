$.getScript("https://maps.googleapis.com/maps/api/js?key=" + key + "&callback=initMap&v=weekly&libraries=places").done(function (script, textStatus) {
	google.maps.event.addListener(window, "load", initMap)
})

function initMap() {
	var directionsService = new google.maps.DirectionsService()
	var directionsDisplay = new google.maps.DirectionsRenderer()
	map = new google.maps.Map(document.getElementById("map"), {
		center: { lat: 38.03413872243867, lng: -78.50873523191473 },
		zoom: 16,
	})
	directionsDisplay.setMap(map)
	if (showDirections != "False") {
		calculateAndDisplayRoute(directionsService, directionsDisplay)
	} else {
		populateStartAddressWithUserLocation()
	}
	initAutocomplete()

	const navbarHeight = document.getElementById("global-navbar").offsetHeight
	const mapHeight = `calc(100vh - ${navbarHeight}px)`
	document.getElementById("map-container").style.height = mapHeight

	const markers = []
	markers.push(
		new google.maps.Marker({
			position: { lat: parseFloat(modData.latitude), lng: parseFloat(modData.longitude) },
			map: map,
		})
	)
}

async function populateStartAddressWithUserLocation() {
	if (navigator.geolocation) {
		navigator.geolocation.getCurrentPosition(function (position) {
			const userLocation = {
				lat: position.coords.latitude,
				lng: position.coords.longitude,
			}

			const userMarker = new google.maps.Marker({
				position: userLocation,
				map: map,
			})

			const geocoder = new google.maps.Geocoder()
			geocoder.geocode({ location: userLocation }, function (results, status) {
				if (status === google.maps.GeocoderStatus.OK) {
					if (results[0]) {
						const userAddress = results[0].formatted_address
						document.getElementById("id-google-address-a").value = userAddress
					}
				}
			})
		})
	}
}

let autocomplete_a
let autocomplete_b

async function initAutocomplete() {
	autocomplete_a = new google.maps.places.Autocomplete(document.getElementById("id-google-address-a"), {
		types: ["address"],
		componentRestrictions: { country: ["usa"] },
	})

	autocomplete_a.addListener("place_changed", function () {
		onPlaceChanged("a")
	})

	autocomplete_b = new google.maps.places.Autocomplete(document.getElementById("id-google-address-b"), {
		types: ["address"],
		componentRestrictions: { country: ["usa"] },
	})

	autocomplete_b.addListener("place_changed", function () {
		onPlaceChanged("b")
	})
}

function geocodeAndSetValues(address, latId, longId) {
	var geocoder = new google.maps.Geocoder()
	geocoder.geocode({ address: address }, function (results, status) {
		if (status === google.maps.GeocoderStatus.OK) {
			var latitude = results[0].geometry.location.lat()
			var longitude = results[0].geometry.location.lng()

			document.getElementById(latId).value = latitude
			document.getElementById(longId).value = longitude
		}
	})
}

function onPlaceChanged(addy) {
	let auto
	let elId
	let latId
	let longId

	if (addy === "a") {
		auto = autocomplete_a
		elId = "id-google-address-a"
		latId = "id-lat-a"
		longId = "id-long-a"
	} else {
		auto = autocomplete_b
		elId = "id-google-address-b"
		latId = "id-lat-b"
		longId = "id-long-b"
	}

	var address = document.getElementById(elId).value
	geocodeAndSetValues(address, latId, longId)
}

async function CalcRoute() {
	const startAddress = document.getElementById("id-google-address-a").value
	const endAddress = document.getElementById("id-google-address-b").value
	if (startAddress.value != "" && endAddress.value != "") {
		let lat_a, lat_b, long_a, long_b
		var geocoder = new google.maps.Geocoder()
		await geocoder.geocode({ address: startAddress }, function (results, status) {
			if (status === google.maps.GeocoderStatus.OK) {
				lat_a = results[0].geometry.location.lat()
				long_a = results[0].geometry.location.lng()
			}
		})
		await geocoder.geocode({ address: endAddress }, function (results, status) {
			if (status === google.maps.GeocoderStatus.OK) {
				lat_b = results[0].geometry.location.lat()
				long_b = results[0].geometry.location.lng()
			}
		})
		if (!lat_a || !lat_b || !long_a || !long_b) return

		var params = {
			lat_a: lat_a,
			long_a: long_a,
			lat_b: lat_b,
			long_b: long_b,
		}

		var esc = encodeURIComponent
		var query = Object.keys(params)
			.map((k) => esc(k) + "=" + esc(params[k]))
			.join("&")

		var url = "/study/directions?" + query
		window.location.assign(url)
	}
}

function calculateAndDisplayRoute(directionsService, directionsDisplay) {
	directionsService.route(
		{
			origin: origin,
			destination: destination,
			travelMode: "WALKING",
		},
		function (response, status) {
			if (status === "OK") {
				directionsDisplay.setDirections(response)
			} else {
				alert("Directions request failed due to " + status)
			}
		}
	)
}

document.addEventListener("DOMContentLoaded", function () {
	const directionsForm = document.getElementById("directions-form")

	directionsForm.addEventListener("submit", function (event) {
		event.preventDefault()
		CalcRoute()
	})
})

window.initMap = initMap