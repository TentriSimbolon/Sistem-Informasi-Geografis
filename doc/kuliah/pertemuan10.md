# OVERLAY
## Latar Belakang

1. Apa itu Open Layer
2. Apa itu Marker?
3. Cara menampilkan marker dengan menggunakan open layer?

## Isi
Open Layer adalah sebuah javascript murni yang digunakan untuk menampilkan data peta di web/browser, tanpsa server side dependencies. Open Layer mengimplementasikan javascript API untuk membangun rich web-based geographic application yang mirip dengan Google Maps dan MSN Virtual Earth APIS.
Marker adalah Suatu tanda sebuah wilayah atau tempat di permukaan bumi sehinggan kita bias mengetahui lokasi tersebut.

## Cara mebuat marker : 

- Buka web :http://openlayers.org/en/latest/examples/overlay.html?q=overlay

Copy code dan edit seperi berikut:
~~~
	<!DOCTYPE html>
	<html>
	  <head>
	    <title>Overlay</title>
	    <link rel="stylesheet" href="https://openlayers.org/en/v3.20.1/css/ol.css" type="text/css">
	    <!-- The line below is only needed for old environments like Internet Explorer and Android 4.x -->
	    <script src="https://cdn.polyfill.io/v2/polyfill.min.js?features=requestAnimationFrame,Element.prototype.classList,URL"></script>
	    <script src="https://openlayers.org/en/v3.20.1/build/ol.js"></script>
	    <script src="https://code.jquery.com/jquery-2.2.3.min.js"></script>
	    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css">
	    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/js/bootstrap.min.js"></script>
	    <style>
	      #marker {
	        width: 20px;
	        height: 20px;
	        border: 1px solid #088;
	        background-color: #FF3300;
	        opacity: 0.5;
	      }
	      #marker2 {
	        width: 20px;
	        height: 20px;
	        border: 1px solid #088;
	        border-radius: 10px;
	        background-color: #FF3300;
	        opacity: 0.5;
            }
            #marker3 {
	        width: 20px;
	        height: 20px;
	        border: 1px solid #088;
	        border-radius: 10px;
	        background-color: #FF3300;
	        opacity: 0.5;
	      }
	      #bandung {
	        text-decoration: none;
	        color: black;
	        font-size: 11pt;
	        font-weight: bold;
	        text-shadow: white 0.1em 0.1em 0.2em;
	      }
	      #jakarta {
	        text-decoration: none;
	        color: black;
	        font-size: 11pt;
	        font-weight: bold;
	        text-shadow: white 0.1em 0.1em 0.2em;
	      }
	      #samosir {
	        text-decoration: none;
	        color: black;
	        font-size: 11pt;
	        font-weight: bold;
	        text-shadow: white 0.1em 0.1em 0.2em;
	      }
	      .popover-content {
	        min-width: 180px;
	      }
	    </style>
	  </head>
	  <body>
	    <div id="map" class="map"></div>
	    <div style="display: none;">
	      <!-- Clickable label -->
	      <a class="overlay" id="bandung" target="_blank" href="http://id.wikipedia.org/wiki/Kota_Bandung">Bandung</a>
	      <div id="marker" title="Marker"></div>
	
	      <a class="overlay" id="jakarta" target="_blank" href="http://id.wikipedia.org/wiki/Daerah_Khusus_Ibukota_Jakarta">Jakarta</a>
	      <div id="marker2" title="Marker"></div>
	
	      <a class="overlay" id="samosir" target="_blank" href="http://id.wikipedia.org/wiki/Kabupaten_Samosir">Samosir</a>
	      <div id="marker3" title="Marker"></div>
	      <!-- Popup -->
	      <div id="popup" title="Welcome to ol3"></div>
	    </div>
	    <script>
	      var layer = new ol.layer.Tile({
	        source: new ol.source.OSM({
	              url: 'https://map.vas.web.id/wmts/agm/webmercator/{z}/{x}/{y}.png'
	            })
	      });
	
	      var map = new ol.Map({
	        layers: [layer],
	        target: 'map',
	        view: new ol.View({
	          center: ol.proj.transform([118.015776, -2.6000285], 'EPSG:4326', 'EPSG:3857'),
	          zoom: 5
	        })
	      });
	
	      var pos = ol.proj.fromLonLat([107.5731165, -6.9034443]);
	      var pos2 = ol.proj.fromLonLat([106.6894294, -6.229728]);
	      var pos3 = ol.proj.fromLonLat([98.4159691, 2.556193]);
	
	      // marker
	      var marker = new ol.Overlay({
	        position: pos,
	        positioning: 'center-center',
	        element: document.getElementById('marker'),
	        stopEvent: false
	      });
	      map.addOverlay(marker);
	
	      var marker2 = new ol.Overlay({
	        position: pos2,
	        positioning: 'center-center',
	        element: document.getElementById('marker2'),
	        stopEvent: false
	      });
          map.addOverlay(marker2);
	
	      var marker3 = new ol.Overlay({
	        position: pos3,
	        positioning: 'center-center',
	        element: document.getElementById('marker3'),
	        stopEvent: false
	      });
	      map.addOverlay(marker3);
	
	      // label
	      var bandung = new ol.Overlay({
	        position: pos,
	        element: document.getElementById('bandung')
	      });
	      map.addOverlay(bandung);
	
	      var jakarta = new ol.Overlay({
	        position: pos2,
	        element: document.getElementById('jakarta')
	      });
	      map.addOverlay(jakarta);
	
	      var samosir = new ol.Overlay({
	        position: pos3,
	        element: document.getElementById('samosir')
	      });
	      map.addOverlay(samosir);
	
	      // Popup showing the position the user clicked
	      var popup = new ol.Overlay({
	        element: document.getElementById('popup')
	      });
	      map.addOverlay(popup);
	
	      map.on('click', function(evt) {
	        var element = popup.getElement();
	        var coordinate = evt.coordinate;
	        var hdms = ol.coordinate.toStringHDMS(ol.proj.transform(
	            coordinate, 'EPSG:3857', 'EPSG:4326'));
	
	        $(element).popover('destroy');
	        popup.setPosition(coordinate);
	        // the keys are quoted to prevent renaming in ADVANCED mode.
	        $(element).popover({
	          'placement': 'top',
	          'animation': false,
	          'html': true,
	          'content': '<p>The location you clicked was:</p><code>' + hdms + '</code>'
	        });
	        $(element).popover('show');
	      });
	    </script>
	  </body>
	</html>
~~~	

Hasil :

## Kesimpulan
Jadi, Openlayers merupakan javascript murni yang digunakan untuk menempatkan peta yang dapat dibuka di web browser. Dan Marker adalah cara yang digunakan agar kita dapat menegtahui titiki tempat atau wilayah di permukaan bumi.

## Saran
Diharapkan memahami materi secara mendetail dan memahami praktikum dengan benar.
<br>

* Nama : Tentri May Simbolon
* NPM : 1144027
* Kelas : D4 Teknik Informatika 3C
* Kampus : Politeknik Pos Indonesia


Link Plagiarisme : https://drive.google.com/open?id=0B7tQon2iaQFdLUlpRkVPeWJyT00 
https://drive.google.com/open?id=0B7tQon2iaQFda2d3aFV5MlFwUHM 
