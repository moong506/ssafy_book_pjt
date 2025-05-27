<template>
  <div class="profile-card" v-if="profile">
    <h2>{{ profile.nickname }}님의 프로필</h2>

    <img v-if="profile.profile_img" :src="profile.profile_img" alt="프로필 이미지" class="profile-img" />
    <div v-else class="default-img">👤</div>

    <ul class="profile-info">
      <li><strong>아이디:</strong> {{ profile.username }}</li>
      <li><strong>이메일:</strong> {{ profile.email }}</li>
      <li><strong>이름:</strong> {{ profile.last_name }} {{ profile.first_name }}</li>
      <li><strong>성별:</strong> {{ profile.gender === 'M' ? '남성' : '여성' }}</li>
      <li><strong>나이:</strong> {{ profile.age }}</li>
      <li><strong>주간 독서 시간:</strong> {{ profile.weekly_avg_reading_time }}시간</li>
      <li><strong>연간 독서량:</strong> {{ profile.annual_reading_amount }}권</li>
    </ul>
  </div>
</template>

<script setup>
  import axios from 'axios'
  import { useAccountStore } from '@/stores/accounts'
  import { ref, onMounted } from 'vue'

  const accountStore = useAccountStore()
  const profile = ref(null)

  const createProfile = function () {
    axios({
      method: 'get',
      url: `http://127.0.0.1:8000/dj-rest-auth/user/`,
      headers: {
        Authorization: `Token ${accountStore.token}`,
      },
    })
      .then(res => {
        profile.value = res.data
      })
      .catch(err => {
        console.log(err)
      })
  }

  onMounted(() => {
    createProfile()
  })
</script>

<style scoped>
  .profile-card {
    width: 90%;
    max-width: 800px;
    margin: 50px auto;
    padding: 40px;
    background-color: #fff8f1;
    border: 2px solid #f7d8c4;
    border-radius: 20px;
    box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.05);
    font-family: 'Gowun Dodum', sans-serif;
    color: #5a4231;
    text-align: center;
    box-sizing: border-box;
  }

  h2 {
    margin-bottom: 24px;
    color: #ce7c5b;
    font-size: 24px;
  }

  .profile-img {
    width: 140px;
    height: 140px;
    border-radius: 50%;
    object-fit: cover;
    margin-bottom: 20px;
    border: 3px solid #ffd6b1;
    background-color: #fff;
  }

  .default-img {
    width: 140px;
    height: 140px;
    border-radius: 50%;
    background-color: #ffe3d1;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 48px;
    margin: 0 auto 20px;
    border: 3px solid #ffd6b1;
  }

  .profile-info {
    list-style: none;
    padding: 0;
    text-align: left;
    font-size: 17px;
  }

  .profile-info li {
    padding: 10px 0;
    border-bottom: 1px dashed #f0c7a4;
  }

  .profile-info li strong {
    color: #ce7c5b;
    margin-right: 6px;
  }

  @media (max-width: 768px) {
    .profile-card {
      padding: 24px;
    }

    .profile-img,
    .default-img {
      width: 100px;
      height: 100px;
      font-size: 40px;
    }

    .profile-info {
      font-size: 15px;
    }

    h2 {
      font-size: 20px;
    }
  }
</style>

