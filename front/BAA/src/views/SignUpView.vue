<template>
  <div>
    <form v-on:submit.prevent="onSignUp">
      <br>
      <b>*는 필수 항목입니다.</b>
      <br>
      <label for="username"> * username : </label>
      <input type="text" id="username" v-model.trim="username">

      <br>


      <label for="password1"> * 비밀번호 : </label>
      <input type="password" id="password1" v-model.trim="password1">

      <br>
      <label for="password2"> * 비밀번호 확인 : </label>
      <input type="password" id="password2" v-model.trim="password2">
      <br>
      <br>

      <b>개인 프로필 생성을 위한 정보</b> <br>
      <label for="nickname"> * 닉네임 : </label>
      <input type="text" id="nickname" v-model.trim="nickname">

      <br>
      <label for="email"> * 이메일 : </label>
      <input type="email" id="email" v-model.trim="email">
      
      
      <br>
      <label for="gender"> * 성별 : </label>
      <select id="gender" v-model.trim="genderchoices">
        <option value="M">남성</option>
        <option value="F">여성</option>
      </select>
      <br>
      <label for="age"> * 나이 : </label>
      <input type="number" id="age" v-model.trim="age">
      
      <br>
      <label for="last_name"> 성 : </label>
      <input type="text" id="last_name" v-model.trim="last_name">

      <br>
      <label for="first_name"> 이름 : </label>
      <input type="text" id="first_name" v-model.trim="first_name">
      
      
      <br>
      <label for="weekly_avg_reading_time"> 주간 평균 독서 시간 : </label>
      <input type="number" id="weekly_avg_reading_time" v-model.trim="weekly_avg_reading_time">
      
      <br>
      <label for="annual_reading_amount"> 연간 독서량 : </label>
      <input type="number" id="annual_reading_amount" v-model.trim="annual_reading_amount">
      
      <br>
      <!-- <label for="profile_img"> 프로필 사진 : </label>
      <input type="file" id="profile_img" v-on.change="uploadImg">
      <br> -->
      <input type="submit" value="회원가입">
    </form>
  </div>
</template>

<script setup>
  import { ref } from 'vue'
  import { useAccountStore } from '@/stores/accounts.js'
  const accountStore = useAccountStore()
  const username = ref(null)
  const password1 = ref(null)
  const password2 = ref(null)
  const nickname = ref(null)
  const last_name = ref(null)
  const first_name = ref(null)
  const email = ref(null)
  const genderchoices = ref(null)
  const age = ref(null)
  const weekly_avg_reading_time = ref(null)
  const annual_reading_amount = ref(null)
  // const profile_img = ref(null)

  // const uploadImg = (event) =>{
  //   console.log(event.target)
  //   const file = event.target.files[0]
  //   profile_img.value = file
  // }

  // 뒤에 요청 생성하기
  const onSignUp = function () {
    const userInfo = {

      username : username.value,
      password1 : password1.value,
      password2 : password2.value,
      nickname : nickname.value, 
      last_name : last_name.value, 
      first_name : first_name.value,
      email : email.value,
      gender : genderchoices.value,
      age : age.value,
      weekly_avg_reading_time : weekly_avg_reading_time.value,
      annual_reading_amount : annual_reading_amount.value,
      // profile_img : profile_img.value 
    }
    Object.keys(userInfo).forEach(key => {
      if (
        userInfo[key] === null ||
        userInfo[key] === undefined ||
        userInfo[key] === ''
      ) {
        delete userInfo[key];
      }
    });



    accountStore.signUp(userInfo)

  }
</script>

<style scoped>

  div {
    width: 90%;
    max-width: 800px; /* 더 넓게 설정 */
    margin: 40px auto;
    padding: 32px;
    background-color: #fffdf8;
    border: 2px solid #f7d8c4;
    border-radius: 16px;
    box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.05);
    font-family: 'Gowun Dodum', sans-serif;
    color: #5a4231;
    box-sizing: border-box;
  }

  form {
    display: flex;
    flex-direction: column;
    gap: 12px;
  }

  label {
    font-weight: bold;
    margin-top: 8px;
  }

  input,
  select {
    padding: 10px 14px;
    border: 1.5px solid #f3c8a2;
    border-radius: 8px;
    font-size: 16px;
    background-color: #fffaf5;
    color: #5a4231;
    width: 100%;
    box-sizing: border-box;
  }

  input[type="submit"] {
    background-color: #ffad60;
    color: white;
    font-weight: bold;
    border: none;
    cursor: pointer;
    transition: background-color 0.2s ease, transform 0.1s ease;
    padding: 12px;
    margin-top: 20px;
    box-shadow: 1px 1px 6px rgba(0, 0, 0, 0.08);
  }

  input[type="submit"]:hover {
    background-color: #ff944d;
    transform: translateY(-2px);
  }

  b {
    font-size: 18px;
    color: #ce7c5b;
    margin-bottom: 4px;
    display: block;
  }

  @media (max-width: 768px) {
    div {
      padding: 20px;
    }

    input,
    select {
      font-size: 14px;
      padding: 8px 10px;
    }

    input[type="submit"] {
      font-size: 15px;
      padding: 10px;
    }
  }
</style>

