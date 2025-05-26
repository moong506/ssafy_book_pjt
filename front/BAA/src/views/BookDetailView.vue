<template>
  <div>
    <h3>bookdetailview</h3>
    <BookDetail/>
    <button @click="goToThread(route.params.bookId)">Thread 작성하기</button>
    <ThreadList/>
  
  </div>
</template>

<script setup>
  import BookDetail from '@/components/BookDetail.vue'
  import ThreadList from '@/components/ThreadList.vue'
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

</style>