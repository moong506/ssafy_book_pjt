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
  div {
    width: 90%;               /* 화면의 90%를 기본 너비로 사용 */
    max-width: 1000px;        /* 최대 너비 제한 (너무 넓어지는 걸 방지) */
    margin: 40px auto;
    padding: 32px;
    background-color: #fffdf8;
    border: 2px solid #f7d8c4;
    border-radius: 16px;
    box-shadow: 3px 3px 12px rgba(0, 0, 0, 0.05);
    font-family: 'Gowun Dodum', sans-serif;
    color: #5a4231;
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 16px;
  }

  img {
    width: 220px;
    height: 300px;
    object-fit: cover;
    border-radius: 12px;
    box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.08);
  }

  h3 {
    font-size: 24px;
    font-weight: bold;
    margin: 12px 0 6px;
    text-align: center;
  }

  p {
    font-size: 16px;
    line-height: 1.6;
    margin: 4px 0;
    text-align: left;
    width: 100%;
  }


</style>