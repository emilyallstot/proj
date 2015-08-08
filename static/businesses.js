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
        zoom: 13,
        center: new google.maps.LatLng(37.77018, -122.44259),
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
    $.get('/businesses.json', function (businesses) {
        // Attach markers to each business location in returned JSON
        var business, marker, contentString;

        for (var yelp_id in businesses) {
            business = businesses[yelp_id];

            // Define the marker
            marker = new google.maps.Marker({
                position: new google.maps.LatLng(business.bus_lat, business.bus_long),
                map: map,
                title: 'Business name: ' + business.business_name,
                icon: '/static/img/nails-small.png'
            });

            // Define the content of the infoWindow
            contentString = (
                '<div class="window-content">' +
                    '<p><b>Address: </b>' + business.address + '</p>' +
                    '<p><b>Phone: </b>' + business.phone + '</p>' +
                    '<p><b>MAKE A HYPERLINK HERE BLAHHHHHH ID IS    ' + business.yelp_id +
                    ' MORE INFO </b></a></p>' +
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
