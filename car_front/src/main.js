import { createApp } from 'vue';
import App from './App.vue';

import { createRouter, createWebHistory } from 'vue-router';
// router registration
import LoginPage from './components/LoginPage.vue'; // 登录页面组件
import TestPage from './components/TestPage.vue';


const routes = [
  {
    path: '/',
    component: App,
  },
  {
    path: '/login',
    component: LoginPage,  // 跳转到登录页面
  },
  {
    path: '/test',
    component: TestPage,
  }
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

createApp(App).use(router).mount('#app');
