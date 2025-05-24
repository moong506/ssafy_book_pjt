import { createRouter, createWebHistory } from 'vue-router'
import MainView from '@/views/MainView.vue'
import BookListView from '@/views/BookListView.vue'
import BookDetailView from '@/views/BookDetailView.vue'
import ThreadListView from '@/views/ThreadListView.vue'
import ThreadDetailView from '@/views/ThreadDetailView.vue'
import ThreadWriteView from '@/views/ThreadWriteView.vue'
import ProfileView from '@/views/ProfileView.vue'
import LoginView from '@/views/LoginView.vue'
import SignUpView from '@/views/SignUpView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'main',
      component: MainView,
    },
    {
      path: '/books',
      name: 'books',
      component: BookListView,
    },
    {
      path: '/books/:bookId',
      name: 'book',
      component: BookDetailView,
    },
    {
      path: '/books/:bookId/threads',
      name: 'threads',
      component: ThreadListView,
    },
    {
      path: '/books/:bookId/threads/:threadId',
      name: 'thread',
      component: ThreadDetailView,
    },
    {
      path: '/books/:bookId/threadWrite',
      name: 'threadWrite',
      component: ThreadWriteView,
    },
    {
      path: '/accounts/:userId',
      name: 'profile',
      component: ProfileView,
    },
    {
      path : '/accounts/signUp',
      name: 'signUp',
      component : SignUpView
    },
    {
      path : '/accounts/login',
      name: 'login',
      component : LoginView
    }
    
  ],
})

export default router
