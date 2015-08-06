function initialize() {

    // Import mapstyles from external .js file
    // Create a new StyledMapType object, passing it the array of styles,
    // as well as the name to be displayed on the map type control.
    var styledMap = new google.maps.StyledMapType(
        MAPSTYLES,
        {name: "Custom Style"}
    );

    // Create a map object, and include the MapTypeId to add
    // to the map type control.
    var mapOptions = {
        zoom: 5,
        center: new google.maps.LatLng(70, -148),
        zoomControl: true,
        panControl: false,
        streetViewControl: false,
        mapTypeControlOptions: {
            mapTypeIds: [google.maps.MapTypeId.ROADMAP, 'map_style']
        }
    };

    // Identify div in which to display map
    var map = new google.maps.Map(
        document.getElementById('single-map'),
        mapOptions);

    // Associate the styled map with the MapTypeId and set it to display.
    map.mapTypes.set('map_style', styledMap);
    map.setMapTypeId('map_style');

    // Define global infoWindow
    // If you do this inside the loop, the windows do
    // not automatically close when a new marker is clicked
    var infoWindow = new google.maps.InfoWindow({
        width: 100
    });

    // Retrieving the information with AJAX
    $.get('/bears.json', function (bears) {
        // Attach markers to each bear location in returned JSON
        var bear, marker, contentString;

        for (var key in bears) {
            bear = bears[key];

            // Define the marker
            marker = new google.maps.Marker({
                position: new google.maps.LatLng(bear.capLat, bear.capLong),
                map: map,
                title: 'Bear ID: ' + bear.bearId,
                icon: '/static/img/white-marker.png'
            });

            // Define the content of the infoWindow
            contentString = (
                '<div class="window-content">' +
                    '<p><b>Bear gender: </b>' + bear.gender + '</p>' +
                    '<p><b>Bear birth year: </b>' + bear.birthYear + '</p>' +
                    '<p><b>Year captured: </b>' + bear.capYear + '</p>' +
                    '<p><b>Collared: </b>' + bear.collared + '</p>' +
                    '<p><b>Location: </b>' + marker.position + '</p>' +
                '</div>');

            // Inside the loop we call bindInfoWindow passing it the marker,
            // map, infoWindow and contentString
            bindInfoWindow(marker, map, infoWindow, contentString);
        }

    });

    // This function is outside the for loop.
    // When a marker is clicked it closes any currently open infowindows
    // Sets the content for the new marker with the content passed through
    // then it open the infoWindow with the new content on the marker that's clicked
    function bindInfoWindow(marker, map, infoWindow, html) {
        google.maps.event.addListener(marker, 'click', function () {
            infoWindow.close();
            infoWindow.setContent(html);
            infoWindow.open(map, marker);
        });
    }
}

google.maps.event.addDomListener(window, 'load', initialize);
