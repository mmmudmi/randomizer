// Composables
import { createRouter, createWebHistory } from 'vue-router'

const routes = [
  {
    path: '/',
    component: () => import('@/layouts/default/Default.vue'),
    children: [
      {
        path: '/main',
        alias: '',
        name: 'main',
        component: () => import('@/views/Main.vue'),
      },
      {
        path: '/tag',
        name: 'tag',
        component: () => import('@/views/Tag.vue'),
      },
      {
        path: '/add',
        name: 'add',
        component: () => import('@/views/Add.vue'),
      },
      {
        path: '/remaining',
        name: 'remaining',
        component: () => import('@/views/Remaining.vue'),
      },
      {
        path: '/history',
        name: 'history',
        component: () => import('@/views/History.vue'),
      },
      {
        path: '/deleted',
        name: 'deleted',
        component: () => import('@/views/Deleted.vue'),
      }
    ],
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
})

export default router
