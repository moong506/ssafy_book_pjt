<template>
  <div v-if="book">
    
    <img :src="book.cover" alt="cover_img"  style="width: 200px; height: auto;" >
    <!-- <p>id : {{book.id}}</p> -->
    <h3>{{book.title}}</h3>
    <p>책 정보 : {{book.description}}</p>
    <!-- <p>isbn : {{book.isbn}}</p> -->

    
    <p>
      작가 : {{ book.author }} | 
      출판사 : {{book.publisher}}
    </p>
    <p> 작가 정보 : {{ book.author_info }}</p>
    <!-- <p>is_bestseller : {{ book.is_bestseller }}</p> -->

    <!-- 찜하기/찜취소 버튼 -->
    <button v-if="accountStore.token" @click="togglePick" style="margin-top: 16px;">
      {{ picked ? "찜 취소" : "찜하기" }}
    </button>

  </div>
</template>

<script setup>
  import axios from 'axios'
  import { useRoute } from 'vue-router'
  import { useBooksStore } from '@/stores/books'
  import { ref, onMounted } from 'vue'
  import { useAccountStore } from '@/stores/accounts'
  const accountStore = useAccountStore()
  const route = useRoute()
  const bookStore = useBooksStore()
  const bookIdParam = route.params.bookId
  const book = ref(null)
  const picked =ref(false) // 찜 상태
  // console.log(bookIdParam)
  // console.log(accountStore.token)
  const getBook = function () {
    const headers = {}
    if (accountStore.token) {
      headers['Authorization'] = `Token ${accountStore.token}`
    }

    axios({
      method: 'GET',
      url: `http://127.0.0.1:8000/api/v1/books/${bookIdParam}/`,
      headers
      // headers: {
      // 'Authorization': `Token ${localStorage.getItem('token')}`,
      // }
    })
    .then(res=>{
      book.value = res.data
      // back에서 is_picked 받으면
      console.log(res.data)
      picked.value = res.data.is_picked

      
    })
    .catch(err => console.log(err))
  }

  // 찜/찜취소 비동기 요청 함수
  const togglePick = function () {
    axios({
      method: 'POST',
      url: `http://127.0.0.1:8000/api/v1/books/${bookIdParam}/picks/`,
      headers: {
        'Authorization': `Token ${accountStore.token}`,
      }
    })
      .then(res => {
        console.log(res.data)
        picked.value = res.data.is_picked // True/False (백엔드에서 내려줌)
      })
      .catch(err => {
        console.log(err)
        if (err.response) {
          console.log('에러 상세:', err.response.status, err.response.data)
        }
      })
  }




  onMounted(() => {  
    getBook()
  })



</script>

<style scoped>
  div {
    width: 90%;               /* 화면의 90%를 기본 너비로 사용 */
    max-width: 1000px;        /* 최대 너비 제한 (너무 넓어지는 걸 방지) */
    margin: 40px auto;
    padding: 32px;
    background-color: #fffdf8;
    border: 2px solid #f7d8c4;
    border-radius: 16px;
    box-shadow: 3px 3px 12px rgba(0, 0, 0, 0.05);
    font-family: 'Gowun Dodum', sans-serif;
    color: #5a4231;
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 16px;
  }

  img {
    width: 220px;
    height: 300px;
    object-fit: cover;
    border-radius: 12px;
    box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.08);
  }

  h3 {
    font-size: 24px;
    font-weight: bold;
    margin: 12px 0 6px;
    text-align: center;
  }

  p {
    font-size: 16px;
    line-height: 1.6;
    margin: 4px 0;
    text-align: left;
    width: 100%;
  }
  
.button-wrapper {
  display: flex;
  justify-content: center; /* 오른쪽 정렬 */
  margin: 20px 0;
}
button {
  background-color: #ffad60;
  color: white;
  border: none;
  padding: 10px 18px;
  border-radius: 8px;
  font-size: 15px;
  font-weight: bold;
  cursor: pointer;
  box-shadow: 2px 2px 6px rgba(0, 0, 0, 0.1);
  transition: background-color 0.2s ease, transform 0.1s ease;
}
button:hover {
  background-color: #ff944d;
  transform: translateY(-2px);
}

</style>