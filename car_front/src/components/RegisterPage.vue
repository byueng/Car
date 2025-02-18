<template>
  <div class="register-page">
    <h2>Register Page</h2>
    <!-- 注册表单 -->
    <form>
      <input type="text" placeholder="Accout" v-model="account" />
      <input type="password" placeholder="Password" v-model="password" />
      <input type="confirm password" placeholder="confirm Password" v-model="confirm_password" />
      <button type="submit" @click="register">Register</button>
    </form>
  </div>
</template>
  
<script>
export default {
  name: 'RegisterPage',
  data() {
    return {
      username: '',
      password: '',
    };
  },
  methods: {
    async handleregister(){
      
    },
    register() {
      this.$router.push('/user/login')
    }
  }
};
</script>
  
<style scoped>
input {
  display: block;
  margin-bottom: 10px;
  margin-left: auto;
  margin-right: auto;
}

.register-page {
  padding: 20px;
  text-align: center;
  display: flex;
  flex-direction: column;
  align-items: center;
}
</style>
  