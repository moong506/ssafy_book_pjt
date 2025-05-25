<template>
  <div></div>
  
  <!-- 이거 아직 만들지도 않음 -->
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

</style>