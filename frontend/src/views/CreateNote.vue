<template>
  <main class="flex flex-col items-center justify-between h-screen bg-gray-100">
    <!-- FARM NOTE Label -->
    <FarmNoteLabel />

    <!-- Eingabeformular -->
    <div class="form-container">
      <!-- Eingabefeld für den Inhalt -->
      <textarea
        v-model="content"
        placeholder="Inhalt der Notiz"
        class="input-field"
        rows="5"
      ></textarea>

      <!-- Eingabefeld für die field_id -->
      <input
        v-model="field_id"
        type="number"
        placeholder="Field ID"
        class="input-field"
      />

      <!-- Button zur Notizerstellung -->
      <button @click="submitNote" class="submit-button">Notiz speichern</button>
    </div>
  </main>
</template>

<script>
import NoteService from "@/services/NoteService";
import Cookies from 'js-cookie';
import FarmNoteLabel from "@/components/FarmNoteLabel.vue";

export default {
  components: {
    FarmNoteLabel,
  },
  data() {
    return {
      content: "",
      field_id: 1, // Beispielwert, setze dies entsprechend
    };
  },
  methods: {
    async getCurrentLocation() {
      return new Promise((resolve, reject) => {
        if (navigator.geolocation) {
          navigator.geolocation.getCurrentPosition(
              (position) => {
                resolve({
                  latitude: position.coords.latitude,
                  longitude: position.coords.longitude,
                });
              },
              (error) => {
                reject(error);
              }
          );
        } else {
          reject(new Error("Geolocation is not supported by this browser."));
        }
      });
    },
    async submitNote() {
  try {
    const cookieLatitude = Cookies.get('latitude');
    const cookieLongitude = Cookies.get('longitude');
    let latitude, longitude;

    // Überprüfen, ob die Cookies auf 'None' gesetzt sind
    if (cookieLatitude === 'None' || cookieLongitude === 'None') {
      // Wenn die Cookies None sind, verwende die aktuelle Position
      const location = await this.getCurrentLocation();
      latitude = location.latitude;
      longitude = location.longitude;
    } else {
      // Verwende die Koordinaten aus den Cookies
      latitude = parseFloat(cookieLatitude);
      longitude = parseFloat(cookieLongitude);
    }

    const token = Cookies.get("session_token"); // Token aus den Cookies abrufen

    if (!token) {
      throw new Error("Kein Token gefunden.");
    }

    let noteData = {
      content: this.content,
      latitude: latitude,
      longitude: longitude,
      field_id: this.field_id,
      // token: token, // Entferne den Token aus der Payload
    };

    // Erstelle die Notiz, indem du nur die noteData übergibst
    const createdNote = await NoteService.createNote(noteData, token); // Token als separates Argument übergeben
    console.log("Notiz erstellt:", createdNote);
    this.$router.push({ name: 'main-page', params: { token: token } });
  } catch (error) {
    console.error("Fehler beim Erstellen der Notiz:", error);
  }
},},}

</script>


<style scoped>
main {
  text-align: center;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  height: 100%;
}

.form-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  flex-grow: 1;
  width: 100%;
}

.input-field {
  width: 80%;
  max-width: 400px;
  padding: 15px;
  font-size: 16px;
  border: 2px solid #ccc;
  border-radius: 10px;
  margin: 10px 0;
  outline: none;
}

.input-field:focus {
  border-color: #28a745; /* Grüner Fokusrahmen */
}

.submit-button {
  width: 80%;
  max-width: 400px;
  padding: 15px;
  font-size: 18px;
  background-color: #28a745;
  color: white;
  border: none;
  border-radius: 10px;
  cursor: pointer;
  margin-top: 20px;
}

.submit-button:hover {
  background-color: #218838;
}

.submit-button:focus {
  outline: none;
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
