<template>
  <div class="profile-wrapper">
    <!-- 프로필 카드 -->
    <div class="profile-card" v-if="profile">
      <h1>{{ profile.nickname }}님의 프로필</h1>
      <img
        v-if="profile.profile_img"
        :src="profile.profile_img"
        alt="프로필 이미지"
        class="profile-img"
      />
      <div v-else class="default-img">👤</div>

      <ul class="profile-info">
        <li><strong>아이디:</strong> {{ profile.username }}</li>
        <li><strong>이메일:</strong> {{ profile.email }}</li>
        <li><strong>이름:</strong> {{ profile.last_name }} {{ profile.first_name }}</li>
        <li><strong>성별:</strong> {{ profile.gender === 'M' ? '남성' : '여성' }}</li>
        <li><strong>나이:</strong> {{ profile.age }}</li>
        <li><strong>주간 평균 독서 시간:</strong> {{ profile.weekly_avg_reading_time }}시간</li>
        <li><strong>연간 독서량:</strong> {{ profile.annual_reading_amount }}권</li>
      </ul>
    </div>

    <!-- 찜한 도서 카드 -->
    <div class="book-card" v-if="bookList?.length">
      <h2>📚 찜한 도서 목록</h2>
      <div class="book-grid">
        <div class="book-item" v-for="book in bookList" :key="book.id">
          <img :src="book.cover" alt="book cover" class="book-cover" />
          <p class="book-title">{{ book.title }}</p>
          <RouterLink class="detail-link" :to="{ name : 'book', params:{'bookId': book.id} }">상세 보기</RouterLink>
        </div>
      </div>
    </div>

  </div>
  


</template>


<script setup>
  import axios from 'axios'
  import { useAccountStore } from '@/stores/accounts'
  import { ref, onMounted } from 'vue'

  const accountStore = useAccountStore()
  const profile = ref(null)
  const bookList = ref(null)
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
        bookList.value = res.data.like_books
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
  .profile-wrapper {
    width: 90%;
    max-width: 1000px;
    margin: 40px auto;
    display: flex;
    flex-direction: column;
    gap: 32px;
  }

  .profile-card,
  .book-card {
    background-color: #fff8f1;
    border: 2px solid #f7d8c4;
    border-radius: 20px;
    padding: 32px;
    box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.05);
    font-family: 'Gowun Dodum', sans-serif;
    color: #5a4231;
    text-align: center;
  }

  h1 {
    margin-bottom: 15px;
    color: #ce7c5b;

  }

  .profile-img,
  .default-img {
    width: 120px;
    height: 120px;
    border-radius: 50%;
    object-fit: cover;
    /* margin-bottom: 20px; */
    margin: 0 auto 20px;
    border: 3px solid #ffd6b1;
    background-color: #fff;
  }

  .default-img {
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 48px;
  }

  .profile-info {
    list-style: none;
    padding: 0;
    text-align: center;
    font-size: 16px;
  }

  .profile-info li {
    padding: 10px 0;
    border-bottom: 1px dashed #f0c7a4;
  }

  .profile-info li strong {
    color: #ce7c5b;
  }

  .book-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(120px, 1fr));
    gap: 20px;
    justify-items: center;
  }

  .book-item {
    display: flex;
    flex-direction: column;
    align-items: center;
  }

  .book-cover {
    width: 100px;
    height: 150px;
    object-fit: cover;
    border-radius: 8px;
    box-shadow: 1px 1px 6px rgba(0, 0, 0, 0.1);
    margin-bottom: 8px;
    border: 1px solid #f3c8a2;
  }

  .book-title {
    font-size: 14px;
    color: #5a4231;
    text-align: center;
  }

  @media (max-width: 768px) {
    .profile-card,
    .book-card {
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

    .book-cover {
      width: 80px;
      height: 120px;
    }

    .book-title {
      font-size: 13px;
    }
  }
  .detail-link {
    text-decoration: none;
    color: #CE7C5B;
    font-weight: bold;
    background-color: #FFF1E6;
    padding: 0.4rem 0.8rem;
    border-radius: 12px;
    transition: 0.2s;
    box-shadow: 1px 1px 4px rgba(0, 0, 0, 0.05);
  }

  .detail-link:hover {
    background-color: #FFBC8B;
    color: #fff;
  }

</style>

