<template>
  <FarmNoteLabel />
  <div class="flex flex-col items-center flex-grow justify-center mt-10">
    <h2 class="text-2xl font-bold mb-4">
      EDIT NOTE
    </h2>

    <input v-model="noteData.content" placeholder="Insert Content" class="border p-3 rounded-lg mb-4 w-3/4 sm:w-1/2 md:w-1/3 lg:w-1/4" />
    <input v-model="noteData.field_id" placeholder="Insert Field-ID" class="border p-3 rounded-lg mb-4 w-3/4 sm:w-1/2 md:w-1/3 lg:w-1/4" />
    <input v-model="noteData.latitude" placeholder="Insert Latitude" class="border p-3 rounded-lg mb-4 w-3/4 sm:w-1/2 md:w-1/3 lg:w-1/4" />
    <input v-model="noteData.longitude" placeholder="Insert Longitude" class="border p-3 rounded-lg mb-4 w-3/4 sm:w-1/2 md:w-1/3 lg:w-1/4" />

    <button @click="updateNote" class="bg-blue-500 text-white px-6 py-3 rounded-lg shadow-lg m-4 text-xl">
      UPDATE
    </button>
    <button @click="deleteNote" class="bg-blue-500 text-white px-6 py-3 rounded-lg shadow-lg m-4 text-xl" :style="{ backgroundColor: '#ff0000', color: 'white' }">
      DELETE
    </button>
  </div>
</template>

<script>
import NoteService from "@/services/NoteService";
import FarmNoteLabel from "@/components/FarmNoteLabel.vue";
import Cookies from 'js-cookie';

export default {
  components: {
    FarmNoteLabel,
  },
  data() {
    return {
      noteData: {
        content: '',
        field_id: '',
        latitude: null,
        longitude: null,
      },
      errorMessage: '',
    };
  },
  async created() {
    await this.loadNote();
  },
  methods: {
    async loadNote() {
      const noteId = Cookies.get('noteID');
      try {
        const notes = await NoteService.getAllNotes();
        const note = notes.find(n => n.id === noteId);
        if (note) {
          this.noteData = {...note}; // Notizdaten in das Formular laden
        }
      } catch (error) {
        console.error("Fehler beim Laden der Notiz:", error);
      }
    },
    async updateNote() {
      const token = Cookies.get("session_token");
      const noteId = Cookies.get('noteID');
      try {
        await NoteService.updateNote(noteId, this.noteData, token);
        this.$router.push({name: 'note-list'}); // Nach dem Update zurück zur Notizenliste
      } catch (error) {
        this.errorMessage = "Fehler beim Aktualisieren der Notiz: " + error.message;
      }
    },


    async deleteNote() {
      const token = Cookies.get("session_token");
      const noteId = Cookies.get('noteID');
      try {
        await NoteService.deleteNote(noteId, token);
        this.$router.push({name: 'note-list'});
      } catch (error) {
        this.errorMessage = "Fehler beim Löschen der Notiz: " + error.message;
      }
    }

  },
};
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
