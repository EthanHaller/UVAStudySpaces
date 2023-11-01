$.getScript("https://maps.googleapis.com/maps/api/js?key=" + window.key + "&callback=initMap&v=weekly&libraries=places").done(function (script, textStatus) {
	google.maps.event.addListener(window, "load", initMap)
})

function initMap() {
	map = new google.maps.Map(document.getElementById("map"), {
		center: { lat: 38.03413872243867, lng: -78.50873523191473 },
		zoom: 16,
	})

	const navbarHeight = document.getElementById("global-navbar").offsetHeight
	const mapHeight = `calc(100vh - ${navbarHeight}px)`
	document.getElementById("map-container").style.height = mapHeight
	document.getElementById("list-container").style.maxHeight = `calc(${mapHeight} - 48px)`

	const modData = window.modJson
	const markers = modData.map((i) => {
		const marker = new google.maps.Marker({
			position: { lat: parseFloat(i.latitude), lng: parseFloat(i.longitude) },
			map: map,
		})
		marker.addListener("click", (this) => {
			markerClicked(this)
			map.setZoom(18)
			map.setCenter(marker.getPosition())

			modData.forEach((element) => {
				const card = document.getElementById("study-card-id-" + element.id)
				card.style.backgroundColor = null
				card.style.borderColor = null
			})

			const card = document.getElementById("study-card-id-" + i.id)
			card.style.backgroundColor = "#F5F5F5"
			card.style.borderColor = "#8BC34A"
		})
	})
}

function markerClicked(this) {
	console.log(this)
	console.log(this.id)
}

window.initMap = initMap
