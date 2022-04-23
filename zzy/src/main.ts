import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import '@/assets/normalize.css'
import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'

createApp(App).use(ElementPlus).use(router).mount('#app')
