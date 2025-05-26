<template>
  <div>
    <br>
    <b>쓰레드 목록</b>
    <ThreadCard
    v-for="thread in threadsStore.threads"
    :key="thread.id"
    :thread= "thread"
    
    />
 
  </div>
  

</template>

<script setup>
  import { onMounted, computed, ref} from 'vue'
  import ThreadCard from './ThreadCard.vue'
  import { useRoute } from 'vue-router'
  const route = useRoute()
  const bookIdParam = route.params.bookId
  import { useThreadsStore } from '@/stores/threads'
  const threadsStore = useThreadsStore()
  
  

</script>

<style scoped>

</style>