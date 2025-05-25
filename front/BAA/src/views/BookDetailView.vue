<template>
  <div>
    <h3>bookdetailview</h3>
    <BookDetail/>
    <button @click="goToThread(route.params.bookId)">Thread 작성하기</button>
  </div>
</template>

<script setup>
  import BookDetail from '@/components/BookDetail.vue'
  import { useRoute, useRouter } from 'vue-router'

  import { ref } from 'vue'

  const route = useRoute()
  const router = useRouter()
  // const bookStore = useBooksStore()
  const bookIdParam = route.params.bookId
  const goToThread = (pk) => {
    router.push({name: 'threadWrite', params: {'bookId':bookIdParam}})
  }

</script>

<style scoped>

</style>