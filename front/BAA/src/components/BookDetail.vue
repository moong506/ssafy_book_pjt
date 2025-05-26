<template>
  <div v-if="book">
    
    <img :src="book.cover" alt="cover_img"  style="width: 200px; height: auto;" >
    <!-- <p>id : {{book.id}}</p> -->
    <h3>{{book.title}}</h3>
    <p>책 정보 : {{book.description}}</p>
    <!-- <p>isbn : {{book.isbn}}</p> -->

    
    <p>
      작가 : {{ book.author }} | 
      출판사 : {{book.publisher}}
    </p>
    <p> 작가 정보 : {{ book.author_info }}</p>
    <!-- <p>is_bestseller : {{ book.is_bestseller }}</p> -->
  
  </div>
</template>

<script setup>
  import axios from 'axios'
  import { useRoute } from 'vue-router'
  import { useBooksStore } from '@/stores/books'
  import { ref, onMounted } from 'vue'

  const route = useRoute()
  const bookStore = useBooksStore()
  const bookIdParam = route.params.bookId
  const book = ref(null)
  // console.log(bookIdParam)
  const getBook = function () {
    axios({
      method: 'GET',
      url: `http://127.0.0.1:8000/api/v1/books/${bookIdParam}/`
    })
    .then(res=>{
      book.value = res.data
    })
    .catch(err => console.log(err))
  }





  onMounted(() => {  
    getBook()
  })



</script>

<style scoped>

</style>