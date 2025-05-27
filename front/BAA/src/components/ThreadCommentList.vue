<template>
 <div class="card-container">
    <div class= "comment-card">

      <b>댓글</b>
      <div @submit.prevent="createThreadComment" v-if="accountStore.token">
        <form >
          <textarea v-model="newThreadComment"></textarea>
          <input type="submit" value="작성">
        </form>
      </div>
      <ThreadCommentCard
      v-for="threadComment in threadCommentsStore.threadComments"
      :key="threadComment.id"
      :threadComment= "threadComment"
      class="thread-comment-card"
      />
    </div>
  </div>
</template>

<script setup>
  import axios from 'axios'
  import { useRoute } from 'vue-router'
  import { useAccountStore } from '@/stores/accounts'
  import { ref, onMounted, computed } from 'vue'
  import { useThreadCommentsStore } from '@/stores/threadcomments.js'
  import ThreadCommentCard from './ThreadCommentCard.vue'
  const accountStore = useAccountStore()
  const route = useRoute()
  const newThreadComment = ref(null)
  const bookId = route.params.bookId
  const threadId = route.params.threadId
  const threadCommentsStore = useThreadCommentsStore()

  const createThreadComment = function(){
    axios({
      method: 'POST',
      url: `http://127.0.0.1:8000/api/v1/books/${bookId}/threads/${threadId}/thread_comments/`,
      data: {
        content: newThreadComment.value
      },
      headers: {
        'Authorization' : `Token ${accountStore.token}`
      }
    })
    .then(res => {
      
      newThreadComment.value = null
      threadCommentsStore.getThreadComments(bookId, threadId)
    })
    .catch(err => {
      console.error('댓글 생성 실패:', err.response?.data || err)
      alert('댓글 생성 중 오류가 발생했습니다.')
    })
  }
  onMounted(() => {
   threadCommentsStore.getThreadComments(bookId, threadId)
  })


</script>

<style scoped>
  .card-container {
    width: 90%;
    max-width: 1000px;
    margin: 20px auto;
  }
  .comment-card {
    background-color: #fffaf0; /* 부드러운 배경 */
    border: 2px solid #FAD390; /* 반죽 노랑 */
    border-radius: 16px;
    padding: 20px;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
    margin: 30px 0;
  }

  b {
    display: block;
    font-size: 20px;
    color: #8B5E3C; /* 소스색 */
    margin-bottom: 10px;
  }

  form {
    display: flex;
    flex-direction: column;
    gap: 8px;
    background-color: #FAF1E4; /* 마요네즈 */
    padding: 16px;
    border-radius: 12px;
    border: 2px solid #FAD390; /* 반죽 노랑 */
    margin-bottom: 20px;
  }

  textarea {
    resize: vertical;
    min-height: 80px;
    padding: 10px;
    font-size: 15px;
    font-family: 'Gowun Dodum', sans-serif;
    border: 2px solid #FAD390;
    border-radius: 8px;
    background-color: #fffaf5;
    color: #5a4231;
  }

  input[type="submit"] {
    align-self: flex-end;
    padding: 8px 16px;
    background-color: #8B5E3C; /* 소스색 */
    color: white;
    font-weight: bold;
    font-size: 14px;
    border: none;
    border-radius: 8px;
    cursor: pointer;
    transition: background-color 0.2s ease, transform 0.1s ease;
  }

  input[type="submit"]:hover {
    background-color: #6f462b; /* 소스 진한 색 */
    transform: translateY(-2px);
  }

  /* 댓글 카드 사이 여백 */
  .thread-comment-card + .thread-comment-card {
    margin-top: 12px;
  }
</style>