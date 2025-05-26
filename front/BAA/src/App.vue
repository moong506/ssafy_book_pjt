<template>
  <div>
    <nav>
      <RouterLink :to="{name: 'main'}">홈 </RouterLink> | 
      <RouterLink :to="{name: 'books'}">도서 목록</RouterLink> |
      
        <RouterLink v-if="!isLogin" :to="{name: 'signUp'}">회원 가입</RouterLink> 
        <RouterLink v-if="!isLogin" :to="{name: 'login'}">로그인</RouterLink>
        <RouterLink v-if="isLogin" :to="{name: 'profile', params:{'userId':1}}">마이 프로필</RouterLink>
        <button v-if="isLogin" @click="accountStore.logOut" >로그아웃</button>

        
    </nav>

  </div>
  <RouterView/>
</template>

<script setup>
  import { useAccountStore } from '@/stores/accounts.js'
  import { computed } from 'vue'
  const accountStore = useAccountStore()
  const isLogin = computed(() => accountStore.isLogin)
</script>

<style scoped>

</style>