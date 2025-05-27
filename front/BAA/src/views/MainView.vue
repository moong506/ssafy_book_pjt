<template>
  <div>
    <div class="welcome-card">
      <h1 class="title">BAA에 오신 걸 환영합니다! 🎉</h1>
      <h2 class="message" v-if="isLogin">안녕하세요, <span class="username">{{ username }}</span> 님 😊</h2>
      <h2 class="message" v-else>로그인 후 이용해주세요! ✨</h2>
    </div>

    <div v-if="isLogin" class="recommend-card">
      <button class="recommend-button" @click.prevent="createBookRecommendation">AI 기반 도서 추천 받기 📚</button>
      <div v-if="recommendation" class="recommendations">
        <div v-for="(rec, index) in recommendation" :key="index" class="book-item">
          <p><strong>📖 책 제목:</strong> {{ rec.book }}</p>
          <p><strong>✍️ 작가:</strong> {{ rec.author }}</p>
          <p><strong>📌 설명:</strong> {{ rec.content }}</p>
        </div>
      </div>
    </div>

    <div class="baa-card">
      <h2>BAA (Book All Around)</h2>
      <p>독서가 생활이 되는 공간, BAA는 언제 어디서든 책을 가까이하는 문화를 지향합니다.</p>
    </div>
  </div>
</template>


<script setup>
import axios from 'axios'
import { useAccountStore } from '@/stores/accounts.js'
import { computed, ref } from 'vue'
const accountStore = useAccountStore()
const isLogin = computed(() => accountStore.isLogin)
const username = computed(() => accountStore.username)
const recommendation = ref(null)
const createBookRecommendation = function(){
  axios({
    method:'GET',
    url: 'http://127.0.0.1:8000/api/v1/',
    headers: {
        'Authorization': `Token ${accountStore.token}`
    }
  })
  .then((res) => {
    console.log(res.data)
    recommendation.value = res.data.recommendations
  })
  .catch(err => {
    console.error(err)
    alert('다시 한 번 눌러주세요!')
  })
}

</script>

<style scoped>
.welcome-card {
  max-width: 700px;
  margin: 80px auto;
  padding: 40px;
  background-color: #fffaf4;
  border: 2px solid #f7d8c4;
  border-radius: 24px;
  box-shadow: 3px 3px 10px rgba(0, 0, 0, 0.05);
  text-align: center;
  font-family: 'Gowun Dodum', 'Noto Sans KR', sans-serif;
  color: #5a4231;
}

.title {
  font-size: 32px;
  font-weight: bold;
  color: #ff914d;
  margin-bottom: 20px;
}

.message {
  font-size: 22px;
  margin-top: 10px;
  color: #6e4c2f;
}

.username {
  font-weight: bold;
  color: #e67300;
}
  .baa-card {
    margin: 2rem auto;
    max-width: 650px;
    background-color: #FFF1E6;
    border: 2px solid #FFD7B5;
    border-radius: 16px;
    padding: 20px 28px;
    text-align: center;
    box-shadow: 2px 2px 8px rgba(0,0,0,0.05);
  }
  .baa-card h2 {
    font-size: 24px;
    color: #CE7C5B;
    margin-bottom: 10px;
  }
  .baa-card p {
    font-size: 16px;
    color: #5C4033;
    line-height: 1.6;
  }
  .recommend-card {
    max-width: 720px;
    margin: 40px auto;
    padding: 28px;
    background-color: #fff9f0;
    border: 2px solid #f7d8c4;
    border-radius: 20px;
    box-shadow: 2px 2px 8px rgba(0,0,0,0.05);
    font-family: 'Gowun Dodum', 'Noto Sans KR', sans-serif;
    color: #5a4231;
  }

.recommend-button {
    background-color: #ffb284;
    border: none;
    padding: 10px 16px;
    font-size: 16px;
    border-radius: 12px;
    color: white;
    font-weight: bold;
    cursor: pointer;
    margin-bottom: 20px;
    transition: background-color 0.3s;
  }

  .recommend-button:hover {
    background-color: #ff944d;
  }

  .recommendations {
    margin-top: 16px;
  }

  .book-item {
    background-color: #fffdf9;
    border: 1px solid #f4d3b2;
    border-radius: 12px;
    padding: 16px;
    margin-bottom: 16px;
    box-shadow: 1px 1px 4px rgba(0,0,0,0.03);
  }

  .book-item p {
    margin: 6px 0;
    line-height: 1.5;
  }

</style>
