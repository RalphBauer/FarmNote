<template>
  <div class="farmnote-label" @click="goToMainPage">
    FARM NOTE
  </div>
</template>

<script>
import Cookies from 'js-cookie';

export default {
  name: "FarmNoteLabel",
  methods: {
    goToMainPage() {
      this.$router.push({ name: 'main-page', params: { token: Cookies.get('session_token') } });
    }
  }
}
</script>

<style scoped>
.farmnote-label {
  font-size: 2.5rem;
  font-weight: bold;
  color: white;
  background-color: #28a745;
  padding: 20px;
  width: 100%;
  text-align: center;
  cursor: pointer; /* Fügt das Klicksymbol hinzu */
}
.farmnote-label:hover {
  background-color: #218838; /* Optional: Ändert die Hintergrundfarbe beim Hover */
}
</style>
