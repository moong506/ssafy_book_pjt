<template>
  <div>
    <p>id : {{book.id}}</p>
    <p>title : {{book.title}}</p>
    <p>description : {{book.desciption}}</p>
    <p>isbn : {{book.isbn}}</p>
    <!-- <img :src="book.cover" alt="cover_img"  style="width: 200px; height: auto;" > -->

    <p>publisher : {{book.publisher}}</p>
    <p>pub_date : {{ book.pub_date }}</p>
    <p>author : {{ book.author }}</p>
    <p>author_info : {{ book.author_info }}</p>
    <!-- <img :src="book.author_photo" alt="cover_img"  style="width: 200px; height: auto;" > -->
    <p>customer_review_rank : {{ book.customer_review_rank }}</p>
    <p>is_bestseller : {{ book.is_bestseller }}</p>
   





  </div>
</template>

<script setup>
defineProps({
    book: Object
  })
</script>

<style scoped>

</style>