<template>
  <div>
    <form v-on:submit.prevent="onLogIn">

      <br>
      <label for="username"> username : </label>
      <input type="text" id="username" v-model.trim="username">
      <br>
      <label for="password"> 비밀번호 : </label>
      <input type="password" id="password" v-model.trim="password">

      <input type="submit" value=" 로그인">
    </form>
  </div>
</template>

<script setup>
  import { ref } from 'vue'
  import { useAccountStore } from '@/stores/accounts.js'
  const accountStore = useAccountStore()
  const username = ref(null)
  const password = ref(null)
  

  // 뒤에 요청 생성하기
  const onLogIn = function () {
    const userInfo = {
      username : username.value,
      password : password.value,

    }
    accountStore.logIn(userInfo)

  }
</script>

<style scoped>

</style>