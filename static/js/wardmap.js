// var user_role = "{{ user_role }}"; // Assuming you are passing the user role from Django

// var selectedLayers = {}; // Initialize an empty object to hold the selected layers

// // Define base layers
// var baseLayers = {
//   OSM: osm,
//   ESRI: Esri_WorldImagery,
//   GoogleImage: googleSat,
// };

// // Define WMS layers
// var wmsLayers = {
//   "Pune Admin Wards": wms_layer,
//   "PMC Missing Link Buffer": wms_layer2,
//   "PMC Missing Links": wms_layer3,
//   "PMC Roads": wms_layer4,
//   "DP Roads Buffer": wms_layer7,
//   "DP Roads": wms_layer6,
//   "Missing Link": wms_layer5,
//   "DProamosaic": wms_layer1,
// };

// // If the user is not an admin, show only selected layers
// if (user_role !== "admin") {
//   selectedLayers = {
//     "PMC Roads": wms_layer4,
//     "Missing Link": wms_layer5,
//     "PMC Missing Links": wms_layer3,
//     // Add other layers for non-admin here
//   };
// }

// // Create the Leaflet map
// var map = L.map("map", {
//   layers: [osm], // Set a default base layer
// }).setView([18.53, 73.85], 12, L.CRS.EPSG4326);

// // Add control for selecting layers
// L.control.layers(baseLayers, user_role === "admin" ? wmsLayers : selectedLayers).addTo(map);



// ==================================================
// MAP
var map, geojson;

//Add Basemap
var map = L.map("map", {}).setView([18.53, 73.85], 12, L.CRS.EPSG4326);

var osm = L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
  attribution:
    '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
});

var googleSat = L.tileLayer(
  "http://{s}.google.com/vt/lyrs=s&x={x}&y={y}&z={z}",
  {
    maxZoom: 35,
    subdomains: ["mt0", "mt1", "mt2", "mt3"]
  }
);


var Esri_WorldImagery = L.tileLayer(
  "https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}",
  {
    attribution:
      "Tiles &copy; Esri &mdash; Source: Esri, i-cubed, USDA, USGS, AEX, GeoEye, Getmapping, Aerogrid, IGN, IGP, UPR-EGP, and the GIS User Community"
  }
);
// <!-- -----------------layer displayed------------------------ -->
var baseLayers = {
  OSM: osm,
  ESRI: Esri_WorldImagery,
  GoogleImage: googleSat,
  
};

var wms_layer = L.tileLayer.wms(
  "https://portal.geopulsea.com/geoserver/PMC/wms",
  {
    layers: "PMC:pune-admin-wards",
    format: "image/png",
    transparent: true,
    version: "1.1.0",
    attribution: "pune-admin-wards"
  }
);


var wms_layer2 = L.tileLayer.wms(
  "https://portal.geopulsea.com/geoserver/PMC/wms",
  {
    layers: "PMC:PMC_Missing_Link_Buffer",
    format: "image/png",
    transparent: true,
    version: "1.1.0",
    attribution: "PMC_Missing_Link_Buffer"
  }
);

var wms_layer3 = L.tileLayer.wms(
  "https://portal.geopulsea.com/geoserver/PMC/wms",
  {
    layers: "PMC:PMC_Missing_Links",
    format: "image/png",
    transparent: true,
    version: "1.1.0",
    attribution: "PMC_Missing_Links"
  }
);

var wms_layer4 = L.tileLayer.wms(
  "https://portal.geopulsea.com/geoserver/PMC/wms",
  {
    layers: "PMC:PMCroads",
    format: "image/png",
    transparent: true,
    version: "1.1.0",
    attribution: "PMCroads"
  }
);

var wms_layer7 = L.tileLayer.wms(
  "https://portal.geopulsea.com/geoserver/PMC/wms",
  {
    layers: "PMC:DP_Roads_Buffer",
    format: "image/png",
    transparent: true,
    version: "1.1.0",
    attribution: "DP_Roads_Buffer"
  }
);

var wms_layer6 = L.tileLayer.wms(
  "https://portal.geopulsea.com/geoserver/PMC/wms",
  {
    layers: "PMC:DP_Roads",
    format: "image/png",
    transparent: true,
    version: "1.1.0",
    attribution: "DP_Roads"
  }
);



// osm.addTo(map)
wms_layer.addTo(map)


var wms_layer5 = L.tileLayer.wms(
  "https://portal.geopulsea.com/geoserver/PMC/wms",
  {
    layers: "PMC:missinglink",
    format: "image/png",
    transparent: true,
    version: "1.1.0",
    attribution: "missinglink"
  }
);

var wms_layer1 = L.tileLayer.wms(
  "https://portal.geopulsea.com/geoserver/PMC/wms",
  {
    layers: "PMC:DProamosaic",
    format: "image/png",
    transparent: true,
    version: "1.1.0",
    attribution: "DProamosaic"
  }
);
// osm.addTo(map)
wms_layer.addTo(map)



var WMSlayers = {
  
  // Pune_admin_wards: wms_layer,
  DProamosaic:wms_layer1,
  PMCroads:wms_layer4,

  missinglink:wms_layer5,
  
  PMC_Missing_Link: wms_layer3,
  PMC_Missing_Link_Buffer: wms_layer2,
 
  DP_Roads_Buffer:wms_layer7,
  DP_Roads:wms_layer6,
  


};
var control = new L.control.layers(baseLayers, WMSlayers).addTo(map);

//===================================================

//<!-- googleEarth popup -->

map.on("dblclick", function (e) {
  var lat = e.latlng.lat.toFixed(15);
  var lng = e.latlng.lng.toFixed(15);
  var popupContent =
    '<a href="https://earth.google.com/web/search/' +
    lat +
    "," +
    lng +
    '" target="_blank">Open in Google Earth</a><br>' + 'Latitude : ' + lat + '<br>' + 'Longitude : ' + lng 
  L.popup().setLatLng(e.latlng).setContent(popupContent).openOn(map);
});


//**************************************************line mesure*************************************************************
L.control
  .polylineMeasure({
    position: "topright",
    unit: "kilometres",
    showBearings: true,
    clearMeasurementsOnStop: false,
    showClearControl: true,
    showUnitControl: true
  })
  .addTo(map);

//**********************************************************area measure**********************************************************************
// var measureControl = new L.Control.Measure({
//   position: "topright"
// });
// measureControl.addTo(map);

// var measureAction = new L.MeasureAction(map, {
//     model: "distance", // 'area' or 'distance', default is 'distance'
// });
// // measureAction.setModel('area');
// measureAction.enable();

// L.Measure = {
//   linearMeasurement: "Distance measurement",
//   areaMeasurement: "Area measurement",
//   // start: "开始",
//    position: "topright",
//   meter: "m",
//   kilometer: "km",
//   squareMeter: "m²",
//   squareKilometers: "km²",
//   };

  var measure = L.control.measure({}).addTo(map);

/////////////////////////north image
var north = L.control({
  position: "bottomright"
});
north.onAdd = function (map) {
  var div = L.DomUtil.create("div", "info legend");
  var imageUrl = northImageUrl;
  div.innerHTML =
    '<img src="' + imageUrl + '" style="height: 20px; width: 30px;">';
  return div;
};
north.addTo(map);

(uri =
  "https://portal.geopulsea.com/geoserver/PMC/wms?REQUEST=GetLegendGraphic&VERSION=1.0.0&FORMAT=image/png&WIDTH=20&HEIGHT=20&LAYER=topp:states"), {
  // namedToggle: false,
};
L.wmsLegend(uri);
//

// control
// mouse position

//******************************************************************Scale***************************************************************

L.control
  .scale({
    imperial: false,
    maxWidth: 200,
    metric: true,
    position: "bottomleft",
    updateWhenIdle: false
  })
  .addTo(map);

// search-button______________________________________
$(document).ready(function () {


  var geojsonLayer; // Reference to the GeoJSON layer
  var geojsonFeatures = []; // Array to store GeoJSON features

  $("#btnData2").click(function () {
    var selectedValue = $("#search-input").val();



    $.ajax({
      url: "/searchOnClick/",
      method: "GET",
      data: { "selected_value": selectedValue },
      dataType: "json",
      success: function (response) {


        geojsonFeatures = response.features;

        if (geojsonLayer) {
          geojsonLayer.removeFrom(map);
        }

        // Process the response data here
        geojsonLayer = L.geoJSON(response).addTo(map);


        map.fitBounds(geojsonLayer.getBounds());

      },
      error: function (error) {
      }
    });
  });
});


$("#btnData1").click(function () {
  ClearMe();
});

function ClearMe() {
  map.setView([18.55, 73.85], 10, L.CRS.EPSG3857)
};



map.on("contextmenu", (e) => {
  let size = map.getSize();
  let bbox = map.getBounds().toBBoxString();


  var container = document.querySelector('.leaflet-control-layers-overlays');

  var checkboxes = container.querySelectorAll('.leaflet-control-layers-selector');

  var checkedValues = [];

  checkboxes.forEach(function (checkbox) {
    // Check if the checkbox is checked
    if (checkbox.checked) {
      // Get the label text associated with the checkbox
      var labelText = checkbox.nextElementSibling.textContent.trim();
      checkedValues.push(labelText);
    }
  });

  // Display the checked values

  let layer = 'zone:' + checkedValues;
  let style = 'zone:' + checkedValues;
  let urrr =
    `https://portal.geopulsea.com/geoserver/PMC/wms?SERVICE=WMS&VERSION=1.1.1&REQUEST=GetFeatureInfo&FORMAT=image%2Fpng&TRANSPARENT=true&QUERY_LAYERS=${layer}&STYLES&LAYERS=${layer}&exceptions=application%2Fvnd.ogc.se_inimage&INFO_FORMAT=application/json&FEATURE_COUNT=50&X=${Math.round(e.containerPoint.x)}&Y=${Math.round(e.containerPoint.y)}&SRS=EPSG%3A4326&WIDTH=${size.x}&HEIGHT=${size.y}&BBOX=${bbox}`


  // `https://portal.geopulsea.com/geoserver/PMC/wms?service=WMS&version=1.1.0&request=GetMap&layers=zone%3AVillage_Boundary&bbox=73.31581115722656%2C18.128164291381836%2C74.46541595458984%2C18.988113403320312&width=768&height=574&srs=EPSG%3A4326&styles=&format=application/openlayers`

  // you can use this url for further processing such as fetching data from server or showing it on the map

  /////////////////////////////
let geojsonLayer;


  if (urrr) {
    fetch(urrr)


      .then((response) => response.json()) // Parse the JSON response
      .then((data) => {

        geojsonLayer = L.geoJSON(data).addTo(map); // Create a GeoJSON layer


        map.fitBounds(geojsonLayer.getBounds()); // Fit the map to the GeoJSON layer bounds

      });

    if (geojsonLayer) {
      geojsonLayer.removeFrom(map);
    }
  }
  ////////////////////////////////////////////

  if (urrr) {
    fetch(urrr)

      .then((response) => response.json())
      .then((html) => {

        // Assuming the ID is a direct property within the JSON data

        const id = html.features[0].properties.ID;
        // Now you can use the 'id' variable as needed

        var htmldata = html.features[0].properties;
        let keys = Object.keys(htmldata);
        let values = Object.values(htmldata);
        let txtk1 = "";
        var xx = 0
        for (let gb in keys) {
          txtk1 += "<tr><td>" + keys[xx] + "</td><td>" + values[xx] + "</td></tr>"
            ;

          xx += 1

        };
        let detaildata1 =

          `<div><table  style='width:100%;' class='popup-table' > 


                  <tr>

                  

                  <a href='/Queryform'><input type="button" id='data' class='btn btn-outline-success' style='width:100%' value="Add Information"></a>
                  
                  
                </tr>

                  ${txtk1}  <tr><td>Co-Ordinates</td><td>  ${e.latlng} 
                      </td></tr> <tr><td>Co-Ordinates</td><td>  ${e.latlng} 
                      </td></tr></table></div>`






        L.popup()
          .setLatLng(e.latlng)
          .setContent(detaildata1)
          .openOn(map);




      });

  };




});



// //pdf____________________________________________________________

L.control.browserPrint({title: 'Print ...' ,outputFormat: 'pdf',printModes: [L.BrowserPrint.Mode.Landscape("A3",{title: "Tabloid VIEW"})] }).addTo(map);


// Bookmark_____________________________________________________________________
$(document).ready(function () {
  var saveBtn = document.getElementById('saveBtn');

  saveBtn.addEventListener('click', function () {
    var center = map.getCenter(); // Get the center of the map
    var latitude = center.lat;
    var longitude = center.lng;

    // Show popup for entering location name
    Swal.fire({
      title: 'Enter Location Name',
      input: 'text',
      inputPlaceholder: 'Location Name',
      showCancelButton: true,
      confirmButtonText: 'Save',
      showLoaderOnConfirm: true,
      preConfirm: function (name) {
        return new Promise(function (resolve, reject) {
          if (name) {
            resolve(name);
          } else {
            reject('Invalid name');
          }
        });
      },

      allowOutsideClick: false,
      customClass: {
        title: 'my_swal_title',
        container: 'my-swal-container', // CSS class for the container
        confirmButton: 'my-swal-button', // CSS class for the confirm button
        cancelButton: 'my-swal-button', // CSS class for the cancel button
        input: 'my-swal-input', // CSS class for the input field
      },
    }).then(function (name) {
      if (name.isConfirmed) {
        var locationName = name.value;
        var username = '{{ request.user.username }}'; // Assuming you are using Django's authentication system

        saveLocationToDB(latitude, longitude, locationName, username);
      }
    }).catch(function (error) {
      Swal.showValidationMessage(error);
    });
  });

  function saveLocationToDB(latitude, longitude, locationName, username) {
    $.ajax({
      url: '/save-location/',
      method: 'POST',
      data: {
        latitude: latitude,
        longitude: longitude,
        name: locationName,
        username: username
      },
      success: function (response) {
      },
      error: function (xhr, errmsg, err) {
      }
    });
  }

  $(document).on('click', '#locationTable td.name', function () {
    var latitude = parseFloat($(this).data('latitude'));
    var longitude = parseFloat($(this).data('longitude'));
    map.flyTo([latitude, longitude], 17);
  });
  // for zoom
  function fetchLocations() {
    $.ajax({
      url: "/get-locations/",
      method: "GET",
      success: function (response) {
        var locations = response.locations;
        var tableBody = $("#locationTable tbody");
        tableBody.empty();

        $.each(locations, function (index, location) {
          var row = $("<tr>");
          row.data("location-id", location.id); // Store the location ID in the row data attribute
          $("<td>", {
            class: "name",
            text: location.name,
            "data-latitude": location.latitude,
            "data-longitude": location.longitude,
          }).appendTo(row);
          // $("<td>", { text: location.latitude }).appendTo(row);
          // $("<td>", { text: location.longitude }).appendTo(row);
          var deleteButton = $("<button>", { text: "Delete" });
          var deleteButtonWrapper = $("<td>", {
            class: "delete-button",
          }).append(deleteButton);
          row.append(deleteButtonWrapper);
          row.appendTo(tableBody);
        });
      },
      error: function (xhr, errmsg, err) {
      },
    });
  }


  // for Delete
  $(document).on("click", ".delete-button button", function () {
    var row = $(this).closest("tr");
    var locationId = row.data("location-id");

    Swal.fire({
      title: "Confirm Deletion",
      text: "Are you sure you want to delete this location?",
      icon: "warning",
      showCancelButton: true,
      confirmButtonColor: "#dc3545",
      confirmButtonText: "Delete",
      cancelButtonText: "Cancel",
      reverseButtons: true,
      customClass: {
        text: "my_swal_text",
        title: "my_swal_title",
        icon: "my_icon",
        container: "my-swal-delete-container",
        confirmButton: "my-swal-button",
        cancelButton: "my-swal-button",
        actions: "my-swal-actions",
      },
    }).then(function (result) {
      if (result.isConfirmed) {
        deleteLocationFromDB(locationId, row);
      }
    });
  });

  function deleteLocationFromDB(locationId, row) {
    $.ajax({
      url: "/delete-location/",
      method: "POST",
      data: {
        locationId: locationId,
      },
      success: function (response) {
        row.remove(); // Remove the deleted row from the table
      },
      error: function (xhr, errmsg, err) {
      },
    });
  }

  fetchLocations();
  setInterval(fetchLocations, 1000);
});





// ***************************************************************Make QUery***************************************************************

$("#button").click(function () {
  $("#boxattribute form").toggle("slow");
  $(document).ready(function () {
    $.ajax({
      type: "GET",
      url: "https://portal.geopulsea.com/geoserver/PMC/wms?request=getCapabilities",
      dataType: "xml",
      success: function (xml) {
        var select1 = $('#layer');

        $(xml).find('FeatureType').each(function () {
          $(this).find('Name').each(function () {
            var value = $(this).text();
            select1.append(
              "<option class='ddindent' value='" +
              value + "'>" + value + "</option>");
          }); 
        }); 
      }
    });
  });

  $(function () {
    $("#layer").change(function () {
      var attributes = document.getElementById("attributes");
      var length = attributes.options.length;
      for (i = length - 1; i >= 0; i--) {
        attributes.options[i] = null;
      }
      console.log("lennnnnnnnnnnnnnnnnn", length)
      var value_layer1 = $(this).val();
      console.log("hhhhhhhhhhhhhhh", value_layer1)
      $(document).ready(function () {
        $.ajax({
          type: "GET",
          url: "https://portal.geopulsea.com/geoserver/PMC/wms?service=WFS&request=DescribeFeatureType&version=1.1.0&typeName=" +
            value_layer1,
          dataType: "xml",

          

          success: function (xml) {



            var select2 = $('#attributes');
            $(xml).find('xsd\\:sequence').each(function () {
              $(this).find('xsd\\:element').each(
                function () {
                  var value = $(this)
                    .attr('name');
                  var type = $(this).attr(
                    'type');
                  if (value != 'geom' &&
                    value != 'the_geom'
                  ) {
                    select2.append(
                      "<option class='ddindent' value='" +
                      type +
                      "'>" +
                      value +
                      "</option>");
                  }
                });
            });
          }
        })
      });
      document.getElementById("textval").innerHTML = value_layer1;
      console.log("data",value_layer1)
    })
  });
 
  $(function () {
    $("#attributes").change(function () {
      var operator = document.getElementById("operator");
      var attributes = $("#layer option:selected").text();
      var length = operator.options.length;
      for (i = length - 1; i >= 0; i--) {
        operator.options[i] = null;
      }
      var value_type = $(this).val();
      var value_attribute = $('#attributes option:selected').text();
      operator.options[0] = new Option('Select operator', "");
      if (value_type == 'xsd:short' || value_type == 'xsd:int' || value_type ==
        'xsd:double') {
        var operator1 = document.getElementById("operator");
        operator1.options[1] = new Option('>', '>');
        operator1.options[2] = new Option('<', '<');
        operator1.options[3] = new Option('=', '=');
        operator1.options[4] = new Option('<=', '<=');
        operator1.options[5] = new Option('=>', '=>');
        operator1.options[6] = new Option('IN ()', 'IN');
        operator1.options[7] = new Option('OR ||', 'OR');
        operator1.options[8] = new Option('AND &', 'AND');
      } else if (value_type == 'xsd:string') {
        var operator1 = document.getElementById("operator");
        operator1.options[1] = new Option('Like', 'ILike');
        operator1.options[2] = new Option('IN ()', 'IN');
        operator1.options[3] = new Option('OR ||', 'OR');
        operator1.options[4] = new Option('AND &', 'AND');
      }


      var selectvalue = document.getElementById("selectvalue");
      console.log("hhhh", selectvalue)
      var length = selectvalue.options.length;
      for (i = length - 1; i >= 0; i--) {
        selectvalue.options[i] = null;
      }

      $(document).ready(function () {
        $.ajax({
          type: "GET",
          url: "https://portal.geopulsea.com/geoserver/PMC/wms?service=wfs&version=1.0.0&request=getfeature&typename=" +
            attributes + "&PROPERTYNAME=" + value_attribute,
          dataType: "xml",
          
          success: function (xml) {
            var select3 = $('#selectvalue');
            var unq = new Array();
            $(xml).each(function () {
              $(this).find('gml\\:featureMember')
                .each(function () {
                  unq.push($(this)
                    .text());
                });
              let unique = unq.filter((item, i,
                ar) => ar.indexOf(
                  item) === i);
              for (let i = 0; i < unique
                .length; i++) {
                select3.append(
                  "<option class='ddindent' value='" +
                  unique[i] + "'>" +
                  unique[i] + "</option>");
                  console.log(select3)
              }
            });
          }
        });
      });
      document.getElementById("textval").innerHTML = "From Layer" + attributes +
        " is " + value_attribute;
    });

  });
});



$(function () {
  $("#selectvalue").change(function () {
    var vars = ['layer', 'attributes', 'operator', 'selectvalue'];
    for (let i = 0; i < vars.length; i++) {
      //   var operator = document.getElementById("operator");
      var layer = $("#layer option:selected").text();
      var attributes = $("#attributes option:selected").text();
      var operator = $("#operator option:selected").text();
      var selectvalue = $("#selectvalue option:selected").text();
    }

   
    
    document.getElementById("textval").innerHTML = "From Layer " + layer + " column is " +
      attributes + " " + operator + " value is " + selectvalue;

    var sql_filter1 = attributes + " Like '" + selectvalue + "'"
    fitbou(sql_filter1, layer)

    var wms_layerf = L.tileLayer.wms(
      "https://portal.geopulsea.com/geoserver/PMC/wms", {
      layers: layer,
      format: "image/png",
      transparent: true,
      tiled: true,
      version: "1.1.0",
      attribution: "ugc",
      opacity: 1,
      cql_filter: sql_filter1,
      styles: 'highlight',

    }
    );
    wms_layerf.addTo(map);
   
    
    function fitbou(filter, layer1) {
      var urlm =
        "https://portal.geopulsea.com/geoserver/PMC/wms?service=WFS&version=1.0.0&request=GetFeature&typeName=" +
        layer1 + "&CQL_FILTER=" + filter + "&outputFormat=application/json";
        // console.log("data",urlm)
      $.getJSON(urlm, function (data) {
        var customStyle = {
          color: "red", // Change this to your desired highlight color
          weight: 2,
          opacity: 1,
          fillOpacity: 0.5,
        };
      /////////////////////////////////
      /////////////////////////////////
      /////////////////////////////////
      /////////////////////////////////

    
      //  console.log("get_json",data)
      
$(document).ready(function() {
        $.getJSON(urlm, function(data) {
          if (data.features.length > 0) {
            // Loop through each feature
            data.features.forEach(function(feature) {
              var id = feature.properties.ID;
              
              var length_m = feature.properties.Length_m;
              
              var missing_existing = feature.properties.Missing_Existing;
              
              var name = feature.properties.Name;
              
             
              
              var road_width = feature.properties.Road_width;
              
              var shape_length = feature.properties.Shape_Length;
              
              var ward_num = feature.properties.wardnum;
      
              // Create a new row
              var newRow = $("<tr>");
      
              // Append cells with data
              newRow.append("<td>" + id + "</td>");
              newRow.append("<td>" + length_m + "</td>");
              newRow.append("<td>" + missing_existing + "</td>");
              newRow.append("<td>" + name + "</td>");
            
              newRow.append("<td>" + road_width + "</td>");
              newRow.append("<td>" + shape_length + "</td>");
              newRow.append("<td>" + ward_num + "</td>");
      
              // Append the row to the table
              $("#other-data-table tbody").append(newRow);
            });
      
            // Show the table after data is ready
            $('#other-data-table').show();
          }
        });
      });
      



     /////////////////////////////////
      /////////////////////////////////
      /////////////////////////////////
      /////////////////////////////////

        if (geojson) {
          map.removeLayer(geojson);
        }
        geojson = L.geoJson(data, {
          style: customStyle,
        });console.log(geojson,"aaaaaaaaaa")

        geojson.addTo(map);
       
        map.fitBounds(geojson.getBounds());
      });
    };


  });
})

////////////////////////////////////////select by location////////////////////////////


$("#btnLocation").click(function () {
  $("#boxLocation form").toggle("slow");

  $(document).ready(function () {
    $.ajax({
      type: "GET",
      url: "https://portal.geopulsea.com/geoserver/PMC/wms?request=getCapabilities",
      dataType: "xml",
      success: function (xml) {
        var selectSource = $('#sourceLayer');
        var selectTarget = $('#targetLayer')

        $(xml).find('FeatureType').each(function () {
          $(this).find('Name').each(function () {
            var value = $(this).text();
            selectSource.append(
              "<option class='ddindent' value='" +
              value + "'>" + value + "</option>");
            selectTarget.append("<option class='ddindent' value='" +
              value + "'>" + value + "</option>")
          });
        }); 
      }
    }); 
  });


})



$(function () {
  $("#sourceLayer").change(function () {
    var value_layer1 = $(this).val();
    console.log("Selected sourceLayer: " + value_layer1);

    // Clear existing options in the attributeLayer dropdown
    var attributeLayers = $("#attributeLayer");
    attributeLayers.empty();

    // Perform an AJAX request to fetch attributes based on the selected sourceLayer
    $.ajax({
      type: "GET",
      url: "https://portal.geopulsea.com/geoserver/PMC/wms?service=WFS&request=DescribeFeatureType&version=1.1.0&typeName=" +
        value_layer1,
      dataType: "xml",
      success: function (xml) {
        var select2 = $('#attributeLayer');

        // Find elements with the specified 'sourceLayer' attribute
        $(xml).find('[sourceLayer]').each(function () {
          var sourceLayer = $(this).attr('sourceLayer');

          // You can customize how you want to determine the attribute name based on 'sourceLayer'
          // Here, we simply use 'sourceLayer' as the attribute name
          var attributeName = sourceLayer;

          // Find elements with the dynamically determined attribute name
          $(this).find('xsd\\:element').each(function () {
            var value = $(this).attr('name');
            var type = $(this).attr('type');
            if (value != 'geom' && value != 'the_geom') {
              select2.append(
                "<option class='ddindent' value='" +
                type +
                "'>" +
                value +
                "</option>"
              );
            }
          });
        });
      }
    });

    // Update the textval element with the selected sourceLayer
    $("#textval").text("Selected sourceLayer: " + value_layer1);
  });
});


var geojsonLayer; // Reference to the GeoJSON layer
 



$("#loadqueryLocation").click(function () {
  var sourceValue = $("#sourceLayer").val();
  var targetLayerName = $("#targetLayer").val();
  var selectTypeValue = $("#selectType").val();

  console.log("Selected Value:", sourceValue, targetLayerName, selectTypeValue);
  if (geojsonLayer) {
    map.removeLayer(geojsonLayer); // Remove the previous GeoJSON layer
  }
  


  $.ajax({
    url: "/select_by_location/",
    method: "GET",
    data: {
      "selected_value": sourceValue,
      'targetLayer': targetLayerName,
      'selectTypeValue': selectTypeValue,
    },
  
    dataType: "json",
  
    success: function (response) {
    
  try {
    // Parse the GeoJSON data if it's a JSON string
    var geojsonData = typeof response === 'string' ? JSON.parse(response) : response;





///////////////////// by anup ////////////////////////

geojsonData.features.forEach(function (feature) {
  var properties = feature.properties;

//id_left,Ward_Name_right,Road_width


//,Ward_Name_left,Name_1Ward_Name_right,Road_Buffer,BUFF_DIST,ORIG_FID,Shape_Length,Shape_Area,index_right,id_right,name,Ward_Name_right

  var id = properties.id_left;
  var Ward_Name_right = properties.Ward_Name_right;
  var Road_width = properties.Road_width;
  var Ward_Name_left = properties.Ward_Name_left;
  var Name_1Ward_Name_right = properties.Name_1Ward_Name_right;
  var Road_Buffer = properties.Road_Buffer;
  var BUFF_DIST = properties.BUFF_DIST;
  var ORIG_FID = properties.ORIG_FID;
  var Shape_Length = properties.Shape_Length;
  var Shape_Area = properties.Shape_Area;
  var index_right = properties.index_right;
  var id_right = properties.id_right;
  var name = properties.name;

  // Extract the numeric part of the id
  var numericId = id.split('.')[1]; // Split the id at '.' and take the second part


  // Create a new table row
  var newRow = document.createElement("tr");

  // Create table data cells for Ward Name, Road Width, and Geometry

  var idCell = document.createElement("td");
  idCell.textContent = numericId;

  var wardNameCell = document.createElement("td");
  wardNameCell.textContent = Ward_Name_right;


  var roadWidthCell = document.createElement("td");
  roadWidthCell.textContent = Road_width;

  var Ward_Name_leftCell = document.createElement("td");
  Ward_Name_leftCell.textContent = Ward_Name_left;

  var Name_1Ward_Name_rightCell = document.createElement("td");
  Name_1Ward_Name_rightCell.textContent = Name_1Ward_Name_right;
  
  var Road_BufferCell = document.createElement("td");
  Road_BufferCell.textContent = Road_Buffer;

  var BUFF_DISTCell = document.createElement("td");
  BUFF_DISTCell.textContent = BUFF_DIST;

  var ORIG_FIDCell = document.createElement("td");
  ORIG_FIDCell.textContent = ORIG_FID;

  var Shape_LengthCell = document.createElement("td");
  Shape_LengthCell.textContent = Shape_Length;

  var Shape_AreaCell = document.createElement("td");
  Shape_AreaCell.textContent = Shape_Area;

  var index_rightCell = document.createElement("td");
  index_rightCell.textContent = index_right;

  var id_rightCell = document.createElement("td");
  id_rightCell.textContent = id_right;

  var nameCell = document.createElement("td");
  nameCell.textContent = name;

  // Append the cells to the row
  newRow.appendChild(idCell);
  newRow.appendChild(wardNameCell);
  newRow.appendChild(roadWidthCell);

  newRow.appendChild(Ward_Name_leftCell);
  newRow.appendChild(Name_1Ward_Name_rightCell);
  newRow.appendChild(Road_BufferCell);
  newRow.appendChild(BUFF_DISTCell);
  newRow.appendChild(ORIG_FIDCell);
  newRow.appendChild(Shape_LengthCell);
  newRow.appendChild(Shape_AreaCell);
  newRow.appendChild(index_rightCell);
  newRow.appendChild(id_rightCell);
  newRow.appendChild(nameCell);




  // Append the row to the table's tbody
  var tbody = document.querySelector("#data-table tbody");
  tbody.appendChild(newRow);
});


/////////////////////// end by anup //////////////////////



    // Process the response data here
    geojsonLayer = L.geoJSON(geojsonData, {
      style: function (feature) {
        // Customize the style for the selected data
        return {
          fillColor: 'transparent', // Change to your desired highlight color
          weight: 5,
          opacity: 1,
          color: 'orange',
          fillOpacity: 0.7
        };
      },
      onEachFeature: function (feature, layer) {
        // Add a popup for each feature (optional)
        layer.bindPopup("Property ID: " + feature.properties.id);
      }
    }).addTo(map);

    // Fit the map to the bounds of the GeoJSON layer
    map.fitBounds(geojsonLayer.getBounds());
  } catch (error) {
    console.error("Error parsing GeoJSON data:", error);
  }
},
error: function (error) {
  console.error("Error fetching GeoJSON data:", error);
}
// });

    // }
  });
});



///////////////// road id fit bound //////////////////////



///======== end ===================///


///////////////////////////////

var drawnItems = new L.FeatureGroup();
map.addLayer(drawnItems);

var markerEnabled = false;
var lineEnabled = true;
var polygonEnabled = true;
var circleEnabled = false;



function enableMarker() {
markerEnabled = true;
lineEnabled = false;
polygonEnabled = false;
circleEnabled = false;
map.off('click', onDrawLine);
map.off('click', onDrawPolygon);
map.off('click', onDrawCircle);
map.on('click', onMapClick);
}

function enableLine() {
lineEnabled = true;
markerEnabled = false;
polygonEnabled = false;
circleEnabled = false;
map.off('click', onMapClick);
map.off('click', onDrawPolygon);
map.off('click', onDrawCircle);
map.on('click', onDrawLine);
}

function onMapClick(e) {
if (markerEnabled) {
  var marker = new L.Marker(e.latlng);
  drawnItems.clearLayers();
  drawnItems.addLayer(marker);
}
}

var lineCoords = [];

function onDrawLine(e) {
if (lineEnabled) {
  lineCoords.push(e.latlng);
  var polyline = new L.Polyline(lineCoords);
  drawnItems.clearLayers();
  drawnItems.addLayer(polyline);
}
}

function enablePolygon() {
polygonEnabled = true;
markerEnabled = false;
lineEnabled = false;
circleEnabled = false;
map.off('click', onMapClick);
map.off('click', onDrawLine);
map.off('click', onDrawCircle);
map.on('click', onDrawPolygon);
}

var polygonCoords = [];

function onDrawPolygon(e) {
if (polygonEnabled) {
  polygonCoords.push(e.latlng);
  var polygon = new L.Polygon(polygonCoords);
  drawnItems.clearLayers();
  drawnItems.addLayer(polygon);
}
}


var circleDiameter = null;

function enableCircle() {
circleEnabled = true;
markerEnabled = false;
lineEnabled = false;
polygonEnabled = false;
map.off('click', onMapClick);
map.off('click', onDrawLine);
map.off('click', onDrawPolygon);
map.on('click', onDrawCirclePrompt);
}

var circleCenter = null;
var circleRadius = 0;

function onDrawCirclePrompt(e) {
  if (circleEnabled) {
      circleCenter = e.latlng;
      var diameter = prompt("Enter diameter of the circle (in meters):");
      if (diameter) {
          circleRadius = parseFloat(diameter) / 2;
          onDrawCircle(e);
      } else {
          circleCenter = null;
      }
  }
}

function onDrawCircle(e) {
  if (circleEnabled) {
      if (circleCenter && circleRadius > 0) {
          var circle = L.circle(circleCenter, {
              radius: circleRadius,
              color: 'blue',
              fill: false,
          });
          drawnItems.clearLayers();
          drawnItems.addLayer(circle);
          circleCenter = null;
          circleRadius = 0;
      }
  }
}


function getCircleLatLngs(center, radius) {
var latlngs = [];
var steps = 100;
for (var i = 0; i < steps; i++) {
    var angle = (i / steps) * Math.PI * 2;
    var x = center.lat + Math.cos(angle) * (radius / 40008000) * 360;
    var y = center.lng + Math.sin(angle) * (radius / 40008000) * 360;
    latlngs.push([x, y]);
}
return latlngs;
}



function onDrawCircle(e) {
if (circleEnabled) {
    if (circleCenter && circleRadius > 0) {
        var circleLatLngs = getCircleLatLngs(circleCenter, circleRadius);
        var circlePolygon = L.polygon(circleLatLngs, {
            color: 'blue',
            fill: false,
        });
        drawnItems.clearLayers();
        drawnItems.addLayer(circlePolygon);
        circleCenter = null;
        circleRadius = 0;
    }
}
}

function exportToKML() {
var layers = drawnItems.getLayers();
if (layers.length === 0) {
    alert("No features to export.");
    return;
}

var kml = '<?xml version="1.0" encoding="UTF-8"?>' +
    '<kml xmlns="http://www.opengis.net/kml/2.2">' +
    '<Document>';

layers.forEach(function (layer, index) {
    var geojsonFeature = layer.toGeoJSON();
    var coordinates = geojsonFeature.geometry.coordinates;

    kml += '<Placemark><name>Feature ' + (index + 1) + '</name>';

    if (geojsonFeature.geometry.type === 'Point') {
        kml += '<Point><coordinates>' + coordinates[0] + ',' + coordinates[1] + '</coordinates></Point>';
    } else if (geojsonFeature.geometry.type === 'LineString') {
        kml += '<LineString><coordinates>';
        coordinates.forEach(function (coord) {
            kml += coord[0] + ',' + coord[1] + ' ';
        });
        kml += '</coordinates></LineString>';
    } else if (geojsonFeature.geometry.type === 'Polygon') {
        kml += '<Polygon><outerBoundaryIs><LinearRing><coordinates>';
        coordinates[0].forEach(function (coord) {
            kml += coord[0] + ',' + coord[1] + ' ';
        });
        kml += '</coordinates></LinearRing></outerBoundaryIs></Polygon>';
    }

    kml += '</Placemark>';
});

kml += '</Document></kml>';

var blob = new Blob([kml], { type: "application/vnd.google-earth.kml+xml" });
var url = URL.createObjectURL(blob);

var a = document.createElement("a");
a.href = url;
a.download = "exported_features.kml";
document.body.appendChild(a);
a.click();
document.body.removeChild(a);
}


function clearMap() {
drawnItems.clearLayers();
lineCoords = [];
polygonCoords = [];
circleCenter = null;
circleRadius = 0;
}

function clearAll() {
drawnItems.clearLayers();
lineCoords = [];
polygonCoords = [];
circleCenter = null;
circleRadius = 0;
map.setView([19.7515, 75.7139], 8); // Reset the map view to initial state
}