<template>
    <div class="login-container">
      <h2>Login to Second-Hand Car Trading Platform</h2>
      <form @submit.prevent="handleLogin">
        <div>
          <label for="username">Username</label>
          <input type="text" v-model="username" id="username" required />
        </div>
        <div>
          <label for="password">Password</label>
          <input type="password" v-model="password" id="password" required />
        </div>
        <button type="submit">Login</button>
      </form>
      <p v-if="errorMessage" class="error">{{ errorMessage }}</p>
    </div>
  </template>
  
  <script>
  // 导入 axios
  import axios from 'axios';
  
  export default {
    data() {
      return {
        username: '',
        password: '',
        errorMessage: ''
      };
    },
    methods: {
      async handleLogin() {
        try {
          // 使用 axios 向 Django 后端发送请求
          const response = await axios.post('http://127.0.0.1:8000/user/login/', {
            username: this.username,
            password: this.password,
          });
  
          if (response.status === 200) {
            const data = response.data;
            // 登录成功，存储 token 到 localStorage
            localStorage.setItem('token', data.token);
            this.$router.push('/dashboard'); // 登录成功后跳转到仪表盘页面
          }
        } catch (error) {
          // 处理请求错误
          if (error.response) {
            this.errorMessage = error.response.data.detail || 'Login failed. Please try again.';
          } else {
            this.errorMessage = 'Something went wrong. Please try again later.';
          }
        }
      }
    }
  };
  </script>
  
  <style scoped>
  /* 这里添加一些基本样式 */
  .login-container {
    width: 300px;
    margin: auto;
    padding: 20px;
    border: 1px solid #ccc;
    border-radius: 5px;
  }
  
  form {
    display: flex;
    flex-direction: column;
  }
  
  input {
    margin-bottom: 10px;
    padding: 8px;
    border: 1px solid #ddd;
    border-radius: 4px;
  }
  
  button {
    padding: 10px;
    background-color: #4caf50;
    color: white;
    border: none;
    border-radius: 4px;
  }
  
  button:hover {
    background-color: #45a049;
  }
  
  .error {
    color: red;
    font-size: 14px;
    margin-top: 10px;
  }
  </style>
  