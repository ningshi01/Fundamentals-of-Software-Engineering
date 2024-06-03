<!-- sign_up -->
<template>
    <div class="container a-container" id="a-container">
        <el-form class="form" ref="form" :model="UserRegisterInfo" :rules="rules">
          <h2 class="form_title title">Create Account</h2>
          <div class="form__icons">
             <img class="form__icon" src=" ">
             <img class="form__icon" src=" ">
             <img class="form__icon" src=" ">
          </div>
          <el-form-item prop="Name">
            <el-input v-model="UserRegisterInfo.Name" type="text" placeholder="用户名"></el-input>
          </el-form-item>
          <el-form-item prop="Email">
            <el-input v-model="UserRegisterInfo.Email" type="text" placeholder="邮箱"></el-input>
          </el-form-item>
          <el-form-item prop="PassWord">
            <el-input v-model="UserRegisterInfo.PassWord" type="password" placeholder="密码"></el-input>
          </el-form-item>
          <el-form-item prop="RePassWord">
            <el-input v-model="UserRegisterInfo.RePassWord" type="password" placeholder="确认密码" ></el-input>
          </el-form-item>
          <button class="form__button button submit" type="primary" @click="submitForm">SIGN UP</button>
        </el-form>
    </div>
</template>
<script>
import axios from "axios";
import { ref } from 'vue';
import { ElMessage } from 'element-plus'
import router from "@/router"; // 导入Vue.js路由器
import { useStore } from "vuex";

export default {
  
  setup() {
    const store = useStore();
    const UserRegisterInfo = ref({
      Name: '',
      Email: '',
      PassWord: '',
      RePassWord: '',
    });

    const form = ref(null);

    const rules = {
      Name: [
        { required: true, message: '请输入用户名', trigger: 'blur' },
      ],
      Email: [
        { required: true, message: '请输入邮箱', trigger: 'blur' },
      ],
      PassWord: [
        { required: true, message: '请输入密码', trigger: 'blur' },
      ],
      RePassWord: [
        { required: true, message: '请确认密码', trigger: 'blur' },
        {
          validator: (rule, value, callback) => {
            if (value !== UserRegisterInfo.value.PassWord) {
              callback(new Error("两次输入的密码不一致"));
            } else {
              callback();
            }
          },
          trigger: "blur",
        },
      ],
    };

    const submitForm = () => {
      
      form.value.validate(async (valid) => {
        if (valid) {
            axios.post('/api/user/register/', {            
            username: UserRegisterInfo.value.Name,
            password: UserRegisterInfo.value.PassWord,
            email: UserRegisterInfo.value.Email
          }, {headers: {
              'Access-Control-Allow-Origin': '*',
              'Access-Control-Allow-Methods': 'GET, POST, PUT, DELETE, OPTIONS',
              'Access-Control-Allow-Headers': 'Origin, X-Requested-With, Content-Type, Accept'
              },}).then((response) => {
                    console.log(response.data);
                    const token = response.data.data.token;
                    store.commit("setToken", token);
                    store.commit('setLogin',true)
                    store.commit("setLogin",true)
                    router.push({ path: "/WELCOME" });
                    })
                    .catch((error) => {
                    if(error.response.status === 400){
                    ElMessage.error('用户已存在')
                    }
                    });
      }});
    };

    return { UserRegisterInfo, form, rules, submitForm};
  },
};
</script>

<style scoped>
@import '../../assets/login.css';
.el-input{
  width: 550px;
}
</style>