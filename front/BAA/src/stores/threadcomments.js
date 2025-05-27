import axios from "axios"
import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import { useRouter } from 'vue-router'
import { useAccountStore } from '@/stores/accounts'

export const useThreadCommentsStore = defineStore('threadomment', () => {
  const threadComments= ref([])
  const accountStore = useAccountStore()
  const selectedThreadComment = ref(null)
  const router = useRouter()
  const getThreadComments = function (bookId, threadId) {
    const headers = {}
    if (accountStore.token) {
      headers['Authorization'] = `Token ${accountStore.token}`
    }
    axios({
      method: 'get',
 
      url: `http://127.0.0.1:8000/api/v1/books/${bookId}/threads/${threadId}/thread_comments`,
      headers
    })
    .then(res => {
      threadComments.value = res.data
    })
    .catch(err => {
      // router.push({ name: 'book', params: { bookId } }).then(() => {
      //   location.reload() 
      // })
      console.log(err)

    })
}


  return { threadComments, selectedThreadComment, getThreadComments } 
}, { persist: true })