<template>
  <div class="flex flex-col items-center flex-grow justify-center mt-10">
    <button @click="goToLoadSession" class="bg-green-500 text-white px-6 py-3 rounded-lg shadow-lg m-4 text-xl">
      LOAD SESSION
    </button>
    <button @click="startSession" class="bg-blue-500 text-white px-6 py-3 rounded-lg shadow-lg m-4 text-xl">
      START SESSION
    </button>
  </div>
</template>

<script>
import NoteService from "@/services/NoteService"; // Importiere den Service
import Cookies from 'js-cookie'; // Importiere die js-cookie Bibliothek

export default {
  methods: {
    goToLoadSession() {
      this.$router.push({ name: 'load-session' });
    },
    async startSession() {
      try {
        const response = await NoteService.createSession();

        // Navigiere zur MainPage und übergib den Token als Parameter
        this.$router.push({ name: 'main-page', params: { token: response.token } });
      } catch (error) {
        alert(`Fehler: ${error.message}`);
      }
    }
  }
}
</script>

<style scoped>
button {
  padding: 15px 30px;
  font-size: 20px;
  background-color: #28a745;
  color: white;
  border: none;
  border-radius: 10px;
  cursor: pointer;
  width: 250px;
  margin-top: 15px;
  text-align: center;
}

button:hover {
  background-color: #218838;
}

button:focus {
  outline: none;
}
</style>
