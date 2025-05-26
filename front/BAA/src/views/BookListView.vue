<template>
  <div>
    <h1>도서 목록</h1>
    <BookList/>
  </div>
</template>

<script setup>
  import BookList from '@/components/BookList.vue'
  import { useBooksStore } from '@/stores/books.js'
  import { onMounted } from 'vue'
  
  const bookStore = useBooksStore()

  onMounted(() => {
  bookStore.getBooks()
  })
</script>

<style scoped>

</style>