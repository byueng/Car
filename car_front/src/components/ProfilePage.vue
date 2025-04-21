<template>
  <div class="profile-container">
    <h1 class="profile-title">用户信息</h1>

    <!-- 个人信息显示区域 -->
    <div class="profile-info" v-if="!isEditing">
      <p><strong>用户名:</strong> {{ user.account }}</p>
      <p><strong>邮箱:</strong> {{ user.email }}</p>
      <p><strong>电话:</strong> {{ user.phone }}</p>
      <p><strong>生日日期:</strong> {{ user.birthdate }}</p>
      <button class="edit-button" @click="toggleEditing">Edit</button>
    </div>

    <!-- 编辑表单 -->
    <div class="profile-form" v-else>
      <div class="form-group">
        <label for="email">邮箱:</label>
        <input id="email" v-model="user.email" type="email" />
      </div>
      <div class="form-group">
        <label for="phone">电话:</label>
        <input id="phone" v-model="user.phone" type="text" />
      </div>
      <div class="form-group">
        <label for="birthdate">生日日期:</label>
        <input id="birthdate" v-model="user.birthdate" type="date" />
      </div>
      <button class="submit-button" @click="updateProfile">Save</button>
      <button class="cancel-button" @click="toggleEditing">Cancel</button>
    </div>
  </div>
  <!-- 收藏车辆显示区域 -->
  <div class="favorite-cars">
    <h2>收藏的车辆</h2>
    <ul>
      <li v-for="car in paginatedCars" :key="car.car_id" class="favorite-car-item">
        <img :src="car.car_image" alt="车辆图片" class="car-image" v-if="car.car_image" />
        <p><strong>品牌:</strong> {{ car.car_brand }}</p>
        <p><strong>型号:</strong> {{ car.car_model }}</p>
        <p><strong>价格:</strong> {{ car.car_price }}</p>
        <button class="remove-button" @click="removeFavorite(car.car_id)">取消收藏</button>
      </li>
    </ul>
    <!-- 分页控件 -->
    <div class="pagination">
      <button :disabled="currentPage === 1" @click="currentPage--">上一页</button>
      <span>第 {{ currentPage }} 页 / 共 {{ totalPages }} 页</span>
      <button :disabled="currentPage === totalPages" @click="currentPage++">下一页</button>
    </div>
  </div>
</template>
  
<script>
import axios from 'axios';
export default {
  data() {
    return {
      isEditing: false,  // 是否处于编辑模式
      user: {
        account: '',
        email: '',
        phone: '',
        birthdate: ''
      },
      favoriteCars: [], // 所有收藏车辆
      currentPage: 1,   // 当前页码
      itemsPerPage: 8   // 每页显示的车辆数量
    };
  },
  computed: {
    // 计算当前页的车辆
    paginatedCars() {
      const start = (this.currentPage - 1) * this.itemsPerPage;
      const end = start + this.itemsPerPage;
      return this.favoriteCars.slice(start, end);
    },
    // 计算总页数
    totalPages() {
      return Math.ceil(this.favoriteCars.length / this.itemsPerPage);
    }
  },
  methods: {
    async GetProfile(userId) {
      try {
        const response = await axios.get(`http://localhost:8000/user/profile/`, {
          params: { id: userId } // 将用户 ID 作为查询参数传递给后端
        });
        this.user = response.data.user;
        this.favoriteCars = response.data.favorite_cars;
      } catch (error) {
        console.error('获取用户信息失败：', error);
      }
    },
    toggleEditing() {
      this.isEditing = !this.isEditing; // 切换编辑模式
    },
    async updateProfile() {
      try {
        const response = await axios.put(`http://localhost:8000/user/profile/`, {
          account: this.user.account,
          email: this.user.email,
          phone: this.user.phone,
          birthdate: this.user.birthdate
        });
        this.user = response.data; // 更新用户信息
        this.isEditing = false; // 退出编辑模式
        alert('用户信息更新成功');
        window.location.reload(); // 刷新页面
      } catch (error) {
        console.error('更新用户信息失败：', error);
        alert('更新失败，请重试');
      }
    },
    async removeFavorite(carId) {
      try {
        const response = await axios.delete(`http://localhost:8000/user/remove_favorite/`, {
          data: { car_id: carId, user_id: this.user.account }
        });
        alert(response.data.message);
        this.favoriteCars = this.favoriteCars.filter(car => car.car_id !== carId); // 更新前端列表
        // 如果当前页没有车辆了，自动跳转到上一页
        if (this.paginatedCars.length === 0 && this.currentPage > 1) {
          this.currentPage--;
        }
      } catch (error) {
        console.error('取消收藏失败：', error);
        alert('取消收藏失败，请稍后重试！');
      }
    }
  },
  beforeRouteEnter(to, from, next) {
    next(vm => {
      const userId = to.query.id; // 从路由查询参数中获取用户 ID
      if (userId) {
        vm.GetProfile(userId);
      } else {
        console.error('用户 ID 未提供');
      }
    });
  }
};
</script>
  
<style scoped>

.car-image {
  width: 150px; /* 限制图片宽度 */
  height: auto; /* 保持图片比例 */
  margin-bottom: 10px;
  border-radius: 8px;
  box-shadow: 0 0 5px rgba(0, 0, 0, 0.1);
}

.favorite-car-item {
  margin-bottom: 20px;
  padding: 15px;
  border: 1px solid #ccc;
  border-radius: 8px;
  background-color: #f9f9f9;
}

.pagination {
  display: flex;
  justify-content: center;
  align-items: center;
  margin-top: 20px;
}

.pagination button {
  background-color: #007BFF;
  color: white;
  border: none;
  padding: 8px 15px;
  margin: 0 5px;
  cursor: pointer;
  border-radius: 5px;
}

.pagination button:disabled {
  background-color: #ccc;
  cursor: not-allowed;
}

.pagination span {
  font-size: 1rem;
  margin: 0 10px;
}

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
  