<script>
import Note from "@/components/Note.vue";
import NoteService from "@/services/NoteService.js";

export default {
  components: {Note},
  data() {
    return {
      notes: []
    }
  },
  mounted() {
    NoteService.getAllNotes('token1').then(notes => this.notes = [...notes]).catch(e => {
      alert(`backend is offline or GET endpoint /notes/ does not exist (${e.response.status})`)
    });
  }
}
</script>

<template>
  <div class="grid grid-cols-6">
    <Note v-for="note in notes" :key="note" :note="note"></Note>
  </div>
</template>