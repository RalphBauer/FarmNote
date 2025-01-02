<template>
  <main class="flex flex-col items-center justify-between h-screen bg-gray-100">
    <!-- FARM NOTE Label -->
    <FarmNoteLabel />

    <!-- Action Buttons -->
    <ActionButtons />
  </main>
</template>

<script>
import FarmNoteLabel from "@/components/FarmNoteLabel.vue";
import ActionButtons from "@/components/ActionButtons.vue";

export default {
  name: "StartPage",
  components: {
    FarmNoteLabel,
    ActionButtons
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
