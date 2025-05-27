<template>
  <div v-if="bookComment.book == bookId" class="comment-card">
    <p class="comment-content">“{{ bookComment.content }}”</p>
    <div class="comment-meta">
      <span class="nickname">작성자: {{ bookComment.user.nickname }}</span>
      <span class="created-at">{{ formatDate(bookComment.created_at) }}</span>
    </div>

    <div v-if="bookComment.user.username === accountStore.username && accountStore.token" class="button-wrapper">
      <button class="delete-button" @click.prevent="onDeleteBookComment">삭제</button>
    </div>
  </div>
</template>

<script setup>
  import axios from 'axios'
  import { useRoute, useRouter } from 'vue-router'
  import { useBookCommentsStore } from '@/stores/bookcomments.js'
  import { useAccountStore } from '@/stores/accounts'
  import { format } from 'date-fns'

  const route = useRoute()
  const router = useRouter()
  const accountStore = useAccountStore()
  const bookCommentsStore = useBookCommentsStore()

  const props = defineProps({
    bookComment: Object
  })
  const bookComment = props.bookComment
  const bookCommentId = bookComment.id
  const bookId = route.params.bookId

  const onDeleteBookComment = function () {
    axios({
      method: 'DELETE',
      url: `http://127.0.0.1:8000/api/v1/books/${bookId}/book_comments/${bookCommentId}`,
      headers: {
        'Authorization': `Token ${accountStore.token}`
      }
    })
      .then(() => {
        bookCommentsStore.getBookComments(bookId)
      })
      .catch(err => {
        console.error(err)
        router.push({ name: 'book', params: { 'bookId': bookId, } }).then(() => {
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
