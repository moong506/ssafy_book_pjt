<template>

  <div v-if="thread.book == bookIdParam">
    <p>쓰레드 제목 : {{ thread.title }} <button @click="goThreadDetail">상세 보기</button></p>
    <p>작성자 : {{ thread.user.username}}
      <!-- <RouterLink  :to="{ name: 'profile' , params: { userId: thread.user.id }}">
        {{ thread.user.username}}
      </RouterLink> -->
    </p>
    <hr>
  </div>
</template>

<script setup>

  import { useRoute, useRouter } from 'vue-router'
  import { useThreadsStore } from '@/stores/threads'
  const route = useRoute()
  const router = useRouter()
  const props = defineProps({
    thread: Object
  })
  
  const thread = props.thread
  
  const threadsStore = useThreadsStore()
  const bookIdParam = Number(route.params.bookId)

  const goThreadDetail = function() {
    threadsStore.selectedThread = thread
    
    router.push({name:'thread', params:{bookId: bookIdParam, threadId: thread.id}})
  }
</script>

<style scoped>

</style>