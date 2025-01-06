<template>
  <div id="map" class="map-container"></div>
</template>

<script>
import 'ol/ol.css';
import { Map, View } from 'ol';
import TileLayer from 'ol/layer/Tile';
import OSM from 'ol/source/OSM';
import { fromLonLat, toLonLat } from 'ol/proj';
import { Feature } from 'ol';
import { Point } from 'ol/geom';
import VectorLayer from 'ol/layer/Vector';
import VectorSource from 'ol/source/Vector';
import { Style, Icon } from 'ol/style';
import NoteService from '../services/NoteService.js';
import Cookies from 'js-cookie';

export default {

  name: 'MapComponent',

  data() {
    return {
      map: null,
      userLocationLayer: null, // Layer for the GNSS Location
      notesLayer: null, // Layer for the notes
      clickCount: 0, // Counter for Mouse clicks
    };
  },


  async mounted() {
    // Open Layers
    this.map = new Map({
      target: 'map',
      layers: [
        new TileLayer({
          source: new OSM(),
        }),
      ],
      view: new View({
        center: fromLonLat([16.3738, 48.2082]),
        zoom: 13,
      }),
    });


    this.userLocationLayer = new VectorLayer({
      source: new VectorSource(),
    });


    this.notesLayer = new VectorLayer({
      source: new VectorSource(),
    });


    this.map.addLayer(this.notesLayer);
    this.map.addLayer(this.userLocationLayer);


    await this.getAllNotes();


    this.map.on('singleclick', (event) => {
      // get the Coordinates after mouse click
      const coordinates = this.map.getCoordinateFromPixel(event.pixel);
      const lonLat = toLonLat(coordinates);
      const latitude = lonLat[1];
      const longitude = lonLat[0];
      console.log('Coordinates after mouse click:', { latitude, longitude });


      this.clickCount++;


      if (this.clickCount % 2 === 0) {
        // Set the cookies to None on every second mouse click
        Cookies.set('latitude', 'None');
        Cookies.set('longitude', 'None');
        console.log('Cookies set to: None');
      } else {
        // Store the coordinates in cookies
        Cookies.set('latitude', latitude, { expires: 7 });
        Cookies.set('longitude', longitude, { expires: 7 });
        console.log('Cookie latitude set to:', { latitude });
        console.log('Cookie longitude set to:', { longitude });
      }


      // Add a marker at the click position
      this.updateMarker();
    });


    // Check the cookies and set the marker if present
    this.updateMarker();
  },


  methods: {


    async getAllNotes() {
      // Loads all Notes into the map
      try {
        const notes = await NoteService.getAllNotes();
        console.log('Retrieved notes:', notes);

        notes.forEach(note => {
          const { latitude, longitude } = note;
          this.addNoteMarker(latitude, longitude);
        });

      } catch (error) {
        console.error("Error at loading notes:", error.message);
      }
    },


    updateMarker() {
      // Delete all existing markers for the temporary marker
      this.userLocationLayer.getSource().clear();

      // Retrieve the coordinates from the cookies
      const latitude = Cookies.get('latitude');
      const longitude = Cookies.get('longitude');

      // Check if the coordinates are present and not 'None'
      if (latitude !== 'None' && longitude !== 'None') {
        this.addMarker(parseFloat(latitude), parseFloat(longitude));
      }
    },


    addMarker(lat, lon) {
      const coords = fromLonLat([lon, lat]);

      // Create a new temporary marker
      const tempMarker = new Feature({
        geometry: new Point(coords),
      });

      tempMarker.setStyle(
        new Style({
          image: new Icon({
            src: 'https://cdn-icons-png.flaticon.com/512/684/684908.png',
            scale: 0.1,
          }),
        })
      );

      // Add the temporary marker to the user location layer
      this.userLocationLayer.getSource().addFeature(tempMarker);
    },


    addNoteMarker(lat, lon) {
      // Creates the markers for the notes
      console.log('Füge Notiz-Marker hinzu:', { lat, lon });
      const coords = fromLonLat([lon, lat]);

      // Create a new marker for the note
      const noteMarker = new Feature({
        geometry: new Point(coords),
      });

      noteMarker.setStyle(
        new Style({
          image: new Icon({
            src: 'https://cdn-icons-png.flaticon.com/512/684/684908.png', // Beispiel für einen Notiz-Marker
            scale: 0.1,
          }),
        })
      );

      // Add the marker to the notes layer
      this.notesLayer.getSource().addFeature(noteMarker);
    }


  },
};
</script>

<style scoped>
.map-container {
  height: 100%;
  width: 100%;
}
</style>
