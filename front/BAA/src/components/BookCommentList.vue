<template>
  <b>댓글</b>
  <div @submit.prevent="createBookComment">
    <form>
      <textarea v-model="newBookComment"></textarea>
      <input type="submit" value="작성">
    </form>
  </div>
</template>

<script setup>
  import axios from 'axios'
  import { useRoute } from 'vue-router'
  import { useAccountStore } from '@/stores/accounts'
  import { ref, onMounted, computed } from 'vue'
  // import { useThreadsStore } from '@/stores/threads'
  const accountStore = useAccountStore()
  const route = useRoute()
  const newBookComment = ref(null)
  const bookId = route.params.bookId

  const createBookComment = function(){
    axios({
      method: 'POST',
      url: `http://127.0.0.1:8000/api/v1/books/${bookId}/book_comments/`,
      data: {
        content: newBookComment.value
      },
      headers: {
        'Authorization' : `Token ${accountStore.token}`
      }
    })
    .then(res => {
      newBookComment.vaule = null
    })
    .catch(err => {
      console.error('댓글 생성 실패:', err.response?.data || err)
      alert('댓글 생성 중 오류가 발생했습니다.')
    })
  }



</script>

<style scoped>

</style>