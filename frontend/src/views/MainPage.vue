<template>
  <div class="main-page">
    <!-- FARM NOTE Label -->
    <FarmNoteLabel />

    <!-- OpenStreetMap -->
    <div class="map-container">
      <MapComponent ref="mapComponent" />
    </div>

    <!-- Buttons -->
    <div class="buttons">
      <!-- Icon-Button links unten -->
      <button @click="onButtonLeftClick" class="button-left">
        <img src="../Invite.svg" alt="User Icon" />
      </button>

      <!-- Icon-Button für "Locate Me" -->
      <button @click="locateMe" class="button-locate">
        <img src="../Location_add.svg" alt="Locate Icon" />
      </button>

      <!-- Icon-Button rechts unten für das Erstellen einer Notiz -->
      <button @click="onButtonRightClick" class="button-right">
        <img src="../Notes.svg" alt="Map Icon" />
      </button>
    </div>
  </div>
</template>

<script>
import FarmNoteLabel from "@/components/FarmNoteLabel.vue";
import MapComponent from "@/components/MapComponent.vue";
import Cookies from "js-cookie";

export default {
  name: "MainPage",
  components: {
    FarmNoteLabel,
    MapComponent,
  },
  methods: {
    async locateMe() {
      if (!navigator.geolocation) {
        alert("Geolocation is not supported by your browser.");
        return;
      }

      navigator.geolocation.getCurrentPosition(
        (position) => {
          const { latitude, longitude } = position.coords;
          // Nachdem der Standort ermittelt wurde, navigiere zur CreateNote-Seite
          this.$router.push({
            name: "create-note", // Stelle sicher, dass diese Route im Router definiert ist
            query: { latitude, longitude }, // Übergebe die Koordinaten als Query-Parameter
          });
        },
        () => {
          alert("Unable to retrieve your location.");
        }
      );
    },
    onButtonLeftClick() {
      alert("Left Button Icon clicked!");
    },
    onButtonRightClick() {
      const token = Cookies.get("session_token");
      this.$router.push({ name: 'note-list', Query: { token: token } });
    },
  },
};
</script>

<style scoped>
.main-page {
  display: flex;
  flex-direction: column;
  height: 100vh;
}

.map-container {
  flex-grow: 1;
  height: calc(100vh - 100px);
  margin-top: 50px;
}

.buttons {
  position: absolute;
  bottom: 20px;
  width: 100%;
  display: flex;
  justify-content: space-between;
  padding: 0 20px;
}

/* Allgemeine Stile für die Icon-Buttons */
.button-left,
.button-right,
.button-locate {
  display: flex;
  justify-content: center;
  align-items: center;
  background-color: transparent; /* Kein Hintergrund, nur das Icon */
  border: none;
  border-radius: 50%; /* Runde Form */
  cursor: pointer;
  width: 60px;
  height: 60px;
  padding: 0;
}

.button-left img,
.button-right img,
.button-locate img {
  width: 100%; /* Bild füllt den Button */
  height: auto;
}

/* Hover-Effekt für die Buttons */
.button-left:hover,
.button-right:hover,
.button-locate:hover {
  background-color: rgba(0, 0, 0, 0.1); /* Leichter Hover-Effekt */
}

/* Fokus-Effekt für die Buttons */
.button-left:focus,
.button-right:focus,
.button-locate:focus {
  outline: none;
}

/* Positioniere den "Locate Me"-Button */
.button-locate {
  position: absolute;
  bottom: 90px; /* Oberhalb des rechten Buttons */
  right: 20px;
}

.farmnote-label {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  background-color: #28a745;
  color: white;
  text-align: center;
  font-size: 2.5rem;
  font-weight: bold;
  padding: 20px;
  z-index: 100000;
}
</style>
