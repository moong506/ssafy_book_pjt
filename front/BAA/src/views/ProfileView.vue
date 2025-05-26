<template>
  <div>
    {{ profile }}
  </div>
</template>

<script setup>
  import axios from 'axios'
  import { useAccountStore } from '@/stores/accounts'
  import { ref, onMounted } from 'vue'
  const accountStore = useAccountStore()
  const profile = ref([])

  const createProfile = function() {
  axios({
      method: 'get',
      url: `http://127.0.0.1:8000/dj-rest-auth/user/`,
      headers: {
        'Authorization' : `Token ${accountStore.token}`
      }
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

</style>