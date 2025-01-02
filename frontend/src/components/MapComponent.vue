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
      userLocationLayer: null,
      notesLayer: null, // Layer für die Notizen
      clickCount: 0, // Zähler für Klicks
    };
  },
  async mounted() {
    // Initialisiere die OpenLayers-Karte
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

    // Erstelle einen Layer für den Benutzerstandort
    this.userLocationLayer = new VectorLayer({
      source: new VectorSource(),
    });

    // Erstelle einen Layer für die Notizen
    this.notesLayer = new VectorLayer({
      source: new VectorSource(),
    });

    // Füge die Layer zur Karte hinzu
    this.map.addLayer(this.notesLayer);
    this.map.addLayer(this.userLocationLayer);

    // Lade die Notizen und füge Marker hinzu
    await this.loadNotes();

    // Füge einen Event-Listener für Linksklicks hinzu
    this.map.on('singleclick', (event) => {
      const coordinates = this.map.getCoordinateFromPixel(event.pixel);
      const lonLat = toLonLat(coordinates);
      const latitude = lonLat[1];
      const longitude = lonLat[0];
      console.log('Koordinaten:', { latitude, longitude });

      // Erhöhe den Klickzähler
      this.clickCount++;

      // Setze die Cookies oder setze sie auf None
      if (this.clickCount % 2 === 0) {
        // Bei jedem zweiten Klick die Cookies auf None setzen
        Cookies.set('latitude', 'None');
        Cookies.set('longitude', 'None');
        console.log('Cookies gesetzt auf: None');
      } else {
        // Speichere die Koordinaten in Cookies
        Cookies.set('latitude', latitude, { expires: 7 });
        Cookies.set('longitude', longitude, { expires: 7 });
        console.log('Cookies gesetzt auf:', { latitude, longitude });
      }

      // Füge einen Marker an der Klickposition hinzu
      this.updateMarker();
    });

    // Überprüfe die Cookies und setze den Marker, falls vorhanden
    this.updateMarker();
  },
  methods: {
    async loadNotes() {
      try {
        const notes = await NoteService.getAllNotes(); // Notizen abrufen
        console.log('Abgerufene Notizen:', notes); // Überprüfen Sie die abgerufenen Notizen
        notes.forEach(note => {
          const { latitude, longitude } = note; // Angenommen, die Notiz hat latitude und longitude
          this.addNoteMarker(latitude, longitude); // Marker für Notizen hinzufügen
        });
      } catch (error) {
        console.error("Fehler beim Laden der Notizen:", error);
      }
    },
    updateMarker() {
      // Lösche alle bestehenden Marker für den temporären Marker
      this.userLocationLayer.getSource().clear();

      // Hole die Koordinaten aus den Cookies
      const latitude = Cookies.get('latitude');
      const longitude = Cookies.get('longitude');

      // Überprüfe, ob die Koordinaten vorhanden sind und nicht 'None' sind
      if (latitude !== 'None' && longitude !== 'None') {
        this.addMarker(parseFloat(latitude), parseFloat(longitude));
      }
    },
    addMarker(lat, lon) {
      const coords = fromLonLat([lon, lat]); // Beachten Sie die Reihenfolge

            // Erstelle einen neuen temporären Marker
      const tempMarker = new Feature({
        geometry: new Point(coords),
      });

      // Stil für den temporären Marker
      tempMarker.setStyle(
        new Style({
          image: new Icon({
            src: 'https://cdn-icons-png.flaticon.com/512/684/684908.png',
            scale: 0.1,
          }),
        })
      );

      // Füge den temporären Marker dem Benutzerstandort-Layer hinzu
      this.userLocationLayer.getSource().addFeature(tempMarker);
    },
    addNoteMarker(lat, lon) {
      console.log('Füge Notiz-Marker hinzu:', { lat, lon }); // Überprüfen Sie die Koordinaten
      const coords = fromLonLat([lon, lat]); // Beachten Sie die Reihenfolge

      // Erstelle einen neuen Marker für die Notiz
      const noteMarker = new Feature({
        geometry: new Point(coords),
      });

      // Stil für den Marker
      noteMarker.setStyle(
        new Style({
          image: new Icon({
            src: 'https://cdn-icons-png.flaticon.com/512/684/684908.png', // Beispiel für einen Notiz-Marker
            scale: 0.1,
          }),
        })
      );

      // Füge den Marker dem Notizen-Layer hinzu
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
