<template>
  <div class="flex flex-col items-center flex-grow justify-center mt-10">
    <button @click="goToLoadSessionPage" class="bg-green-500 text-white px-6 py-3 rounded-lg shadow-lg m-4 text-xl">
      LOAD SESSION
    </button>
    <button @click="createSession" class="bg-blue-500 text-white px-6 py-3 rounded-lg shadow-lg m-4 text-xl">
      START SESSION
    </button>
  </div>
</template>


<script>
import SessionService from "@/services/SessionService.js";

export default {

  name: "StartPageButtons",

  methods: {

    async goToLoadSessionPage() {
      // changes to view LoadSessionPage.vue
      this.$router.push({ name: 'load-session-page' });
    },


    async createSession() {
      // creates a Session
      try {
        const response = await SessionService.createSession();
        this.$router.push({ name: 'main-page', params: { token: response.token } });
      } catch (error) {
        alert(`Error at StartPageButtons.vue at Function createSession: ${error.message}`);
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
  width: 80%;
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
