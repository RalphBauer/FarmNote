<template>
  <main class="note-list-container">
    <FarmNoteLabel />
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
</template>

<script>
import NoteService from "@/services/NoteService";
import FarmNoteLabel from "@/components/FarmNoteLabel.vue";

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
        let notes = await NoteService.getAllNotes(); // Notizen abrufen

        this.notes_data1 = notes; // Notizen in die Daten speichern
      } catch (error) {
        console.error("Fehler beim Laden der Notizen:", error);
      }
    },
    // Methode zum Bearbeiten einer Notiz
    editNote(noteId) {
      this.$router.push({ name: 'edit-note', params: { id: noteId } });
    }
  },
};
</script>

<style scoped>
.note-list-container {
  text-align: center;
  padding: 20px;
}

.title {
  font-size: 2rem;
  margin-bottom: 20px;
}

.no-notes {
  font-size: 1.2rem;
  color: #888;
}

.notes-list {
  list-style-type: none;
  padding: 0;
}

.note-item {
  background-color: #f9f9f9;
  border: 1px solid #ccc;
  border-radius: 10px;
  padding: 15px;
  margin: 10px 0;
  cursor: pointer; /* Zeigt, dass das Element klickbar ist */
}

.note-item:hover {
  background-color: #f1f1f1; /* Hover-Effekt für bessere Benutzererfahrung */
}

.note-content {
  text-align: left;
}
</style>
