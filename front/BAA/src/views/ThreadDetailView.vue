<template>
  <div v-if="thread">
    <h1>{{ thread.title }}</h1>
    <p>{{ thread.description }}</p>
    <p>읽은 날짜 : {{ thread.read_date }}</p>
    <p>작성자 : {{ thread.user.username }}</p>
    <!-- 기타 쓰레드 상세 내용 -->
  </div>
  <div v-else>
    <p>로딩 중...</p>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRoute } from 'vue-router'
import axios from 'axios'
import { useAccountStore } from '@/stores/accounts'

const route = useRoute()
const accountStore = useAccountStore()
const thread = ref(null)

const threadId = route.params.threadId
const bookId = route.params.bookId


const fetchThreadDetail = function () {
  axios({
      method: 'get',
      url: `http://127.0.0.1:8000/api/v1/books/${bookId}/threads/${threadId}`,
      headers: {
        'Authorization' : `Token ${accountStore.token}`
      }
    })
    .then(res => {
      thread.value = res.data
    })
    .catch(err => {
      console.log(err)
    })
  }

onMounted(() => {
  fetchThreadDetail()
})
</script>

<style scoped>

</style>