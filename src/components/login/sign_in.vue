<template>
  <div class="container b-container" id="b-container">
    <el-form class="form" ref="form" :model="UserLoginInfo" :rules="rules">
      <h2 class="form_title title">请输入帐号，共同开启列车旅程吧</h2>
      <div class="form__icons">
        <img class="form__icon" src=" ">
        <img class="form__icon" src=" ">
        <img class="form__icon" src=" ">
      </div>
      <el-form-item prop="Name">
        <el-input v-model="UserLoginInfo.Name" type="text" placeholder="用户名" class="input_login"></el-input>
      </el-form-item>
      <el-form-item prop="PassWord">
        <el-input v-model="UserLoginInfo.PassWord" type="password" placeholder="密码" class="input_login"></el-input>
      </el-form-item>
      <el-button class="form__button button submit" type="primary" @click="submitForm">登录</el-button>
    </el-form>
  </div>
</template>

<script>
import axios from "axios";
import { ref } from 'vue';
import router from "@/router"; // 导入Vue.js路由器
import { useStore } from "vuex";
import { ElMessageBox,ElMessage } from "element-plus";

export default {
  setup() {
    const store = useStore();
    const UserLoginInfo = ref({
      Name: '',
      PassWord: '',
    });
    const form = ref(null);

    const rules = {
      Name: [
        { required: true, message: '请输入用户名', trigger: 'blur' },
      ],
      PassWord: [
        { required: true, message: '请输入密码', trigger: 'blur' },
      ],
    };
    const check = () => {
      console.log(axios.post('/api/user/login/'))
    }
    const submitForm = () => {

      form.value.validate(async (valid) => {
        if (valid) {
          axios.post('/api/user/login/', {
            username: UserLoginInfo.value.Name,
            password: UserLoginInfo.value.PassWord,
          }).then((response) => {
            console.log(response);
            const token = response.data.data.token;
            console.log(token)
            store.commit("setToken", token);
            store.commit("setLogin", true);
            store.commit("setUserID", response.data.data.user_id);
            ElMessage({
                    showClose: true,
                    message: '登陆成功！',
                    type: 'success',
                })
            if (response.data.data.user_type === 'user') {
              router.push({ path: "/WELCOME" });
            }
            else if (response.data.data.user_type === 'system_admin') {
              router.push({ path: '/mesdeal1' });
            }
            else if (response.data.data.user_type === 'railway_admin') {
              router.push({ path: '/trainAdjust1' });
            }
          })
            .catch((error) => {
              console.log(error);
              if (error.response.status === 404) {
                ElMessageBox.alert('用户不存在', '登录失败', {
                  confirmButtonText: '确定',
                  showClose: false
                });
              }
              else if (error.response.status == 400) {
                ElMessageBox.alert('用户名或密码错误', '登录失败', {
                  confirmButtonText: '确定',
                  showClose: false
                });
              }
            });
        }
      });


    };



    return { UserLoginInfo, form, rules, submitForm, check };
  },
};
</script>

<style scoped>
@import '../../assets/login.css';

.input_login{
    width: 250px;
}</style>