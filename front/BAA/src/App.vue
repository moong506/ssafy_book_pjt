<template>
  <div class="app-container">
    <nav class="navbar">
      <RouterLink class="nav-link" :to="{name: 'main'}">홈</RouterLink> 
      <RouterLink class="nav-link" :to="{name: 'books'}">도서 목록</RouterLink> 

      <RouterLink v-if="!isLogin" class="nav-link" :to="{name: 'signUp'}">회원 가입</RouterLink> 
      <RouterLink v-if="!isLogin" class="nav-link" :to="{name: 'login'}">로그인</RouterLink>
      <RouterLink v-if="isLogin" class="nav-link" :to="{name: 'profile', params:{'userId':1}}">마이 프로필</RouterLink>
      <button v-if="isLogin" class="logout-button" @click="accountStore.logOut">로그아웃</button>
    </nav>
    <RouterView class="main-content"/>
  
    
    <footer class="footer">
      made by 김영훈 & 곽주혜 © {{ new Date().getFullYear() }}
    </footer>
  </div>

</template>


<script setup>
  import { useAccountStore } from '@/stores/accounts.js'
  import { computed } from 'vue'
  const accountStore = useAccountStore()
  const isLogin = computed(() => accountStore.isLogin)
</script>


<style scoped>
  .app-container {
    font-family: 'Noto Sans KR', sans-serif;
    background-color: #FFF6EC;
    color: #5C4033;
    min-height: 100vh;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
  }

  .navbar {
    background-color: #FFE5D1;
    padding: 1rem 1.5rem;
    display: flex;
    gap: 1rem;
    flex-wrap: wrap;
    border-bottom: 3px solid #FFD7B5;
    box-shadow: 0 4px 8px rgba(255, 209, 155, 0.3);
    border-radius: 0 0 16px 16px;
  }

  .nav-link {
    text-decoration: none;
    color: #CE7C5B;
    font-weight: bold;
    background-color: #FFF1E6;
    padding: 0.4rem 0.8rem;
    border-radius: 12px;
    transition: 0.2s;
    box-shadow: 1px 1px 4px rgba(0, 0, 0, 0.05);
  }
  .nav-link:hover {
    background-color: #FFBC8B;
    color: #fff;
  }

  .logout-button {
    background-color: #FF9E7C;
    border: none;
    color: #fff;
    padding: 0.4rem 0.8rem;
    border-radius: 12px;
    font-weight: bold;
    cursor: pointer;
    transition: 0.2s;
    box-shadow: 1px 1px 5px rgba(0, 0, 0, 0.1);
  }
  .logout-button:hover {
    background-color: #CE7C5B;
  }

  .main-content {
    padding: 2rem;
  }



  .footer {
    margin-top: auto;
    text-align: center;
    padding: 1rem;
    background-color: #FFE5D1;
    color: #5C4033;
    font-size: 14px;
    border-top: 2px solid #FFD7B5;
    border-radius: 16px 16px 0 0;
  }
</style>
