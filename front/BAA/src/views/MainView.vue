<template>
  <div>
    <h1>BBA에 오신걸 환영합니다!</h1>
    <h1 v-if="isLogin" >안녕하세요 {{ username }}님</h1>
    <h1 v-else> 로그인 후 이용하세요</h1>
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

</style>