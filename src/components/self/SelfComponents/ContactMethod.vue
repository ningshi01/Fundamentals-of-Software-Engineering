<template>
  <div class="center-form-item">
    <div class="center-tit">
      <div class="tit-name">基本信息</div>
      <div class="pull-right">
        <a href="javascript:;" class="btn-edit" id="relation_way_edit" title="编辑联系方式" aria-label="编辑联系方式" @click="edit"
          v-show="!person.isedit">编辑</a>
        <a href="javascript:;" class="btn-edit" id="relation_way_edit" title="提交联系方式" aria-label="提交联系方式" @click="subedit"
          v-show="person.isedit">提交</a>
        <a href="javascript:;" class="btn-edit" id="relation_way_edit" @click="exitedit" v-show="person.isedit">取消</a>
      </div>
    </div>
    <!-- 显示 -->
    <div class="form-list form-list-view" id="relation_way_view">
      <div class="form-item">
        <div class="form-label"><span class="required">*</span>用户名：</div>
        <div class="form-bd">
          <div class="form-bd-txt" v-show="!person.isedit">{{ person.username }}</div>
          <input type="text" v-model="person.username" maxlength="30" v-show="person.isedit">
        </div>
      </div>

      <div class="form-item" style="position:relative">
        <div class="form-label">邮箱：</div>
        <div class="form-bd" title="">
          <div class="form-bd-txt" v-show="!person.isedit">{{ person.email }}</div>
          <div class="input-box"><input type="text" class="input" v-model="person.email" v-show="person.isedit"></div>
        </div>
      </div>
      <div class="form-item">
        <div class="form-label"><span class="required">*</span>余额：</div>
        <div class="form-bd">
          <div class="form-bd-txt">{{ person.balance }}</div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import {  ElMessageBox,ElMessage} from 'element-plus'
import axios from 'axios'
import { mapState } from "vuex";
import router from '@/router';
export default {
  computed: {
    ...mapState(["token"]),
    ...mapState(["isLogin"]),
  },
  name: 'ContactMethod',
  data() {
    return {
      person: {
        username: '',
        email: '',
        balance: 0,
        isedit: false,

      },
      temp: {
        username: '',
        email: '',
        balance: 0,
        isedit: false
      }
    }
  },
  methods: {
    edit() {
      this.temp = { ...this.person }
      this.person.isedit = true;
    },
    subedit() {
      const emailRegex = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
      if (this.person.email != '' && !emailRegex.test(this.person.email)) {
        ElMessageBox.alert('邮箱格式有误', '修改失败', {
          confirmButtonText: '确定',
          showClose:false
        })
      }  else {
        this.person.isedit = false;

        axios.post('/api/user/update_user_info/', {
          username: this.person.username,
          email: this.person.email,
          user_id:4
        }, {
             headers:{
                   "Authorization":this.token
                     }
                })
          // eslint-disable-next-line no-unused-vars
          .then((response) => {
            ElMessageBox.alert('您已成功修改联系方式信息', '修改成功', {
              confirmButtonText: '确定',
              showClose:false
            })
          })
          
          // eslint-disable-next-line no-unused-vars
          .catch((error) => {
            if(error.response.status==401 || this.isLogin==false)
                {
                    router.push({ path: "/Login" });
                    ElMessage({
                    showClose: true,
                    message: '登录失效,请重新登录',
                    type: 'error',
                })
                }
            this.person.isedit = true;
            ElMessageBox.alert('用户名已被注册', '修改失败', {
              confirmButtonText: '确定',
              showClose:false
            })
          });



      }
    },
    exitedit() {
      this.person = { ...this.temp }
      this.person.isedit = false;
    }
  },
  mounted() {
    axios.post('/api/user/get_user_info/', {
      user_id: "4",
    },  {
             headers:{
                   "Authorization":this.token
                     }
                })
      .then((response) => {
        //console.log(response.data);
        let data = response.data;
        this.person.username = data.username;
        this.person.email = data.email;
        this.person.balance = data.balance;
      })
      .catch((error) => {
                console.log(error);
                if(error.response.status==401 || this.isLogin==false)
                {
                    router.push({ path: "/Login" });
                    ElMessage({
                    showClose: true,
                    message: '登录失效,请重新登录',
                    type: 'error',
                })
                }
            });
  }
}
</script>

<style scoped>
* {
  margin: 0;
  padding: 0;
}

.form-item {
  margin-bottom: 10px;
}


.center-tit {
  height: 30px;
  margin-bottom: 10px;
}


.center-tit .tit-name {
  float: left;
  font-weight: 700;
  line-height: 30px;
}

.pull-right {
  float: right !important;
}

.form-label {
  -webkit-text-size-adjust: 100%;
  font-family: "Helvetica Neue", Helvetica, Arial, "PingFang SC", "Hiragino Sans GB", "Heiti SC", "Microsoft YaHei", "WenQuanYi Micro Hei", sans-serif;
  font-size: 14px;
  box-sizing: border-box;
  margin: 0;
  float: left;
  padding: 5px 5px 5px 0;
  line-height: 20px;
  font-weight: 400;
  color: #666;
  text-align: right;
  width: 360px;
}

.required {
  color: #f00;
  font-weight: 400;
}

.center-form-item .form-bd {
  min-height: 30px;
}

.form-list .form-bd-txt {
  line-height: 20px;
  padding-top: 5px;
  padding-bottom: 5px;
  min-height: 20px;
}

.btn-edit {
  -webkit-text-size-adjust: 100%;
  font-family: "Helvetica Neue", Helvetica, Arial, "PingFang SC", "Hiragino Sans GB", "Heiti SC", "Microsoft YaHei", "WenQuanYi Micro Hei", sans-serif;
  box-sizing: border-box;
  text-decoration: none;
  display: inline-block;
  font-size: 14px;
  color: #333;
  min-width: 80px;
  height: 30px;
  line-height: 20px;
  padding: 4px 10px;
  border: 1px solid #dedede;
  border-radius: 6px;
  background-color: #fff;
  text-align: center;
  white-space: nowrap;
  vertical-align: middle;
  cursor: pointer;
  user-select: none;
  outline: none;
  position: relative;
  font-weight: bold;
  transition: border-color ease-in-out 0.15s, box-shadow ease-in-out 0.15s, color ease-in-out 0.15s, background ease-in-out 0.15s, -webkit-box-shadow ease-in-out 0.15s;
}
</style>