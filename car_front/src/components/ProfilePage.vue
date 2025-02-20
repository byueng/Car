<template>
    <div class="profile-container">
      <h1 class="profile-title">用户信息</h1>
  
      <!-- 个人信息显示区域 -->
      <div class="profile-info" v-if="!isEditing">
        <p><strong>用户名:</strong> {{ user.account }}</p>
        <p><strong>邮箱:</strong> {{ user.email }}</p>
        <p><strong>电话:</strong> {{ user.phone }}</p>
        <p><strong>生日日期:</strong> {{ user.birthdate }}</p>
        
        <button class="edit-button" @click="isEditing = true">Edit</button>
      </div>
    </div>
  </template>
  
  <script>
//   import axios from 'axios';
  export default {
    data() {
      return {
        isEditing: false,  // 是否处于编辑模式
        user: {
          account: '',
          email: '',
          phone: '',
          birthdate: ''
        }
      };
    },
    methods: {
        async GetProfile(){
          const address = this.$config.local_address
          console.log(address)
        }
    },
    beforeRouteEnter(to, from, next) {
      next(vm => {
        vm.GetProfile();
      });
    }
  };
  </script>
  
  <style scoped>
  .profile-container {
    max-width: 800px;
    margin: 20px auto;
    padding: 20px;
    background-color: #fff;
    border-radius: 8px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  }
  
  .profile-title {
    text-align: center;
    font-size: 2rem;
    margin-bottom: 20px;
  }
  
  .profile-info {
    text-align: left;
  }
  
  .profile-info p {
    font-size: 1rem;
    margin: 8px 0;
  }
  
  .edit-button {
    background-color: #007BFF;
    color: white;
    border: none;
    padding: 10px 20px;
    cursor: pointer;
    border-radius: 5px;
  }
  
  .edit-button:hover {
    background-color: #0056b3;
  }
  
  .profile-form {
    text-align: left;
  }
  
  .form-group {
    margin-bottom: 20px;
  }
  
  .form-group label {
    font-weight: bold;
  }
  
  .form-group input {
    width: 100%;
    padding: 8px;
    margin-top: 5px;
    border-radius: 5px;
    border: 1px solid #ccc;
  }
  
  .submit-button {
    background-color: #28a745;
    color: white;
    border: none;
    padding: 10px 20px;
    cursor: pointer;
    border-radius: 5px;
    margin-right: 10px;
  }
  
  .submit-button:hover {
    background-color: #218838;
  }
  
  .cancel-button {
    background-color: #dc3545;
    color: white;
    border: none;
    padding: 10px 20px;
    cursor: pointer;
    border-radius: 5px;
  }
  
  .cancel-button:hover {
    background-color: #c82333;
  }
  </style>
  