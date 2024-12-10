<template>
  <div class="flex flex-col items-center flex-grow justify-center mt-10">
    <h2 class="text-2xl font-bold mb-4">LOAD SESSION</h2>
    <input v-model="sessionToken" placeholder="Insert Token" class="border p-3 rounded-lg mb-4 w-3/4 sm:w-1/2 md:w-1/3 lg:w-1/4" />
    <button @click="loadSession" class="bg-blue-500 text-white px-6 py-3 rounded-lg shadow-lg m-4 text-xl">
      LOAD SESSION
    </button>
  </div>
</template>

<script>
import NoteService from "@/services/NoteService";
import Cookies from 'js-cookie'; // Importiere die js-cookie Bibliothek

export default {
  name: "SessionLoaderForm",
  data() {
    return {
      sessionToken: '',
    };
  },
  methods: {
    async loadSession() {
      try {
        const response = await NoteService.loadSession(this.sessionToken);
        // Speichere den Token in den Cookies mit einer Ablaufzeit von 7 Tagen
        Cookies.set('session_token', response.token, {expires: 7});

        // Navigiere zur Hauptseite nach erfolgreichem Laden
        this.$router.push({name: 'main-page', params: {token: response.token}});
      } catch (error) {
        alert(error.message); // Zeige eine Fehlermeldung an
      }
    }
  }
}
</script>

<style scoped>
input {
  padding: 15px 30px;
  font-size: 16px;
  border: 1px solid #ccc;
  border-radius: 8px;
  width: 250px;
  margin-bottom: 15px;
}

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
