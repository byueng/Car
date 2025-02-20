<template>
  <div class="register-page">
    <h2>注册页面</h2>
    <!-- 注册表单 -->
    <form @submit.prevent="handleRegister">
      <input type="text" placeholder="账号" v-model="account" />
      <input type="password" placeholder="密码" v-model="password" />
      <input type="password" placeholder="确认密码" v-model="confirm_password" />
      <button type="submit">注册</button>
    </form>

    <!-- 成功或失败消息 -->
    <div v-if="message" :class="messageType" class="message">
      {{ message }}
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      account: '',
      password: '',
      confirm_password: '',
      message: '',
      messageType: '',
    };
  },
  methods: {
    async handleRegister() {
      const AddressConfig = await axios.get("/config.json")
      const address = AddressConfig.data['local_address']
      console.log(address)
      if (this.password !== this.confirm_password) {
        this.message = '两次的密码不同'
        this.messageType = 'error'
        return 
      }
      if (this.account === '' || this.password === '' || this.confirm_password === ''){
        this.message = '需要的信息不能为空'
        this.messageType = 'error'
        return 
      }
      try {
        const response = await axios.post(address + '/user/register/', {
          account: this.account,
          password: this.password
        })
        if (response.status === 201) {
          this.message = response.data['message']
          this.messageType = 'success'
          setTimeout(() => {
            this.$router.push('/user/login')
          }, 2000)
        }
      } catch (error) {
        this.message = error.response.data['message']
        this.messageType = 'error'
      }
    },
  },
};
</script>

<style scoped>
.register-page {
  max-width: 400px;
  margin: 50px auto;
  padding: 20px;
  background-color: #f9f9f9;
  border-radius: 8px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

h2 {
  text-align: center;
  color: #333;
}

form {
  display: flex;
  flex-direction: column;
}

input {
  margin-bottom: 15px;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 5px;
  font-size: 16px;
}

button {
  padding: 10px;
  background-color: #4CAF50;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  font-size: 16px;
}

button:hover {
  background-color: #45a049;
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