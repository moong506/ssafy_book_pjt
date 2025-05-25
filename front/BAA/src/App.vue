<template>
  <div>
    <nav>
      <RouterLink :to="{name: 'main'}">홈 </RouterLink> | 
      <RouterLink :to="{name: 'books'}">도서 목록</RouterLink> | 
    
      <RouterLink :to="{name: 'signUp'}">회원 가입</RouterLink> | 
      <RouterLink :to="{name: 'login'}">로그인</RouterLink>

    </nav>

  </div>
  <RouterView/>
</template>

<script setup>
 
</script>

<style scoped>

</style>