<template>
  <div class="reserve-container">
    <h2>车辆预约</h2>
    <form class="reserve-form" @submit.prevent="submitReserve">
      <label>
        姓名：
        <input v-model="form.name" required />
      </label>
      <label>
        手机号：
        <input v-model="form.phone" required pattern="^1[3-9]\d{9}$" />
      </label>
      <label>
        身份证号：
        <input v-model="form.idcard" required maxlength="18" />
      </label>
      <label>
        预约日期：
        <input v-model="form.date" type="date" required />
      </label>
      <label>
        预约地点：
        <input v-model="form.place" required />
      </label>
      <button class="btn" type="submit">提交预约</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios';
export default {
  name: 'ReservePage',
  data() {
    return {
      form: {
        name: '',
        phone: '',
        idcard: '',
        date: '',
        place: ''
      }
    };
  },
    methods: {
    async submitReserve() {
        if (!this.form.name || !this.form.phone || !this.form.idcard || !this.form.date || !this.form.place) {
            alert('请填写完整信息');
        return;
        }
        try {
        const userId = localStorage.getItem('account');
        const carId = this.$route.query.car_id;
        if (!carId) {
            alert('未获取到车辆ID，无法预约！');
            return;
        }
        const res = await axios.post('http://localhost:8000/user/reserve/', {
            user_id: userId,
            car_id: carId,
            name: this.form.name,
            phone: this.form.phone,
            idcard: this.form.idcard,
            date: this.form.date,
            place: this.form.place
        });
        alert(res.data.message); // 只显示 message
        this.$router.push('/');  // 自动跳转回主页
        } catch (e) {
        alert('预约失败，请稍后重试！' + e);
        }
    }
    }
};
</script>

<style scoped>
.reserve-container {
  max-width: 400px;
  margin: 40px auto;
  background: #fff;
  border-radius: 8px;
  box-shadow: 0 2px 12px rgba(0,0,0,0.08);
  padding: 24px;
}
.reserve-form {
  display: flex;
  flex-direction: column;
  gap: 16px;
}
.reserve-form label {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  font-size: 15px;
}
.reserve-form input {
  margin-top: 4px;
  padding: 6px 10px;
  border-radius: 4px;
  border: 1px solid #ccc;
  width: 250px;
}
.btn {
  padding: 8px 18px;
  background: #007bff;
  color: #fff;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}
.btn:hover {
  background: #0056b3;
}
</style>