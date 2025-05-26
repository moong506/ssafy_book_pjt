<template>
  <div class="book-list-container">
    <BookCard
    v-for="book in bookStore.books"
    :key="book.pk"
    :book = "book"
    
    />
  </div>
</template>

<script setup>
  
  // import { onMounted, computed, ref} from 'vue'
  import BookCard from './BookCard.vue'
  import { useBooksStore } from '@/stores/books'
//   const categoryStore = useCategoriesStore()
  const bookStore = useBooksStore()

//   const selectedCategory = ref(0)

//   const filteredBooks = computed(() => {
//   if (!selectedCategory.value) return bookStore.books
//   return bookStore.books.filter(
//     book => book.fields.category === selectedCategory.value
//   )
//   }
// )
</script>

<style scoped>
  div {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    gap: 20px;
    padding: 20px;
    background-color: #fff8f0; /* 따뜻하고 부드러운 배경 */
  }
  .book-list-container {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
  }

</style>