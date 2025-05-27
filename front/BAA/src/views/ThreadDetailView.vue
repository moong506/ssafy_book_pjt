<template>
  <div>

    <div class="thread-card" v-if="thread">
      <h2 class="thread-title">{{ thread.title }}</h2>
      <p class="thread-desc">{{ thread.description }}</p>
      <p class="thread-date">📅 읽은 날짜 : {{ thread.read_date }}</p>
      <p class="thread-user">👤 작성자 : {{ thread.user.username }}</p>
      
      <div class="button-group" v-if="thread.user.username === accountStore.username && accountStore.token">
        <button class="update-button" @click="onUpdateThread">수정</button>
        <button class="delete-button" @click="onDeleteThread">삭제</button>
      </div>
    </div>
    
    <div v-else class="loading">
      <p>로딩 중...</p>
    </div>
    <ThreadCommentList/>
  </div>
</template>


<script setup>
import ThreadCommentList from '@/components/ThreadCommentList.vue'
import axios from 'axios'
import { ref, onMounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { useAccountStore } from '@/stores/accounts'
import { useThreadsStore } from '@/stores/threads'
import { onBeforeRouteLeave } from 'vue-router'

const route = useRoute()
const router = useRouter()
const accountStore = useAccountStore()
const threadsStore = useThreadsStore()
const thread = ref(null)

const threadId = route.params.threadId
const bookId = route.params.bookId


const fetchThreadDetail = function () {
  const headers = {}
  if (accountStore.token) {
    headers['Authorization'] = `Token ${accountStore.token}`
  }

  axios({
    method: 'get',
    url: `http://127.0.0.1:8000/api/v1/books/${bookId}/threads/${threadId}`,
    headers
  })
  .then(res => {
    thread.value = res.data
  })
  .catch(err => {
    console.log(err)
  })
}


  const onUpdateThread = function(){
      threadsStore.selectedThread = thread.value
    
    router.push({name: 'threadWrite', params: {'bookId':bookId}})
  }
  
  

  
  const onDeleteThread = function(){
    axios({
      method: 'DELETE',
      url: `http://127.0.0.1:8000/api/v1/books/${bookId}/threads/${threadId}`,
      headers: {
        'Authorization' : `Token ${accountStore.token}`
      }
    })
    .then(res => {
      router.push({ name: 'book', params: { bookId } }).then(() => {
        location.reload() 
      })
    })

    .catch(err => {
      console.log(err)
    })
  }


onMounted(() => {
  fetchThreadDetail()
  
})
onBeforeRouteLeave(() => {
  threadsStore.selectedThread = null
})
</script>

<style scoped>
  .thread-card {
    width: 95%;
    max-width: 1000px;         /* 댓글 카드와 통일 */
    margin: 40px auto;
    padding: 40px;
    background-color: #fffdf8;
    border: 2px solid #f7d8c4;
    border-radius: 20px;
    box-shadow: 4px 4px 14px rgba(0, 0, 0, 0.06);
    font-family: 'Gowun Dodum', sans-serif;
    color: #5a4231;
    display: flex;
    flex-direction: column;
    gap: 20px;
  }


  .thread-title {
    font-size: 26px;
    font-weight: bold;
    text-align: center;
    color: #ce7c5b;
    margin-bottom: 10px;
  }

  .thread-desc {
    font-size: 18px;
    line-height: 1.6;
    padding: 10px;
    background-color: #fffaf4;
    border-radius: 10px;
    border: 1px dashed #f3c8a2;
  }

  .thread-date,
  .thread-user {
    font-size: 15px;
    color: #87614f;
  }

  .button-group {
    margin-top: 16px;
    display: flex;
    justify-content: center;
    gap: 16px;
  }

  button {
    padding: 10px 20px;
    font-size: 14px;
    font-weight: bold;
    border: none;
    border-radius: 16px;
    cursor: pointer;
    transition: background-color 0.2s ease, transform 0.1s ease;
    box-shadow: 1px 1px 6px rgba(0, 0, 0, 0.08);
  }

  button:hover {
    transform: translateY(-2px);
  }

  .update-button {
    background-color: #ffad60;
    color: #fff;
  }

  .update-button:hover {
    background-color: #ff944d;
  }

  .delete-button {
    background-color: #ff6b6b;
    color: #fff;
  }

  .delete-button:hover {
    background-color: #e74c3c;
  }

  .loading {
    text-align: center;
    font-size: 18px;
    color: #a18b7f;
    margin-top: 80px;
  }


</style>