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
<!--       
      <label for="cover_img">이미지(나중에 자동 생성으로 구현 예정): </label>
      <input type="text" id="cover_img" v-model="coverImg">
      <br> -->
      
      <input v-if="!isUpdateMode" type="submit" value="Thread 생성">
      <input v-else type="submit" value="Thread 수정">
    </form>
    <button @click="goBack">뒤로가기</button>


  </div>
</template>

<script setup>
  import axios from 'axios'
  import { useRoute, useRouter } from 'vue-router'
  import { useAccountStore } from '@/stores/accounts'
  import { ref, onMounted, computed } from 'vue'
  import { useThreadsStore } from '@/stores/threads'

  const title = ref(null)
  const description = ref(null)
  const readDate = ref(null)
  // const coverImg = ref(null)

  const route = useRoute()
  const router = useRouter()
  const accountStore = useAccountStore()
  const threadsStore = useThreadsStore()
  const isUpdateMode = computed(() => threadsStore.selectedThread !== null)
  const bookIdParam = route.params.bookId
  const goBack = function() {
    router.push({name:'book', params:{'bookId':bookIdParam}})
  }
  const createThread = function () {

    const data = {
      title: title.value,
      description: description.value,
      read_date: readDate.value,
      // cover_img: coverImg.value,
    }

    const config = {
      headers: {
        'Authorization': `Token ${accountStore.token}`
      }
    }

    // 수정인지 생성인지 판단
    if (threadsStore.selectedThread) {
      // ✅ 수정 (PUT 요청)
      axios.put(
        `http://127.0.0.1:8000/api/v1/books/${bookIdParam}/threads/${threadsStore.selectedThread.id}/`,
        data,
        config
      )
        .then(res => {
          threadsStore.selectedThread = null  // 상태 초기화
          router.push({ name: 'book', params: { bookIdParam } }).then(() => {
          location.reload() 
        })
        })
        .catch(err => {
          console.error('수정 실패:', err.response?.data || err)
          alert('수정 중 오류가 발생했습니다.')
        })
    } else {
      // ✅ 생성 (POST 요청)
      axios.post(
        `http://127.0.0.1:8000/api/v1/books/${bookIdParam}/threads/`,
        data,
        config
      )
        .then(res => {
          router.push({ name: 'book', params: { bookId: bookIdParam } })
        })
        .catch(err => {
          console.error('생성 실패:', err.response?.data || err)
          alert('생성 중 오류가 발생했습니다.')
        })
    }
  }

  
  onMounted(() => {
    const thread = threadsStore.selectedThread
    if (thread) {
      title.value = thread.title
      description.value = thread.description
      readDate.value = thread.read_date
      coverImg.value = thread.cover_img
      
    }
  })
</script>

<style scoped>
  div {
    max-width: 600px;
    margin: 40px auto;
    padding: 32px;
    background-color: #fffdf8;
    border: 2px solid #f7d8c4;
    border-radius: 16px;
    box-shadow: 2px 2px 12px rgba(0, 0, 0, 0.05);
    font-family: 'Gowun Dodum', sans-serif;
    color: #5a4231;
  }

  form {
    display: flex;
    flex-direction: column;
    gap: 14px;
  }

  label {
    font-weight: bold;
    margin-bottom: 4px;
  }

  input[type="text"],
  input[type="date"],
  textarea {
    padding: 10px 12px;
    border: 1.5px solid #f3c8a2;
    border-radius: 10px;
    background-color: #fffaf5;
    font-size: 14px;
    color: #5a4231;
    resize: vertical;
    min-height: 38px;
  }

  textarea {
    min-height: 100px;
  }
  input[type="submit"],
  button {
    width: 100%; /* 버튼 너비 동일하게 */
    padding: 12px;
    border-radius: 10px;
    font-weight: bold;
    font-size: 14px;
    cursor: pointer;
    transition: background-color 0.2s ease, transform 0.1s ease;
    box-shadow: 1px 1px 6px rgba(0, 0, 0, 0.1);
    margin-top: 10px; /* 위 요소와 간격 확보 */
  }

  /* 생성 버튼 */
  input[type="submit"] {
    background-color: #ffad60;
    color: white;
    border: none;
  }

  input[type="submit"]:hover {
    background-color: #ff944d;
    transform: translateY(-2px);
  }

  /* 뒤로가기 버튼 (색상만 다르게) */
  button {
    background-color: #dcd3ca; /* 연회색/베이지톤 */
    color: #5a4231;
    border: none;
  }

  button:hover {
    background-color: #c8bfb5;
    transform: translateY(-2px);
  }



</style>