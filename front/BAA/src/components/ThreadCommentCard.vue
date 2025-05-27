<template>
  <div v-if="threadComment.thread == threadId && threadComment.book == bookId" class="comment-card">
    <p class="comment-content">“{{ threadComment.content }}”</p>
    <div class="comment-meta">
      <span class="nickname">작성자: {{ threadComment.user.nickname }}</span>
      <span class="created-at">{{ formatDate(threadComment.created_at) }}</span>
    </div>
    <div v-if="threadComment.user.username === accountStore.username && accountStore.token" class="button-wrapper">
      <button class="delete-button" @click.prevent="onDeleteThreadComment">삭제</button>
    </div>
  </div>
</template>

<script setup>
  import axios from 'axios'
  import { useRoute, useRouter } from 'vue-router'
  import { useThreadCommentsStore } from '@/stores/threadcomments.js'
  import { useAccountStore } from '@/stores/accounts'
  import { format } from 'date-fns'
  const props = defineProps({
    threadComment: Object
  })
  const threadComment = props.threadComment

  const route = useRoute()
  const router = useRouter()
  const accountStore = useAccountStore()
  const threadCommentsStore = useThreadCommentsStore()

  const threadCommentId = threadComment.id
  const bookId = route.params.bookId
  const threadId = route.params.threadId

  const onDeleteThreadComment = function () {
    axios({
      method: 'DELETE',
      url: `http://127.0.0.1:8000/api/v1/books/${bookId}/threads/${threadId}/thread_comments/${threadCommentId}`,
      headers: {
        'Authorization': `Token ${accountStore.token}`
      }
    })
      .then(() => {
        threadCommentsStore.getThreadComments(bookId, threadId)
      })
      .catch(err => {
        console.error(err)
        router.push({ name: 'thread', params: { 'bookId': bookId, 'threadId':threadId  }}).then(() => {
          location.reload()
        })
      })
  }

  const formatDate = (datetime) => {
    return format(new Date(datetime), 'yyyy-MM-dd HH:mm')
  }
</script>

<style scoped>
  .comment-card {
    background-color: #fffaf4;
    border: 2px solid #f7d8c4;
    border-radius: 16px;
    padding: 16px;
    margin: 12px 0;
    box-shadow: 2px 2px 6px rgba(0, 0, 0, 0.05);
    font-family: 'Gowun Dodum', sans-serif;
    color: #5a4231;
  }

  .comment-content {
    font-size: 16px;
    margin-bottom: 10px;
    font-style: italic;
    color: #3f2e22;
  }

  .comment-meta {
    display: flex;
    justify-content: space-between;
    font-size: 14px;
    color: #6f4e37;
    margin-bottom: 8px;
  }
  .button-wrapper {
    text-align: right;
  }
  .delete-button {
    background-color: #ffb49a;
    border: none;
    color: white;
    font-weight: bold;
    padding: 6px 12px;
    border-radius: 10px;
    cursor: pointer;
    transition: 0.2s;
    box-shadow: 1px 1px 4px rgba(0, 0, 0, 0.05);
  }

  .delete-button:hover {
  
    background-color: #ff3333;
  }
</style>