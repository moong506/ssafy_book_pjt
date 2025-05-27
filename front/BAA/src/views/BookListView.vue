<template>
  <div>
    <h1 class="book_list_title">도서 목록</h1>
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
.book_list_title {
  text-align: center;
  font-size: 28px;
  margin-bottom: 24px;
  color: #ce7c5b; /* 기존 테마에 어울리는 색상 (선택사항) */
}
</style>