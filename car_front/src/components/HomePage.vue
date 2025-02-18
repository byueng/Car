<!-- HTML code -->
<template>
    <h1></h1>
    <div>
        <button v-if="$route.path == '/'" class="login-button" @click="goToLogin">登录</button>
    </div>
    <div>
        <button v-if="$route.path == '/'" class="test-button" @click="goToTest">测试</button>
    </div>
    <!-- 安装路由 -->
    <router-view></router-view>
</template>

<!-- JS code -->
<script>
    export default{
        props: {
            msg: String
        },
        methods: {
            goToLogin(){
                this.$router.push('/user/login');
            },
            goToTest(){
                this.$router.push('/user/test');
            },
        }
    }
</script>

<!-- CSS code -->
<style scoped>
    .homepage {
    position: relative;
    min-height: 100vh; /* 页面至少占满整个视口高度 */
    background-color: #f5f5f5; /* 页面背景色 */
    }

    .login-button {
    position: fixed;
    top: 20px;
    right: 20px;
    padding: 10px 20px;
    background-color: #007BFF;
    color: white;
    border: none;
    border-radius: 5px;
    font-size: 16px;
    cursor: pointer;
    }

    .login-button:hover {
    background-color: #0056b3;
    }

    .test-button {
    position: fixed;
    top: 20px;
    left: 20px;
    padding: 10px 20px;
    background-color: #28a745;
    color: white;
    border: none;
    border-radius: 5px;
    font-size: 16px;
    cursor: pointer;
    }

    .test-button:hover {
    background-color: #218838;
    }
</style>
