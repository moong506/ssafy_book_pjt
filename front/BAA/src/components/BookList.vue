<template>
  <div class="book-list-container">


    <div class="top-bar">
      <div class="search-bar">
        <input type="text" v-model="searchText" placeholder="제목 또는 작가 검색" />
        <button>검색</button>
      </div>

      <div class="category-bar">

        <button
          v-for="category in categoryStore.categories"
          :key="category.pk"
          class="category-button"
          :class="{ active: selectedCategory === category.pk }"
          @click="selectedCategory = category.pk"
        >
          {{ category.fields.name }}
        </button>
      </div>
    </div>

    <div class="book-grid">
      <BookCard
        v-for="book in filteredBooks"
        :key="book.pk"
        :book="book"
      />
    </div>
  </div>
</template>


<script setup>
  
  import BookCard from './BookCard.vue'
  import { computed, ref } from 'vue'
  import { useBooksStore } from '@/stores/books'
  import { useCategoriesStore } from '@/stores/categories'

  const categoryStore = useCategoriesStore()
  const bookStore = useBooksStore()

  const searchText = ref('')

  const selectedCategory = ref(0)

  const filteredBooks = computed(() => {
    return bookStore.books.filter(book => {
      const matchCategory = !selectedCategory.value || book.category === selectedCategory.value
      const matchSearch =
        book.title.toLowerCase().includes(searchText.value.toLowerCase()) ||
        book.author.toLowerCase().includes(searchText.value.toLowerCase())
      return matchCategory && matchSearch
    })
  })


</script>

<style scoped>
 .book-list-container {
  max-width: 1200px;
  margin: 40px auto;
  padding: 24px;
  background-color: #fffaf4;
  border-radius: 16px;
  border: 2px solid #f7d8c4;
  box-shadow: 3px 3px 10px rgba(0, 0, 0, 0.03);
  font-family: 'Gowun Dodum', sans-serif;
  color: #5a4231;
}

/* 상단 바 정렬 */
  .top-bar {
    display: flex;
    flex-direction: column;
    gap: 16px;
    margin-bottom: 24px;
  }

  /* 검색창 */
  .search-bar {
    display: flex;
    justify-content: flex-end;
    gap: 8px;
  }

  .search-bar input {
    padding: 8px 12px;
    border: 1.5px solid #f3c8a2;
    border-radius: 10px;
    background-color: #fffdf8;
    font-size: 14px;
    color: #5a4231;
    width: 200px;
  }

  .search-bar button {
    background-color: #ffad60;
    border: none;
    color: white;
    font-weight: bold;
    padding: 8px 14px;
    border-radius: 10px;
    cursor: pointer;
    transition: background-color 0.2s ease;
  }

  .search-bar button:hover {
    background-color: #ff944d;
  }

  /* 카테고리 버튼 */
  .category-bar {
    display: flex;
    flex-wrap: wrap;
    gap: 8px;
    justify-content: center;
  }

  .category-button {
    padding: 6px 12px;
    border: 1.5px solid #f3c8a2;
    background-color: #fff1e6;
    color: #ce7c5b;
    border-radius: 8px;
    font-weight: bold;
    cursor: pointer;
    transition: 0.2s;
  }

  .category-button.active,
  .category-button:hover {
    background-color: #ffbc8b;
    color: #fff;
  }

  /* 도서 카드 그리드 */
  .book-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
    gap: 24px;
    justify-items: center;
  }



</style>