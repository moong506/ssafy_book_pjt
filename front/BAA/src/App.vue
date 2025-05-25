<template>
  <div>
    <nav>
      <RouterLink :to="{name: 'main'}">홈 </RouterLink> | 
      <RouterLink :to="{name: 'books'}">도서 목록</RouterLink>
    </nav>

  </div>
  <RouterView/>
</template>

<script setup>
 
</script>

<style scoped>

</style>