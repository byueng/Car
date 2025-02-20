import { createApp } from 'vue';
import App from './App.vue';
import { createRouter, createWebHistory } from 'vue-router';
// router registration
import LoginPage from './components/LoginPage.vue';
import TestPage from './components/TestPage.vue';
import RegisterPage from './components/RegisterPage.vue';
import ProfilePage from './components/ProfilePage.vue';
// third 
import axios from 'axios';


const routes = [
  {
    path: '/',
    component: App,
  },
  {
    path: '/user/login',
    component: LoginPage,  // 跳转到登录页面
  },
  {
    path: '/user/test',
    component: TestPage,
  },
  {
    path: '/user/register',
    component: RegisterPage
  },
  {
    path: '/user/profile',
    component: ProfilePage
  },
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

axios.get('/config.json')
  .then((response) => {
    app.config.globalProperties.$config = response.data;  // 将配置放入全局属性
  })
  .catch((error) => {
    console.error('Error loading config.json:', error);
  })


const app = createApp(App)
app.use(router)
app.mount('#app')