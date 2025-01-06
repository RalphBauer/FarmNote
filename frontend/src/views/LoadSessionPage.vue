<template>
  <FarmNoteLabel />
  <SessionLoaderForm />
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

</style>
