import axios from "axios"
import { ref } from 'vue'
import { defineStore } from 'pinia'

export const useBooksStore = defineStore('article', () => {
  const books = ref([])

  const getBooks = function () {
    axios({
      method: 'get',
      url: 'http://127.0.0.1:8000/api/v1/books/'
    })
    .then(res => {
      books.value = res.data
    //   for (let i = 0; i < articles.value.length; i++){
    //     articles.value[i].id = i+1

    //   }
    })
  }

  return { books, getBooks }
})