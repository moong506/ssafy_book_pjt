<template>
  <div>
    <img :src="book.cover" alt="cover_img"  style="width: 200px; height: auto;" >
    <!-- <p>id : {{book.id}}</p> -->
    <h3>{{book.title}}</h3>
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
  div {
    width: 220px;
    min-height: 430px;
    background-color: #fffdf8;
    border: 2px solid #f7d8c4;
    border-radius: 16px;
    box-shadow: 2px 2px 6px rgba(0, 0, 0, 0.1);
    padding: 16px;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: space-between;
    transition: transform 0.2s ease;
    overflow: hidden;
  }

  div:hover {
    transform: translateY(-4px);
  }

  img {
    width: 160px;
    height: 200px;
    object-fit: cover;
    border-radius: 8px;
    margin-bottom: 10px;
  }

  p {
    margin: 4px 0;
    text-align: center;
    font-size: 15px;
    color: #5a4231;
  }

  a {
    color: #ff7f50;
    font-weight: bold;
    text-decoration: none;
    font-size: 14px;
  }

  a:hover {
    text-decoration: underline;
  }

</style>