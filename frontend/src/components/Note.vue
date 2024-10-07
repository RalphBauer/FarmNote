<script setup>
  const props = defineProps(['note'])
</script>

<template>
  <div class="p-5 m-2 bg-white rounded-lg shadow-xl"><span class="bg-green-300 rounded-xl p-1 m-1">{{ props.note.id }}</span> {{ props.note.content }}</div>
</template>
