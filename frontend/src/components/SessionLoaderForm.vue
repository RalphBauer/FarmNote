<template>
  <div class="flex flex-col items-center flex-grow justify-center mt-10">
    <h2 class="text-2xl font-bold mb-4">
      LOAD SESSION
    </h2>

    <input v-model="sessionToken" placeholder="Insert Token" class="border p-3 rounded-lg mb-4 w-3/4 sm:w-1/2 md:w-1/3 lg:w-1/4" />

    <button @click="loadSession" class="bg-blue-500 text-white px-6 py-3 rounded-lg shadow-lg m-4 text-xl">
      CONFIRM
    </button>
  </div>
</template>


<script>
import SessionService from "@/services/SessionService";
import Cookies from 'js-cookie';

export default {

  name: "LoadSessionPageForm",


  data() {
    return {
      sessionToken: '',
    };
  },


  methods: {


    async loadSession() {
      // Loads the Session with the Token which the User put in
      try {
        const response = await SessionService.loadSession(this.sessionToken);
        Cookies.set('session_token', response.token, {expires: 7});
        this.$router.push({name: 'main-page', params: {token: response.token}});
      } catch (error) {
        alert(`Error at SessionLoaderForm.vue at Function loadSession: ${error.message}`);
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
  width: 80%;
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
