<template>
  <main class="flex flex-col items-center justify-between h-screen bg-gray-100">

    <FarmNoteLabel />

    <div class="form-container">

      <textarea
        v-model="content"
        placeholder="Inhalt der Notiz"
        class="input-field"
        rows="5"
      ></textarea>


      <input
        v-model="field_id"
        type="number"
        placeholder="Field ID"
        class="input-field"
      />


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

        // Check if the cookies are set to 'None'
        if (cookieLatitude === 'None' && cookieLongitude === 'None') {
          // If the cookies are none, use the current location
          const location = await this.getCurrentLocation();
          latitude = location.latitude;
          longitude = location.longitude;
        } else {
          // Use the coordinates from the cookies
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
        };

        const createdNote = await NoteService.createNote(noteData, token);

        console.log("Create Note:", createdNote);

        this.$router.push({name: 'main-page', params: {token: token}});

      } catch (error) {
        console.error("Fehler beim Erstellen der Notiz:", error.message);
      }
    },

  },

}

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
