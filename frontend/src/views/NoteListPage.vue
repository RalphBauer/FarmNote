<template>
  <FarmNoteLabel />
  <main class="flex flex-col items-center justify-between h-screen bg-gray-100">
    <main class="note-list-container">

      <h1 class="title">Notizen</h1>
      <div v-if="notes_data1.length === 0" class="no-notes">
        <p>Keine Notizen vorhanden.</p>
      </div>
      <ul v-else class="notes-list" :key="notes_data1.length">
        <li v-for="note in notes_data1" :key="note.id" class="note-item" @click="editNote(note.id)">
          <div class="note-content">
            <p><strong>Content:</strong> {{ note.content }}</p>
            <p><strong>Field-ID:</strong> {{ note.field_id }}</p>
            <p><strong>Position:</strong> {{ note.latitude }}, {{ note.longitude }}</p>
          </div>
        </li>
      </ul>
    </main>
  </main>
</template>

<script>
import NoteService from "@/services/NoteService";
import FarmNoteLabel from "@/components/FarmNoteLabel.vue";
import Cookies from "js-cookie";

export default {

  components: {
    FarmNoteLabel,
  },

  data() {
    return {
      notes_data1: [],
    };
  },

  async created() {
    await this.loadNotes();
  },

  methods: {

    async loadNotes() {
      try {
        let notes = await NoteService.getAllNotes();
        this.notes_data1 = notes;
      } catch (error) {
        console.error("Fehler beim Laden der Notizen:", error);
      }
    },



    editNote(noteId) {
      this.$router.push({name: 'edit-note'});
      Cookies.set('noteID', noteId);
    }

  },
};
</script>

<style scoped>
.note-list-container {
  text-align: center;
  padding: 20px;
  background-color: #f3f4f6; /* Hintergrundfarbe für den Container */
  flex-grow: 2; /* Damit der Container den verfügbaren Platz einnimmt */
}

.title {
  font-size: 2rem;
  margin-bottom: 20px;
}

.no-notes {
  font-size: 1.2rem;
  background-color: #f3f4f6; /* Hintergrundfarbe für die "Keine Notizen"-Nachricht */
  padding: 10px; /* Padding hinzufügen für bessere Lesbarkeit */
  border-radius: 5px; /* Abgerundete Ecken für die Nachricht */
}

.notes-list {
  list-style-type: none;
  padding: 0;
  margin: 0; /* Margin auf 0 setzen, um unerwünschte Abstände zu vermeiden */
}

.note-item {
  background-color: #f9f9f9;
  border: 1px solid #ccc;
  border-radius: 10px;
  padding: 15px;
  margin: 10px 0;
  cursor: pointer; /* Zeigt, dass das Element klickbar ist */
  transition: background-color 0.3s; /* Sanfter Übergang für den Hover-Effekt */
}

.note-item:hover {
  background-color: #f1f1f1; /* Hover-Effekt für bessere Benutzererfahrung */
}

.note-content {
  text-align: left;
}
</style>
