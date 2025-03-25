<!-- filepath: /Users/apple/code/Car/car_front/src/components/CarManagement.vue -->
<template>
    <div class="car-management-container">
      <h1 class="title">车辆管理</h1>
  
      <!-- 添加车辆 -->
      <div class="add-car-section">
        <h2>添加新车辆</h2>
        <form @submit.prevent="addCar">
          <input v-model="newCar.brand" placeholder="品牌" required />
          <input v-model="newCar.model" placeholder="型号" required />
          <input v-model.number="newCar.price" placeholder="价格 (万元)" type="number" required />
          <input v-model.number="newCar.age" placeholder="车龄 (年)" type="number" required />
          <input type="file" @change="handleFileUpload" placeholder="图片" required />
          <button type="submit" class="btn">添加车辆</button>
        </form>
      </div>
  
      <!-- 车辆列表 -->
      <div class="car-list-section">
        <h2>车辆列表</h2>
        <div v-if="cars.length" class="car-list">
          <div v-for="car in cars" :key="car.id" class="car-item">
            <img :src="getImageUrl(car.image)" class="car-image" />
            <div class="car-details">
              <h3>{{ car.brand }} - {{ car.model }}</h3>
              <p>价格: {{ car.price }} 万元</p>
              <p>车龄: {{ car.age }} 年</p>
              <button class="btn delete-button" @click="deleteCar(car.id)">删除</button>
            </div>
          </div>
        </div>
        <p v-else>暂无车辆信息。</p>
      </div>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  export default {
    data() {
      return {
        cars: [],
        newCar: {
          brand: "",
          model: "",
          price: null,
          age: null,
          image: null
        }
      };
    },
    methods: {
      getImageUrl(imagePath) {
        if (!imagePath) {
          return ""; // 如果没有图片路径，返回空字符串
        }
        return `http://127.0.0.1:8000${imagePath}`;
        },
      handleFileUpload(event) {
        this.newCar.image = event.target.files[0]; // 获取文件对象
      },
      async fetchCars() {
        try {
          const response = await axios.get("http://127.0.0.1:8000/car/info/");
          this.cars = response.data;
        } catch (error) {
          console.error("获取车辆信息失败:", error);
        }
      },
      async addCar() {
        if (this.newCar.brand && this.newCar.model && this.newCar.price && this.newCar.age && this.newCar.image) {
          try {
            // 构建请求数据
            const formData = new FormData();
            formData.append("brand", this.newCar.brand);
            formData.append("model", this.newCar.model);
            formData.append("price", this.newCar.price);
            formData.append("age", this.newCar.age);
            formData.append("image", this.newCar.image); // 假设 image 是文件对象

            // 发送 POST 请求
            const response = await axios.post("http://127.0.0.1:8000/car/info/", formData, {
              headers: {
                "Content-Type": "multipart/form-data"
              }
            });
            // 更新车辆列表
            this.cars.push(response.data);
            // 重置表单
            this.newCar = { brand: "", model: "", price: null, age: null, image: null };
            alert("车辆添加成功！");
          } catch (error) {
            console.error("添加车辆失败:", error);
            alert("添加车辆失败，请稍后重试！");
          }
        } else {
          alert("请填写完整的车辆信息！");
        }
      },
      async deleteCar(id) {
        try {
          // 发送 DELETE 请求到后端
          await axios.delete(`http://127.0.0.1:8000/car/info/${id}/`);
          // 从本地车辆列表中移除已删除的车辆
          this.cars = this.cars.filter(car => car.id !== id);
          alert("车辆已删除！");
        } catch (error) {
          console.error("删除车辆失败:", error);
          alert("删除车辆失败，请稍后重试！");
        }
  }
    },
    mounted() {
      this.fetchCars()
    }  
};
  </script>
  
  <style scoped>
  .car-management-container {
    max-width: 900px;
    margin: auto;
    text-align: center;
  }
  
  .title {
    font-size: 24px;
    margin-bottom: 20px;
  }
  
  .add-car-section form {
    display: flex;
    flex-direction: column;
    gap: 10px;
    margin-bottom: 20px;
  }
  
  .add-car-section input {
    padding: 10px;
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
  
  .delete-button {
    background-color: #dc3545;
  }
  
  .delete-button:hover {
    background-color: #a71d2a;
  }
  </style>