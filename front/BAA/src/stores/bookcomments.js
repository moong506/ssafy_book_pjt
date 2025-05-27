import axios from "axios"
import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import { useRouter } from 'vue-router'
import { useAccountStore } from '@/stores/accounts'

export const useBookCommentsStore = defineStore('bookComment', () => {
  const bookComments= ref([])
  const accountStore = useAccountStore()
  const selectedBookComment = ref(null)
  const router = useRouter()
  const getBookComments = function (bookId) {
    const headers = {}
    if (accountStore.token) {
      headers['Authorization'] = `Token ${accountStore.token}`
    }
    axios({
      method: 'get',
      url: `http://127.0.0.1:8000/api/v1/books/${bookId}/book_comments`,
      headers
    })
    .then(res => {
      bookComments.value = res.data
    })
    .catch(err => {
      // router.push({ name: 'book', params: { bookId } }).then(() => {
      //   location.reload() 
      // })
      console.log(err)

    })
}


  return { bookComments, selectedBookComment, getBookComments} 
}, { persist: true })