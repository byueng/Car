<template>
  <div class="login-container">
    <h2>登录二手车交易平台</h2>
    <form @submit.prevent="handleLogin">
      <div>
        <label for="account">账号</label>
        <input type="text" v-model="account" id="account" required />
      </div>
      <div>
        <label for="password">密码</label>
        <input type="password" v-model="password" id="password" required />
      </div>
      <button type="submit">Login</button>
      <div>
        <button type="forget button" class="forget-password-button" @click="ForgetPassword">忘记密码?</button>
      </div>
      <div>
        <button type="register button" class="register-button" @click="RegisterLogin">没有用户？创建一个新的</button>
      </div>
    </form>
    <div v-if="message" :class="messageType" class="message">
    {{ message }}
  </div>
  </div>
</template>

<script>
// 导入 axios
import axios from 'axios';

export default {
data() {
  return {
    account: '',
    password: '',
    message: '',
    messageType: ''
  }
},
methods: {
  async handleLogin() {
    const address = this.$config.local_address

    try {
      // 使用 axios 向 Django 后端发送请求
      const response = await axios.post(address + '/user/login/', {
        account: this.account,
        password: this.password,
      })
      if (response.status === 201) {
        const data = response.data
        // 登录成功，存储 token 到 localStorage
        localStorage.setItem('token', data.token)
        localStorage.setItem('account', this.account)
        this.message = response.data['message']
        this.messageType = 'success'
        setTimeout(() => {
          this.$router.push('/')
        }, 2000)
      }
    } catch (error) {
      // 处理请求错误
      this.message = error.response.data['message']
      this.messageType = 'error'
      }
    },
    RegisterLogin() {
      this.$router.push('/user/register')
    },
    ForgetPassword() {
      this.$router.push('/user/forget')
    },
  },
}
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

.register-button {
  position: fixed;
  bottom: 20px;
  right: 20px;
  padding: 10px 20px;
  background-color: #28a745;
  color: white;
  border: none;
  border-radius: 5px;
  font-size: 16px;
  cursor: pointer;
}

.register-button:hover {
  background-color: #218838;
}

.forget-password-button {
  display: block;
  margin-top: 10px;
  margin-left: auto;
  color: blue;
  cursor: pointer;
  /* text-decoration: underline; */
}

.message {
  margin-top: 20px;
  padding: 10px;
  border-radius: 5px;
  font-weight: bold;
  text-align: center;
}

.success {
  background-color: #d4edda;
  color: #155724;
}

.error {
  background-color: #f8d7da;
  color: #721c24;
}
</style>