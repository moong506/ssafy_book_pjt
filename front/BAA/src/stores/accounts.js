import axios from "axios"
import { computed, ref } from 'vue'
import { defineStore } from 'pinia'
import { useRouter } from 'vue-router'


export const useAccountStore = defineStore('account', () => {
  const token = ref(localStorage.getItem('authToken') || null)
  const username = ref(localStorage.getItem('username') || null)
  const password = ref(localStorage.getItem('password') || null)

  const router = useRouter()
  const signUp = function (payload) {


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
      router.push({name:'login'})

    })
    // 아래 디버깅때매 추가함
    ////////////////////////////////
    .catch(err => {
      console.log(err.response.data)
      console.error('회원가입 실패:', err.response?.data || err.message)
      const errName = Object.values(err.response.data)
      alert(errName)
    })

    
    ////////////////////////////////
  }

  const logIn = function({username: inputUsername, password: inputPassword}) {
    axios({
      method: 'POST',
      url : 'http://127.0.0.1:8000/dj-rest-auth/login/',
      data:{
        username: inputUsername,
        password : inputPassword
      }
    })
    .then(res => {
      token.value = res.data.key
      localStorage.setItem('authToken', token.value) 

      username.value = inputUsername
      password.value = inputPassword
      localStorage.setItem('username', username.value) 
      localStorage.setItem('password', password.value) 
      router.push({name:'main'})
    })
    .catch(err =>console.log(err))
  }


  const isLogin = computed(() => {
    return token.value ? true : false
  })

  const logOut = function(){
    axios({
      method: 'POST',
      url : 'http://127.0.0.1:8000/dj-rest-auth/logout/',
    })
    .then(res => {
      token.value = null
      localStorage.removeItem('authToken')
      localStorage.removeItem('username')
      localStorage.removeItem('password')
      username.value = null
      password.value = null

      router.push({name:'main'})

    })
    .catch(err =>console.log(err))
  }

  return { username, password, signUp, logIn, token, isLogin, logOut }
},  {persist: {paths: ['token', 'username'], }})