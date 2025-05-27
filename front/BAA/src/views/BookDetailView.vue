<template>
  <div>
 
    <BookDetail/>
    <div class="button-wrapper">
      <button @click="goToThread(route.params.bookId)">Thread 작성하기</button>
    </div>
    <ThreadList/>
    <BookCommentList/>
    
  </div>
</template>

<script setup>
  import BookDetail from '@/components/BookDetail.vue'
  import ThreadList from '@/components/ThreadList.vue'
  import BookCommentList from '@/components/BookCommentList.vue'
  import { useRoute, useRouter } from 'vue-router'
  import { ref, onMounted } from 'vue'
  import { useThreadsStore } from '@/stores/threads'
  import { useAccountStore } from '@/stores/accounts'


  const route = useRoute()
  const router = useRouter()
  const threadsStore = useThreadsStore()
  // const bookStore = useBooksStore()
  const bookIdParam = route.params.bookId
  const goToThread = (pk) => {
    router.push({name: 'threadWrite', params: {'bookId':bookIdParam}})
  }
  onMounted(() => {
  threadsStore.getThreads(bookIdParam)
  })
</script>
  
<style scoped>
  .button-wrapper {
    display: flex;
    justify-content: flex-end; /* 오른쪽 정렬 */
    margin: 16px 0;
  }

  button {
    background-color: #ffad60;
    color: white;
    border: none;
    padding: 10px 18px;
    border-radius: 8px;
    font-size: 15px;
    font-weight: bold;
    cursor: pointer;
    box-shadow: 2px 2px 6px rgba(0, 0, 0, 0.1);
    transition: background-color 0.2s ease, transform 0.1s ease;
  }

  button:hover {
    background-color: #ff944d;
    transform: translateY(-2px);
  }


</style>