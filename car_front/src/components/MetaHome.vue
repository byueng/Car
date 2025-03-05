<template>
    <div class="min-h-screen bg-gray-100">
      <!-- 顶部导航栏 -->
      <header class="bg-white shadow-md">
        <div class="container mx-auto flex justify-between items-center p-4">
          <h1 class="text-2xl font-bold">二手车交易平台</h1>
          <div class="flex items-center space-x-4">
            <input
              type="text"
              v-model="searchQuery"
              placeholder="搜索车辆..."
              class="border px-4 py-2 rounded"
            />
            <button class="bg-blue-500 text-white px-4 py-2 rounded">搜索</button>
            <button v-if="!isLoggedIn" @click="login" class="text-blue-500">
              登录/注册
            </button>
            <div v-else class="flex items-center space-x-2">
              <span>欢迎, {{ userName }}</span>
              <button @click="logout" class="text-red-500">退出</button>
            </div>
          </div>
        </div>
      </header>
  
      <!-- 轮播广告区 -->
      <section class="w-full bg-gray-200 py-10 flex justify-center">
        <div class="w-3/4 bg-white p-4 rounded shadow-md">
          <h2 class="text-xl font-bold mb-2">🔥 热门推荐车辆</h2>
          <div class="carousel flex space-x-4 overflow-x-auto">
            <img v-for="(car, index) in featuredCars" :key="index" :src="car.image" class="w-48 h-32 object-cover rounded" />
          </div>
        </div>
      </section>
  
      <!-- 车辆搜索筛选 -->
      <section class="container mx-auto my-6">
        <h2 class="text-xl font-bold">🔍 搜索 & 筛选</h2>
        <div class="flex space-x-4">
          <select v-model="filter.brand" class="border px-4 py-2 rounded">
            <option value="">品牌</option>
            <option v-for="brand in brands" :key="brand">{{ brand }}</option>
          </select>
          <select v-model="filter.price" class="border px-4 py-2 rounded">
            <option value="">价格</option>
            <option value="0-5">0-5万</option>
            <option value="5-10">5-10万</option>
          </select>
          <button @click="applyFilter" class="bg-blue-500 text-white px-4 py-2 rounded">筛选</button>
        </div>
      </section>
  
      <!-- 车辆展示 -->
      <section class="container mx-auto">
        <h2 class="text-xl font-bold">🚗 最新二手车</h2>
        <div class="grid grid-cols-3 gap-6">
          <div v-for="(car, index) in filteredCars" :key="index" class="bg-white p-4 rounded shadow-md">
            <img :src="car.image" class="w-full h-40 object-cover rounded" />
            <h3 class="text-lg font-bold mt-2">{{ car.brand }} - {{ car.model }}</h3>
            <p class="text-gray-700">💰 {{ car.price }} 万</p>
          </div>
        </div>
      </section>
  
      <!-- 底部信息 -->
      <footer class="bg-gray-800 text-white py-4 text-center mt-10">
        <p>© 2025 二手车交易平台. 联系方式: xxx-xxx-xxxx</p>
      </footer>
    </div>
  </template>
  
  <script setup>
  import { ref, computed } from "vue";
  
  // 用户信息
  const isLoggedIn = ref(false);
  const userName = ref("");
  
  // 搜索和筛选
  const searchQuery = ref("");
  const filter = ref({ brand: "", price: "" });
  const brands = ref(["丰田", "本田", "宝马", "奥迪", "奔驰"]);
  
  // 车辆数据（示例）
  const cars = ref([
    { brand: "丰田", model: "卡罗拉", price: 8, image: "https://via.placeholder.com/150" },
    { brand: "宝马", model: "X5", price: 35, image: "https://via.placeholder.com/150" },
    { brand: "奔驰", model: "C200", price: 25, image: "https://via.placeholder.com/150" },
  ]);
  
  // 轮播的热门推荐车辆
  const featuredCars = computed(() => cars.value.slice(0, 3));
  
  // 筛选后的车辆
  const filteredCars = computed(() => {
    return cars.value.filter((car) => {
      const matchBrand = filter.value.brand ? car.brand === filter.value.brand : true;
      const matchPrice = filter.value.price
        ? (filter.value.price === "0-5" && car.price <= 5) ||
          (filter.value.price === "5-10" && car.price > 5 && car.price <= 10)
        : true;
      return matchBrand && matchPrice;
    });
  });
  
  // 事件方法
  const applyFilter = () => {
    console.log("筛选条件", filter.value);
  };
  
  const login = () => {
    isLoggedIn.value = true;
    userName.value = "张三";
  };
  
  const logout = () => {
    isLoggedIn.value = false;
    userName.value = "";
  };
  </script>
  
  <style scoped>
  .carousel {
    overflow-x: auto;
    display: flex;
  }
  </style>
  