import {createRouter, createWebHistory, RouteRecordRaw} from 'vue-router'

const routes: Array<RouteRecordRaw> = [
  {
    path: '/',
    name: 'one',
    component: () => import("@/views/One.vue")
  },
  {
    path: '/two',
    name: 'two',
    component: () => import('@/views/Two.vue')
  },
  {
    path: '/three',
    name: 'three',
    component: () => import('@/views/Three.vue')
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
