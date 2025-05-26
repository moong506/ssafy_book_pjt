<template>
  <div>
    <img :src="book.cover" alt="cover_img"  >
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
    <RouterLink class="detail-link" :to="{ name : 'book', params:{'bookId': book.id} }">상세 보기</RouterLink>
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
    max-width: 800px; /* 기존 600px → 800px로 넓힘 */
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
    text-align: center;
    line-height: 1.6;
    margin: 4px 0;
  }
  .detail-link {
    text-decoration: none;
    color: #CE7C5B;
    font-weight: bold;
    background-color: #FFF1E6;
    padding: 0.4rem 0.8rem;
    border-radius: 12px;
    transition: 0.2s;
    box-shadow: 1px 1px 4px rgba(0, 0, 0, 0.05);
  }

  .detail-link:hover {
    background-color: #FFBC8B;
    color: #fff;
  }



</style>