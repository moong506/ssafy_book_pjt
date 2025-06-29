import { ref, computed } from 'vue'
import { defineStore } from 'pinia'

export const useCategoriesStore = defineStore('categories', () => {
  const categories = [
    
    {
        "model": "books.category",
        "pk": 0,
        "fields": {
            "name": "전체"
        }
    },
    {
        "model": "books.category",
        "pk": 1,
        "fields": {
            "name": "소설/시/희곡"
        }
    },
    {
        "model": "books.category",
        "pk": 2,
        "fields": {
            "name": "경제/경영"
        }
    },
    {
        "model": "books.category",
        "pk": 3,
        "fields": {
            "name": "자기계발"
        }
    },
    {
        "model": "books.category",
        "pk": 4,
        "fields": {
            "name": "인문/교양"
        }
    },
    {
        "model": "books.category",
        "pk": 5,
        "fields": {
            "name": "취미/실용"
        }
    },
    {
        "model": "books.category",
        "pk": 6,
        "fields": {
            "name": "어린이/청소년"
        }
    },
    {
        "model": "books.category",
        "pk": 7,
        "fields": {
            "name": "과학"
        }
    }

  ]
    
  return { categories }
})
