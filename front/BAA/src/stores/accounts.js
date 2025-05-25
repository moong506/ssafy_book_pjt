import axios from "axios"
import { ref } from 'vue'
import { defineStore } from 'pinia'

export const useAccountStore = defineStore('account', () => {
  const token = ref(null)

  const signUp = function (payload) {
    console.log(payload)
    axios({
      method: 'POST',
      // url: 'http://127.0.0.1:8000/accounts/signup/', // 원래 코드 이거, 아래 registration으로 수정함
      url: 'http://127.0.0.1:8000/dj-rest-auth/registration/',
      data:{
        ...payload,
    //   username,
    //   password1,
    //   password2, 
    //   lastname, 
    //   firstname,
    //   email,
    //   gender,
    //   weekly_age_reading_time,
    //   annual_reading_amount,
    //   profile_img 
      }
    })
    .then(res => {
      console.log('회원가입성공')
    //   for (let i = 0; i < articles.value.length; i++){
    //     articles.value[i].id = i+1

    //   }
    })
    // 아래 디버깅때매 추가함
    ////////////////////////////////
    .catch(err => {
  console.error('회원가입 실패:', err.response?.data || err.message)
    })
    ////////////////////////////////
  }

  const logIn = function({username, password}) {
    axios({
      method: 'POST',
      url : 'http://127.0.0.1:8000/accounts/login/',
      data:{
        username, password
      }
    })
    .then(res => {
      token.value = res.data.key
      console.log(res)
    })
    .catch(err =>console.log(err))
  }


  return { signUp, logIn, token }
}, {persist: true})