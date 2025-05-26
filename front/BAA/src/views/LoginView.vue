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
  div {
    max-width: 400px;
    margin: 60px auto;
    padding: 32px;
    background-color: #fffdf8;
    border: 2px solid #f7d8c4;
    border-radius: 16px;
    box-shadow: 2px 2px 12px rgba(0, 0, 0, 0.05);
    font-family: 'Gowun Dodum', sans-serif;
    color: #5a4231;
  }

  form {
    display: flex;
    flex-direction: column;
    gap: 14px;
  }

  label {
    font-weight: bold;
    margin-bottom: 4px;
  }

  input[type="text"],
  input[type="password"] {
    padding: 10px 12px;
    border: 1.5px solid #f3c8a2;
    border-radius: 10px;
    font-size: 15px;
    background-color: #fffaf5;
    color: #5a4231;
  }

  input[type="submit"] {
    background-color: #ffad60;
    color: white;
    font-weight: bold;
    border: none;
    border-radius: 10px;
    padding: 10px;
    cursor: pointer;
    margin-top: 12px;
    box-shadow: 1px 1px 6px rgba(0, 0, 0, 0.1);
    transition: background-color 0.2s ease, transform 0.1s ease;
  }

  input[type="submit"]:hover {
    background-color: #ff944d;
    transform: translateY(-2px);
  }

</style>