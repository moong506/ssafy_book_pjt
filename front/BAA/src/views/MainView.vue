<template>
  <div class="welcome-card">
    <h1 class="title">BAA에 오신 걸 환영합니다! 🎉</h1>
    <h2 class="message" v-if="isLogin">안녕하세요, <span class="username">{{ username }}</span> 님 😊</h2>
    <h2 class="message" v-else>로그인 후 이용해주세요! ✨</h2>
  </div>
    <div class="baa-card">
      <h2>BAA (Book All Around)</h2>
      <p>독서가 생활이 되는 공간, BAA는 언제 어디서든 책을 가까이하는 문화를 지향합니다.</p>
    </div>
</template>

<script setup>
import { useAccountStore } from '@/stores/accounts.js'
import { computed } from 'vue'
const accountStore = useAccountStore()
const isLogin = computed(() => accountStore.isLogin)
const username = computed(() => accountStore.username)
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
</style>
