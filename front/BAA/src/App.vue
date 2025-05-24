<template>
  <div>
    <nav>
      <RouterLink :to="{name: 'books'}">도서 목록</RouterLink>
    </nav>
    <MainView/>
  </div>
  <RouterView/>
</template>

<script setup>
  import MainView from './views/MainView.vue'
</script>

<style scoped>

</style>