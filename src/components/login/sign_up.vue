<!-- sign_up -->
<template>
  <div class="container a-container" id="a-container">
    <el-form class="form" ref="form" :model="UserRegisterInfo" :rules="rules">
      <h2 class="form_title title">创建您的帐号，我们一起出发！</h2>

      <el-form-item prop="Name">
        <el-input v-model="UserRegisterInfo.Name" type="text" placeholder="用户名" class="input_login"></el-input>
      </el-form-item>
      <el-form-item prop="Email">
        <el-input v-model="UserRegisterInfo.Email" type="text" placeholder="邮箱" class="input_login"></el-input>
      </el-form-item>
      <el-form-item prop="PassWord">
        <el-input v-model="UserRegisterInfo.PassWord" type="password" placeholder="密码" class="input_login"></el-input>
      </el-form-item>
      <el-form-item prop="RePassWord">
        <el-input v-model="UserRegisterInfo.RePassWord" type="password" placeholder="确认密码" class="input_login"></el-input>
      </el-form-item>
      <button class="form__button button submit" type="primary" @click="submitForm" style="margin-top: 10px;">注册</button>
    </el-form>
  </div>
</template>
<script>
import axios from "axios";
import { ref } from 'vue';
import {  ElMessageBox } from 'element-plus'
import router from "@/router"; // 导入Vue.js路由器

export default {

  setup() {
    const UserRegisterInfo = ref({
      Name: '',
      Email: '',
      PassWord: '',
      RePassWord: '',
    });

    const form = ref(null);

    const rules = {
      Name: [
        { required: true, message: '请输入用户名，长度在3-16之间', trigger: 'blur' },
        {
          validator: (rule, value, callback) => {
            if (value.length<3||value.length>16) {
              callback(new Error("用户名长度应在3-16字符之间"));
            } else {
              callback();
            }
          },
          trigger: "blur",
        },
      ],
      Email: [
        { required: true, message: '请输入邮箱', trigger: 'blur' },
        {
          validator: (rule, value, callback) => {
            const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
            if (!emailRegex.test(value)) {
              callback(new Error("邮箱格式有误"));
            } else {
              callback();
            }
          },
          trigger: "blur",
        },
      ],
      PassWord: [
        { required: true, message: '请输入密码，长度在8-16之间', trigger: 'blur' },
        {
          validator: (rule, value, callback) => {
            if (value.length<8||value.length>16) {
              callback(new Error("密码长度应在8-16字符之间"));
            } else {
              callback();
            }
          },
          trigger: "blur",
        },
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
      if(UserRegisterInfo.value.Name===''){
        ElMessageBox.alert('用户名不能为空', '注册失败', {
                  confirmButtonText: '确定',
                  showClose: false
                });
            return;
      }else if(UserRegisterInfo.value.Email===''){
        ElMessageBox.alert('邮箱不能为空', '注册失败', {
                  confirmButtonText: '确定',
                  showClose: false
                });
            return;
      }else if(UserRegisterInfo.value.PassWord===''){
        ElMessageBox.alert('密码不能为空', '注册失败', {
                  confirmButtonText: '确定',
                  showClose: false
                });
            return;
      }else if(UserRegisterInfo.value.RePassWord===''){
        ElMessageBox.alert('密码不能为空', '注册失败', {
                  confirmButtonText: '确定',
                  showClose: false
                });
            return;
      }else if(UserRegisterInfo.value.RePassWord!==UserRegisterInfo.value.PassWord){
        ElMessageBox.alert('两次输入的密码不一致', '注册失败', {
                  confirmButtonText: '确定',
                  showClose: false
                });
            return;
      }
      else if(UserRegisterInfo.value.Name.length<3||UserRegisterInfo.value.Name.length>16){
        ElMessageBox.alert('用户名长度应在3-16字符之间', '注册失败', {
                  confirmButtonText: '确定',
                  showClose: false
                });
            return;
      }
      else if(UserRegisterInfo.value.PassWord.length<8||UserRegisterInfo.value.PassWord.length>16){
        ElMessageBox.alert('密码长度应在8-16字符之间', '注册失败', {
                  confirmButtonText: '确定',
                  showClose: false
                });
            return;
      }
      form.value.validate(async (valid) => {
        if (valid) {

          const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
          if (!emailRegex.test(UserRegisterInfo.value.Email)) {
            ElMessageBox.alert('邮箱格式有误', '注册失败', {
                  confirmButtonText: '确定',
                  showClose: false
                });
            return;
          }

          axios.post('/api/user/register/', {
            username: UserRegisterInfo.value.Name,
            password: UserRegisterInfo.value.PassWord,
            email: UserRegisterInfo.value.Email
          }).then((response) => {
            console.log(response)
                ElMessageBox.alert('用户注册成功,请返回登录', '注册成功', {
                  confirmButtonText: '确定',
                  showClose: false
                });
            UserRegisterInfo.value.Name='';
            UserRegisterInfo.value.Email='';
            UserRegisterInfo.value.PassWord='';
            UserRegisterInfo.value.RePassWord='';
            router.push({ path: "/Login" });
          })
            .catch((error) => {
              if (error.response.status === 400) {
                ElMessageBox.alert('用户名已存在', '注册失败', {
                  confirmButtonText: '确定',
                  showClose: false
                });
              }
              else
              {
                  ElMessageBox.alert('未知错误', '注册失败', {
                  confirmButtonText: '确定',
                  showClose: false
                });
              }
            });
        }
      });
    };

    return { UserRegisterInfo, form, rules, submitForm };
  },
};
</script>

<style scoped>
@import '../../assets/login.css';

.input_login{
    width: 250px;
}
</style>