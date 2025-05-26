<template>
  <div>
    <form @submit.prevent='createThread'>
      <label for="title">Thread 제목: </label>
      <input type="text" id="title" v-model="title">
      <br>
      <label for="description">내용: </label>
      <textarea id="description" v-model="description"></textarea>
      <br>
      
      <label for="read_date">읽은 날짜: </label>
      <input type="date" id="read_date" v-model="readDate">
      <br>
      
      <label for="cover_img">이미지(나중에 자동 생성으로 구현 예정): </label>
      <input type="text" id="cover_img" v-model="coverImg">
      <br>
      
      <input type="submit" value="Thread 생성">


    </form>


  </div>
</template>

<script setup>
  import axios from 'axios'
  // import { usethreadsStore } from '@/stores/threads.js'
  import { ref } from 'vue'
  import { useRoute, useRouter } from 'vue-router'
  import { useAccountStore } from '@/stores/accounts'

  const title = ref(null)
  const description = ref(null)
  const readDate = ref(null)
  const coverImg = ref(null)

  const route = useRoute()
  const router = useRouter()
  const accountStore = useAccountStore()
  // const store = useThreadsStore()

  const bookIdParam = route.params.bookId

  const createThread = function () {
    axios({
      method: 'post',
      url: `http://127.0.0.1:8000/api/v1/books/${bookIdParam}/threads/`,
      data: {

        title: title.value,
        description: description.value,
        read_date: readDate.value,
        cover_img: coverImg.value,
      },
      headers: {
        'Authorization' : `Token ${accountStore.token}`
      }
    })
      .then(res => {
        console.log(res)
        console.log(res.data)
        router.push({name: 'book', params: {'bookId':bookIdParam}})
      })
      .catch(err => {
        if (err.response) {
          console.error('서버 응답 에러:', err.response.data)
          alert(JSON.stringify(err.response.data))
        } else {
          console.error(err)
        }
      })
  }
</script>

<style scoped>

</style>