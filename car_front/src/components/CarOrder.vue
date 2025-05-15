<template>
  <div class="favorites-container">
    <h2>我的收藏</h2>
    <div v-if="loading">加载中...</div>
    <div v-else>
      <div v-if="cars.length === 0">暂无收藏车辆</div>
      <div class="car-list">
        <div class="car-card" v-for="car in cars" :key="car.car_id">
          <img :src="car.car_image" alt="车辆图片" class="car-image" v-if="car.car_image" />
          <div class="car-info">
            <h3>{{ car.car_model }}</h3>
            <p>品牌：{{ car.car_brand }}</p>
            <p>价格：{{ car.car_price }} 元</p>
            <button class="btn" @click="viewReserve(car.car_id)">查看预约信息</button>
            <button class="btn trade-btn" @click="showQrDialog = true">交易</button>
          </div>
        </div>
      </div>
    </div>
    <!-- 预约信息弹窗 -->
    <div v-if="showDialog" class="dialog-overlay" @click.self="closeDialog">
      <div class="dialog">
        <h3>预约信息</h3>
        <div v-if="reserveInfo">
          <p><strong>姓名：</strong>{{ reserveInfo.name }}</p>
          <p><strong>手机号：</strong>{{ reserveInfo.phone }}</p>
          <p><strong>身份证号：</strong>{{ reserveInfo.idcard }}</p>
          <p><strong>预约日期：</strong>{{ reserveInfo.date }}</p>
          <p><strong>预约地点：</strong>{{ reserveInfo.place }}</p>
        </div>
        <div v-else>暂无预约信息</div>
        <button class="btn" @click="closeDialog" style="margin-top:12px;">关闭</button>
      </div>
    </div>
    <!-- 交易二维码弹窗 -->
    <div v-if="showQrDialog" class="dialog-overlay" @click.self="closeQrDialog">
      <div class="dialog">
        <h3>交易二维码</h3>
        <img :src="qrImgUrl" alt="交易二维码" style="width:200px;height:200px;" />
        <button class="btn" @click="closeQrDialog" style="margin-top:12px;">关闭</button>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
export default {
  name: 'CarOrder',
  data() {
    return {
      cars: [],
      loading: true,
      showDialog: false,
      reserveInfo: null,
      showQrDialog: false,
      qrImgUrl: require('@/assets/123.png'),
      qrTimer: null
    };
  },
  watch: {
    async showQrDialog(val) {
      if (val) {
        // 模拟扫码，3秒后提示交易成功并关闭弹窗
        this.qrTimer = setTimeout(async () => {
          alert('交易成功');
          this.showQrDialog = false;
          try {
            // 需要 carId，这里假设用第一个收藏车辆的 car_id
            const carId = this.cars.length > 0 ? this.cars[0].car_id : null;
            const userId = localStorage.getItem("account");
            if (carId && userId) {
              const response = await axios.delete(`http://localhost:8000/user/remove_favorite/`, {
                data: { car_id: carId, user_id: userId }
              });
              alert(response.data.message);
              this.cars = this.cars.filter(car => car.car_id !== carId); // 更新前端列表
            }
          } catch (error) {
            console.error('取消收藏失败：', error);
            alert('取消收藏失败，请稍后重试！');
          }
        }, 3000);
      } else {
        // 关闭弹窗时清除定时器
        if (this.qrTimer) {
          clearTimeout(this.qrTimer);
          this.qrTimer = null;
        }
      }
    }
  },
  mounted() {
    const userId = localStorage.getItem("account");
    axios.get('http://localhost:8000/user/profile/', {
      params: { id: userId }
    })
    .then(res => {
      this.cars = res.data.favorite_cars || [];
      this.loading = false;
    })
    .catch(() => {
      this.loading = false;
    });
  },
  methods: {
    async viewReserve(carId) {
      const userId = localStorage.getItem("account");
      try {
        const res = await axios.get("http://localhost:8000/user/reserveinfo/", {
          params: { userId: userId, carId: carId }
        });
        this.reserveInfo = res.data.reserve_info || null;
        this.showDialog = true;
      } catch (e) {
        this.reserveInfo = null;
        this.showDialog = true;
      }
    },
    closeDialog() {
      this.showDialog = false;
      this.reserveInfo = null;
    },
    closeQrDialog() {
      this.showQrDialog = false;
    }
  }
};
</script>

<style scoped>
.favorites-container {
  padding: 24px;
}
.car-list {
  display: flex;
  flex-wrap: wrap;
  gap: 16px;
}
.car-card {
  border: 1px solid #eee;
  border-radius: 8px;
  width: 260px;
  padding: 16px;
  background: #fff;
  box-shadow: 0 2px 8px rgba(0,0,0,0.05);
}
.car-image {
  width: 100%;
  height: 140px;
  object-fit: cover;
  border-radius: 4px;
}
.car-info {
  margin-top: 12px;
}
.dialog-overlay {
  position: fixed;
  top: 0; left: 0; right: 0; bottom: 0;
  background: rgba(0,0,0,0.18);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 1000;
}
.dialog {
  background: #fff;
  padding: 24px 32px;
  border-radius: 10px;
  min-width: 280px;
  box-shadow: 0 4px 24px rgba(0,0,0,0.18);
  position: relative;
}
</style>