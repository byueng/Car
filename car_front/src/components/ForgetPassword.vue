<template>
    <div class="forget-password">
      <h1>忘记密码</h1>
      <form @submit.prevent="submitForm">
        <div class="form-group">
          <label for="account">用户名</label>
          <input type="account" id="account" v-model="account" required />
        </div>
        <div class="form-group">
          <label for="newPassword">新密码</label>
          <input type="password" id="newPassword" v-model="newPassword" required />
        </div>
        <div class="form-group">
          <label for="confirmPassword">确认新密码</label>
          <input type="password" id="confirmPassword" v-model="confirmPassword" required />
        </div>
        <button type="submit" @click="submitPassword">提交</button>
        <div v-if="message" :class="messageType" class="message">
        {{ message }}
      </div>
      </form>
    </div>
  </template>
  
  <script>
import axios from 'axios';

  export default {
    data() {
      return {
        account: '',
        newPassword: '',
        confirmPassword: '',
        message: '',
        messageType: '',
      };
    },
    methods: {
      async submitPassword(){
        const address = this.$config.local_address
        if (this.newPassword !== this.confirmPassword){
          this.message = '两次的密码不同'
          this.messageType = 'error'
          return
        }
        console.log('everything correct')
        try {
            const response = await axios.post(address + '/user/forgetpassword/', {
                account: this.account,
                newPassword: this.newPassword,
            })
            this.message = response.data['message']
            this.messageType = 'success'
            setTimeout(() => {
              this.$router.push('/user/login')
            }, 2000)
        }
        catch(error){
          this.message = error.response.data['message']
          this.messageType = 'error'
        }

      }
    }
  };
  </script>
  
  <style scoped>
  .forget-password {
    max-width: 400px;
    margin: 0 auto;
    padding: 20px;
    border: 1px solid #ccc;
    border-radius: 4px;
    background-color: #f9f9f9;
  }
  
  .form-group {
    margin-bottom: 15px;
  }
  
  label {
    display: block;
    margin-bottom: 5px;
  }
  
  input[type="email"] {
    width: 100%;
    padding: 8px;
    box-sizing: border-box;
  }
  
  button {
    padding: 10px 15px;
    background-color: #007bff;
    color: white;
    border: none;
    border-radius: 4px;
    cursor: pointer;
  }
  
  button:hover {
    background-color: #0056b3;
  }
  .success {
    margin-top: 20px;
    background-color: #d4edda;
    color: #155724;
  }
  .error {
    margin-top: 20px;
    background-color: #f8d7da;
    color: #721c24;
  }
  </style>