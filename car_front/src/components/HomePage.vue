<template>
  <div class="container">
    <!-- 主页标题 -->
    <h1 class="title">二手车交易平台</h1>

    <!-- 用户管理 -->
    <div class="user-section">
      <button v-if="$route.path == '/'" class="btn login-button" @click="goToLogin">登录</button>
      <button v-if="$route.path == '/'" class="btn test-button" @click="goToTest">
        <i class="fas fa-vial">测试</i>
      </button>
    </div>

    <!-- 车辆管理 -->
    <div class="car-section">
      <h2>车辆信息</h2>
      <input v-model="searchQuery" placeholder="搜索品牌/价格/车龄" class="search-box" />
      <div class="car-list">
        <div v-for="car in filteredCars" :key="car.id" class="car-item">
          <img :src="car.image" class="car-image" />
          <div class="car-details">
            <h3>{{ car.brand }} - {{ car.model }}</h3>
            <p>价格: {{ car.price }} 万元</p>
            <p>车龄: {{ car.age }} 年</p>
            <button class="btn" @click="bookCar(car.id)">预约看车</button>
          </div>
        </div>
      </div>
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
  <router-view></router-view>
</template>

<script>
export default {
  data() {
    return {
      searchQuery: "",
      isAdmin: false, // 假设从后端获取权限
      cars: [
        { id: 1, brand: "Toyota", model: "Camry", price: 15, age: 3, image: "car1.jpg" },
        { id: 2, brand: "Honda", model: "Civic", price: 12, age: 2, image: "car2.jpg" }
      ]
    };
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
    goToLogin() {
      this.$router.push("/user/login");
    },
    goToTest() {
      this.$router.push("/user/test");
    },
    bookCar(id) {
      alert(`预约成功，车辆ID: ${id}`);
    },
    goToOrders() {
      this.$router.push("/user/orders");
    },
    goToAdmin() {
      this.$router.push("/user/admin");
    }
  }
};
</script>

<style scoped>
.container {
  max-width: 900px;
  margin: auto;
  text-align: center;
}

.title {
  font-size: 24px;
  margin-bottom: 20px;
}

.btn {
  padding: 10px 15px;
  margin: 5px;
  background-color: #007bff;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

.btn:hover {
  background-color: #0056b3;
}

.search-box {
  padding: 10px;
  width: 80%;
  margin-bottom: 20px;
  border: 1px solid #ccc;
  border-radius: 5px;
}

.car-list {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between;
}

.car-item {
  width: 45%;
  background: #f9f9f9;
  padding: 10px;
  border-radius: 5px;
  margin-bottom: 10px;
}

.car-image {
  width: 100%;
  border-radius: 5px;
}
</style>
