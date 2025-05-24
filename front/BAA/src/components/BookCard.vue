<template>
  <div>
    <p>id : {{book.id}}</p>
    <p>title : {{book.id}}</p>
    <p>description : {{book.desciption}}</p>
    <p>isbn : {{book.isbn}}</p>
    <img :src="book.cover_img" alt="cover_img"  style="width: 200px; height: auto;" >

    <p>publisher : {{book.publisher}}</p>
    <p>pub_date : {{ book.pub_date }}</p>
    <p>author : {{ book.author }}</p>
    <p>author_info : {{ book.author_info }}</p>
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