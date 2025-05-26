import axios from "axios"
import { ref } from 'vue'
import { defineStore } from 'pinia'
import { useAccountStore } from '@/stores/accounts'

export const useThreadsStore = defineStore('thread', () => {
  const threads = ref([])
  const accountStore = useAccountStore()
  // const selectedThread = ref(null)
  const getThreads = function (bookId) {
    axios({
      method: 'get',
      url: `http://127.0.0.1:8000/api/v1/books/${bookId}/threads`,
      headers: {
        'Authorization' : `Token ${accountStore.token}`
      }
    })
    .then(res => {
      threads.value = res.data
    })
    .catch(err => {
      console.log(err)
    })
  }

  return { threads, getThreads } 
}, { persist: true })