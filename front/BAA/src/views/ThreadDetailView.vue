<template>
  <div v-if="thread">
    <h1>{{ thread.title }}</h1>
    <p>{{ thread.description }}</p>
    <p>읽은 날짜 : {{ thread.read_date }}</p>
    <p>작성자 : {{ thread.user.username }}</p>
    
    <div v-if="thread.user.username === accountStore.username && accountStore.token">
      
      <button class="update-button" @click="onUpdateThread">수정</button>
      <button class="delete-button" @click="onDeleteThread">삭제</button>

    </div>

  </div>
  <div v-else>
    <p>로딩 중...</p>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import axios from 'axios'
import { useAccountStore } from '@/stores/accounts'
import { useThreadsStore } from '@/stores/threads'

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

</script>

<style scoped>
  
  button {
  padding: 8px 16px;
  font-size: 14px;
  font-weight: bold;
  border: none;
  border-radius: 16px;
  margin-right: 10px;
  cursor: pointer;
  transition: background-color 0.2s ease, transform 0.1s ease;
  box-shadow: 1px 1px 6px rgba(0, 0, 0, 0.08);
}

button:hover {
  transform: translateY(-2px);
}

/* 수정 버튼 */
.update-button {
  background-color: #ffad60;
  color: #fff;
}

.update-button:hover {
  background-color: #ff944d;
}

/* 삭제 버튼 */
.delete-button {
  background-color: #ff6b6b;
  color: #fff;
}

.delete-button:hover {
  background-color: #e74c3c;
}


</style>