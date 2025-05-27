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
      if (err.response) {
        const status = err.response.status
        if (status === 500) {
          // 500 에러면 로그인 페이지로 리다이렉트
          router.push({ name: 'login' })
        } else {
          // 기타 오류 메시지 표시
          const errName = Object.values(err.response.data)
          // const message = err.response.data?.detail || '오류가 발생했습니다.'
          alert(`오류 코드 ${status}: ${errName}`)
        }
      } else {
        // 서버 응답이 없는 경우 (네트워크 오류 등)
        alert('네트워크 오류가 발생했습니다. 인터넷 연결을 확인해주세요.')
      }

      console.error('에러 디버깅:', err)
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
    .catch(err =>{
      const status = err.response.status
      const errName = Object.values(err.response.data)
      alert(`오류 코드 ${status}: ${errName}`)
    })
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