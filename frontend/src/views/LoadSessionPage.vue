<template>
  <main class="flex flex-col items-center justify-between h-screen bg-gray-100">
    <!-- FARM NOTE Label -->
    <FarmNoteLabel />

    <!-- SessionLoaderForm -->
    <SessionLoaderForm />
  </main>
</template>

<script>
import FarmNoteLabel from "@/components/FarmNoteLabel.vue";
import SessionLoaderForm from "@/components/SessionLoaderForm.vue";

export default {
  name: "LoadSessionPage",
  components: {
    FarmNoteLabel,
    SessionLoaderForm
  }
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
</style>
