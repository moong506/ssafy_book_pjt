<template>
  <div>
    <img :src="book.cover" alt="cover_img"  style="width: 200px; height: auto;" >
    <!-- <p>id : {{book.id}}</p> -->
    <p>{{book.title}}</p>
    <!-- <p>description : {{book.desciption}}</p> -->
    <!-- <p>isbn : {{book.isbn}}</p> -->

    <!-- <p>publisher : {{book.publisher}}</p> -->
    <!-- <p>pub_date : {{ book.pub_date }}</p> -->
    <p>작가 : {{ book.author }}</p>
    <!-- <p>author_info : {{ book.author_info }}</p> -->
    <!-- <img :src="book.author_photo" alt="cover_img"  style="width: 200px; height: auto;" > -->
    <!-- <p>customer_review_rank : {{ book.customer_review_rank }}</p> -->
    <!-- <p>is_bestseller : {{ book.is_bestseller }}</p> -->  
    <RouterLink :to="{ name : 'book', params:{'bookId': book.id} }">상세 보기</RouterLink>
    <br>
    <br>



  </div>
</template>

<script setup>
  import { RouterLink } from 'vue-router'
  defineProps({
    book: Object
  })
</script>

<style scoped>

</style>