<template>

  <div v-if="thread.book == bookIdParam">
    <p>쓰레드 제목 : {{ thread.title }} <button @click="goThreadDetail">상세 보기</button></p>
    <p>작성자 : {{ thread.user.username}}
      <!-- <RouterLink  :to="{ name: 'profile' , params: { userId: thread.user.id }}">
        {{ thread.user.username}}
      </RouterLink> -->
    </p>

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
  p {
  font-size: 16px;
  color: #5a4231;
  margin: 8px 0;
  font-family: 'Gowun Dodum', sans-serif;
}

button {
  background-color: #ffad60;
  color: white;
  border: none;
  padding: 6px 12px;
  border-radius: 6px;
  font-size: 14px;
  font-weight: bold;
  margin-left: 12px;
  cursor: pointer;
  box-shadow: 1px 1px 4px rgba(0, 0, 0, 0.1);
  transition: background-color 0.2s ease, transform 0.1s ease;
}

button:hover {
  background-color: #ff944d;
  transform: translateY(-2px);
}

</style>