<template>
  <div>
    <h2>注册</h2>
    <form @submit.prevent="register">
      <input v-model="username" placeholder="用户名" required />
      <input v-model="email" placeholder="邮箱" type="email" required />
      <input v-model="password" placeholder="密码" type="password" required />
      <input v-model="confirmPassword" placeholder="确认密码" type="password" required />
      <button type="submit">注册</button>
    </form>
    <p v-if="error">{{ error }}</p>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      username: '',
      email: '',
      password: '',
      confirmPassword: '',
      error: '',
    };
  },
  methods: {
    async register() {
      if (this.password !== this.confirmPassword) {
        this.error = '两次输入的密码不一致';
        return;
      }
      try {
        const response = await axios.post('/api/auth/register', {
          username: this.username,
          email: this.email,
          password: this.password,
        });
        if (response.data.success) {
          this.$router.push('/login'); // 跳转到登录页面
        }
      } catch (err) {
        this.error = err.response.data.message || '注册失败';
      }
    },
  },
};
</script>