<template>
  <div class="container">
    <!-- 主页标题 -->
    <div class="header">
      <div class="logo-title">
        <img src="@/assets/logo.png" alt="Logo" class="logo" />
        <h1 class="title">二手车交易平台</h1>
      </div>
      <div class="header-buttons">
    <!-- 登录按钮，只在未登录时显示 -->
      <button v-if="!isLoggedIn" class="btn login-button" @click="goToLogin">登录</button>

      <!-- 欢迎语或登出按钮，登录状态时显示 -->
      <div v-if="isLoggedIn" class="welcome-section">
        <img class="avatar" src='@/assets/default-avatar.jpg' alt="头像" @click="goToProfile" />
        <button class="btn logout-button" @click="logout">退出登录</button>
      </div>
    </div>
    </div>

    <!-- 车辆管理 -->
    <div class="car-section">
      <h2>车辆信息</h2>
      <!-- <input v-model="searchQuery" placeholder="搜索品牌/价格/车龄" class="search-box" @input="searchCars"/> -->
      <div class="search-section">
        <select v-model="searchCriteria.brand" class="search-box" @change="fetchBrands">
          <option value="" disabled>选择品牌</option>
          <option v-for="brand in brands" :key="brand" :value="brand">{{ brand }}</option>
        </select>

        <!-- 车型搜索 -->
        <select v-model="searchCriteria.model" class="search-box" :disabled="!searchCriteria.brand">
          <option value="" disabled>选择车型</option>
          <option v-for="model in models" :key="model" :value="model">{{ model }}</option>
        </select>

        <!-- 价格搜索 -->
        <input 
          v-model="searchCriteria.price" 
          placeholder="输入价格" 
          class="search-box" 
          type="number" 
        />
        <button class="btn" @click="searchCars">搜索</button>
      </div>

      <div class="car-list">
        <div v-for="car in filteredCars" :key="car.id" class="car-item">
          <img :src="getImageUrl(car.image)" class="car-image" />
          <div class="car-details">
            <h3>{{ car.brand }} - {{ car.model }}</h3>
            <p>价格: {{ car.price }} 万元</p>
            <p>车龄: {{ car.age }} 年</p>
            <button class="btn" @click="bookCar(car.id)">预约看车</button>
          </div>
        </div>
      </div>
      <button class="btn" @click="goToCarMangement">进入车辆管理后台</button>
    </div>

    <!-- 交易管理 -->
    <div class="transaction-section">
      <h2>交易管理</h2>
      <button class="btn" @click="goToOrders">订单跟踪</button>
    </div>

    <!-- 后台管理入口 -->
    <div v-if="isAdmin" class="admin-section">
      <h2>后台管理</h2>
      <button class="btn" @click="goToAdmin">进入管理后台</button>
    </div>
  </div>
  <!-- <router-view></router-view> -->
     <!-- 页脚 -->
  <footer class="footer">
    <div class="footer-content">
      <p>联系方式: support@usedcarplatform.com | 电话: 123-456-7890</p>
      <p>平台说明: 二手车交易平台，致力于为用户提供安全、便捷的车辆交易服务。</p>
      <p>版权所有 © 2025 二手车交易平台</p>
    </div>
  </footer>
</template>

<script>
import axios from 'axios';
export default {
  data() {
    return {
      searchQuery: "",
      isLogined: false,
      isAdmin: false, // 假设从后端获取权限
      searchCriteria: {
        brand: "", // 品牌
        model: "", // 车型
        price: "" // 价格
      },
      cars: [],
      brands: [],
      models: [],
    };
  },
  created() {
    // 页面加载时检查 token
    const token = localStorage.getItem('token');
    if (token) {
      this.isLoggedIn = true;
    }
  },
  computed: {
    filteredCars() {
      return this.cars.filter(car =>
        car.brand.includes(this.searchQuery) ||
        car.price.toString().includes(this.searchQuery) ||
        car.age.toString().includes(this.searchQuery)
      );
    }
  },
  methods: {
    async searchCars() {
      try {
        const params = {
          brand: this.searchCriteria.brand || "",
          model: this.searchCriteria.model || "",
          price: this.searchCriteria.price || ""
        };
        const response = await axios.get("http://127.0.0.1:8000/car/search/", { params });
        this.cars = Array.isArray(response.data) ? response.data : [];
      } catch (error) {
        console.error("搜索车辆信息失败:", error);
        this.cars = [];
      }
    },
    getImageUrl(imagePath) {
      if (!imagePath) {
        return ""; // 如果没有图片路径，返回空字符串
      }
      return `http://127.0.0.1:8000${imagePath}`;
    },
    logout(){
      localStorage.removeItem('token');
      this.isLoggedIn = false;
      this.$router.push('/').then(() => {
        window.location.reload(); // 手动刷新页面
      })
    },
    async bookCar(id) {
      const token = localStorage.getItem('token'); // 检查是否有登录的 token
      if (!token) {
        alert('请先登录后再预约车辆！');
        this.goToLogin(); // 跳转到登录页面
        return;
      }

      // 如果用户已登录，发送预约请求
      try {
    // 如果用户已登录，发送预约请求
      const response = await axios.post("http://localhost:8000/car/bookcar/", {
        user_id: localStorage.getItem('account'),
        car_id: id,
      });
      // 请求成功后的处理
      alert(response.data.message);
    } catch (error) {
      // 捕获错误并处理
      console.error('预约失败:', error);
      alert('预约失败，请稍后重试！');
    }
    },
    async fetchCars() {
      try {      
        const response = await axios.get("http://127.0.0.1:8000/car/info/");
        this.cars = response.data;
      } catch (error) {
        console.error("获取车辆信息失败:", error);
      }
    },
    async fetchBrands(){
      try {
        const response = await axios.get("http://127.0.0.1:8000/car/brands/")
        this.brands = Array.isArray(response.data.brands) ? response.data.brands : []
      } catch (error){
        console.error("获取车型信息失败:", error);
        this.brands = [];
        }
    },
    async fetchModels(){
      try {
        const response = await axios.get("http://127.0.0.1:8000/car/models/")
        this.models = Array.isArray(response.data.models) ? response.data.models : []
      } catch (error){
        console.error("获取车型信息失败:", error);
        this.models = [];
        }
    },
    goToLogin() {
      this.$router.push("/user/login");
    },
    goToTest() {
      this.$router.push("/user/test");
    },
    goToOrders() {
      this.$router.push("/user/orders");
    },
    goToCarMangement(){
      this.$router.push("/car/management");
    },
    goToAdmin() {
      this.$router.push("/user/admin");
    },
    goToProfile(){
      const account = localStorage.getItem('account')
      this.$router.push({ path: "/user/profile", query: { id: account } });
    },
  },
  mounted() {
    this.fetchCars(),
    this.fetchBrands(),
    this.fetchModels()
  }
};
</script>

<style scoped>
.header {
  display: flex;
  justify-content: space-between; /* 两端对齐 */
  align-items: center; /* 垂直居中 */
  padding: 5px 10px;
  width: 100%;
}
.logo-title {
  display: flex;
  align-items: center; /* 垂直居中 */
}

.logo {
  height: 30px; /* 调整 logo 大小 */
  margin-right: 10px; /* 增加 logo 和标题之间的间距 */
}
.title {
  font-size: 20px; /* 调整标题字体大小 */
  font-weight: bold;
  margin: 0;
}
.header-buttons {
  display: flex;
  gap: 10px; /* 按钮之间的间距 */
}
.container {
  max-width: 1000px;
  margin: auto;
  text-align: center;
  padding: 10px; /* 添加整体内边距 */
}

.btn {
  padding: 8px 12px; /* 减少按钮内边距 */
  margin: 3px; /* 减少按钮间距 */
  font-size: 14px; /* 减小按钮字体大小 */
  background-color: #007bff;
  color: white;
  border: none;
  border-radius: 3px; /* 减小圆角 */
  cursor: pointer;
}

.btn:hover {
  background-color: #0056b3;
}

.search-box {
  padding: 8px; /* 减少输入框内边距 */
  width: 75%; /* 减小宽度 */
  margin-bottom: 10px; /* 减少底部间距 */
  border: 1px solid #ccc;
  border-radius: 3px; /* 减小圆角 */
}

.car-list {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between;
  gap: 10px; /* 使用 gap 控制间距 */
}

.car-item {
  width: 48%; /* 减少宽度以增加间距 */
  background: #f9f9f9;
  padding: 8px; /* 减少内边距 */
  border-radius: 3px; /* 减小圆角 */
  margin-bottom: 10px; /* 减少底部间距 */
}

.car-image {
  width: 100%;
  border-radius: 3px; /* 减小圆角 */
}

.car-details h3 {
  font-size: 16px; /* 减小标题字体大小 */
  margin: 5px 0; /* 减少上下间距 */
}

.car-details p {
  font-size: 14px; /* 减小描述字体大小 */
  margin: 3px 0; /* 减少上下间距 */
}
.footer {
  background-color: #f1f1f1;
  padding: 10px;
  text-align: center;
  margin-top: 20px;
  font-size: 14px;
  color: #666;
}

.footer-content p {
  margin: 5px 0;
}
.welcome-section {
  display: flex;
  align-items: center; /* 垂直居中 */
  gap: 10px; /* 控制头像和按钮之间的水平间距 */
}

.avatar {
  width: 40px;
  height: 40px;
  border-radius: 50%;
  cursor: pointer;
  border: 2px solid #ccc;
}

.avatar:hover {
  border-color: #007bff;
}

.logout-button {
  background-color: #dc3545;
  color: white;
  border: none;
  border-radius: 3px;
  padding: 8px 12px;
  cursor: pointer;
}

.logout-button:hover {
  background-color: #c82333;
}
</style>