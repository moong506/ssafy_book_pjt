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
  div {
    margin-top: 40px;
    padding: 20px;
    background-color: #fffdf8;
    border: 2px solid #f7d8c4;
    border-radius: 16px;
    box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.05);
    font-family: 'Gowun Dodum', sans-serif;
    color: #5a4231;
  }

  b {
    display: block;
    font-size: 20px;
    margin-bottom: 16px;
    color: #5a4231;
  }

  .thread-list {
    display: flex;
    flex-direction: column;
    gap: 16px;
  }

</style>