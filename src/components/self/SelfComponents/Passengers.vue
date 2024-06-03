<template>
  <div class="table">
    乘车人
    <a href="javascript:;" class="btn btn-edit" id="append_info_edit" @click="edit" v-show="!isedit">编辑</a>
    <a href="javascript:;" class="btn btn-edit" id="append_info_edit" @click="dialog = true" v-show="!isedit">新增</a>
    <a href="javascript:;" class="btn btn-edit" id="append_info_edit" @click="commitedit" v-show="isedit">提交</a>
    <a href="javascript:;" class="btn-edit" id="relation_way_edit" @click="exitedit" v-show="isedit">取消</a>
  </div>
  <div v-for="pas in passengers" :key="pas" class="main">
    <el-descriptions :column="3" border>
      <el-descriptions-item label="姓名" label-align="right" align="center" label-class-name="my-label"
        class-name="my-content" width="150px">
        <div>{{ pas.name }}</div>
      </el-descriptions-item>


      <el-descriptions-item label="手机号码" label-align="right" align="center">
        <div v-show="!isedit"> {{ '+' + pas.phone_region + ' ' +
          pas.phone_number
        }}</div>
        <input type="text" v-model="pas.phone_number" maxlength="20" style="width: 120px;text-align: center;"
          v-show="isedit">
      </el-descriptions-item>


      <el-descriptions-item label="优惠类型" label-align="right" align="center">
        <div v-show="!isedit"><el-tag size="large">
            {{ pas.ticket_type
            }}</el-tag></div>
        <el-select v-model="pas.ticket_type" class="m-2" placeholder="Select" v-show="isedit">
          <el-option v-for="item in options1" :key="item.value" :label="item.label" :value="item.value" />
        </el-select>
      </el-descriptions-item>


      <el-descriptions-item label="证件类型" label-align="right" align="center">
        <div>{{ pas.id_type }}</div>
        <!-- <el-select v-model="pas.id_type" class="m-2" placeholder="Select" v-show="isedit">
          <el-option v-for="item in options2" :key="item.value" :label="item.label" :value="item.value" />
        </el-select> -->
      </el-descriptions-item>


      <el-descriptions-item label="证件号码" label-align="right" align="center">
        <div>{{ pas.id_number
        }}
          <a href="javascript:;" class="delete_btn btn-edit" id="append_info_edit" @click="delete2(pas.id)"
            v-show="isedit">删除</a>
        </div>
        <!-- <input type="text" v-model="pas.id_number" maxlength="20" style="width: 200px;text-align: center;"
          v-show="isedit"> -->

      </el-descriptions-item>


    </el-descriptions>
  </div>

  <!-- 新增乘车人抽屉 -->
  <el-drawer ref="drawerRef" v-model="dialog" title="新增乘车人" :before-close="handleClose" direction="rtl"
    class="demo-drawer" size="40%">
    <div class="demo-drawer__content">
      <el-form :model="new_passenger">
        <el-form-item label="姓名" :label-width="formLabelWidth">
          <el-input v-model="new_passenger.name" autocomplete="off" placeholder="请填写姓名" />
        </el-form-item>
        <el-form-item label="证件类型" :label-width="formLabelWidth">
          <el-select v-model="new_passenger.id_type" placeholder="请选择证件类型">
            <el-option label="中国居民身份证" value="CIC" />
            <el-option label="港澳居民来往内地通行证" value="HTP" />
            <el-option label="台湾居民来往大陆通行证" value="TTP" />
            <el-option label="护照" value="PSP" />
            <el-option label="外国人永久居留身份证" value="FRI" />
            <el-option label="港澳台居民居住证" value="HMT" />
          </el-select>
        </el-form-item>
        <el-form-item label="证件号" :label-width="formLabelWidth">
          <el-input v-model="new_passenger.id_number" autocomplete="off" placeholder="请填写证件号" />
        </el-form-item>
        <el-form-item label="手机号" :label-width="formLabelWidth">
          <el-input v-model="new_passenger.phone_number" autocomplete="off" placeholder="请填写手机号" />
        </el-form-item>
        <el-form-item label="地区" :label-width="formLabelWidth">
          <el-select v-model="new_passenger.phone_region" placeholder="请选择您所在的地区号">
            <el-option label="中国" value="86" />
            <el-option label="美国" value="1" />
            <el-option label="日本" value="81" />
            <el-option label="韩国" value="82" />
            <el-option label="英国" value="44" />
            <el-option label="法国" value="33" />
            <el-option label="德国" value="94" />
            <el-option label="俄罗斯" value="1" />
            <el-option label="越南" value="84" />
            <el-option label="印度" value="7" />
          </el-select>
        </el-form-item>
        <el-form-item label="优惠类型" :label-width="formLabelWidth">
          <el-select v-model="new_passenger.ticket_type" placeholder="请选择您的优惠类型">
            <el-option label="成人" value="ADU" />
            <el-option label="儿童" value="CHI" />
            <el-option label="学生" value="STU" />
            <el-option label="残疾军人" value="DOM" />
          </el-select>
        </el-form-item>
      </el-form>
      <div class="demo-drawer__footer">
        <el-button @click="cancelForm">取消</el-button>
        <el-button type="primary" :loading="loading" @click="submit">{{
          loading ? '提交中 ...' : '提交'
        }}</el-button>
      </div>
    </div>
  </el-drawer>
</template>

<script>

import axios from 'axios';
import {  ElMessageBox,ElMessage} from 'element-plus'
import { mapState } from "vuex";
import router from '@/router';
export default {
  computed: {
    ...mapState(["token"]),
    ...mapState(["isLogin"]),
  },
  // eslint-disable-next-line vue/multi-word-component-names
  name: 'Passengers',
  data() {
    return {
      passengers: [],
      temp_pas: [],
      pas_str: '',
      temp_str: '',
      isedit: false,
      dialog: false,
      loading: false,
      formLabelWidth: '80px',
      new_passenger: {
        id_type: '',
        name: '',
        id_number: '',
        ticket_type: '',
        phone_region: '',
        phone_number: ''
      },
      empty_passenger: {
        id_type: '',
        name: '',
        id_number: '',
        ticket_type: '',
        phone_region: '',
        phone_number: ''
      },
      options1: [
        {
          value: '成人',
          label: '成人',
        },
        {
          value: '儿童',
          label: '儿童',
        },
        {
          value: '学生',
          label: '学生',
        },
        {
          value: '残疾军人',
          label: '残疾军人',
        }
      ],
      options2: [
        {
          value: '中国居民身份证',
          label: '中国居民身份证',
        },
        {
          value: '港澳居民来往内地通行证',
          label: '港澳居民来往内地通行证',
        },
        {
          value: '台湾居民来往大陆通行证',
          label: '台湾居民来往大陆通行证',
        },
        {
          value: '护照',
          label: '护照',
        },
        {
          value: '外国人永久居留身份证',
          label: '外国人永久居留身份证',
        },
        {
          value: '港澳台居民居住证',
          label: '港澳台居民居住证',
        }
      ]
    }
  },
  methods: {
    edit() {
      this.isedit = !this.isedit
      this.temp_pas = [...this.passengers];
      this.temp_str = JSON.stringify(this.passengers);
      /*console.log(JSON.stringify(this.passengers))
      console.log(JSON.stringify(this.temp_pas))*/
    },
    commitedit() {
      let flag = 0;
      this.temp_pas = JSON.parse(this.temp_str);
      for (let i = 0; i < this.passengers.length; i++) {
        if (JSON.stringify(this.temp_pas[i]) !== JSON.stringify(this.passengers[i])) {
          if (!this.isValidPhoneNumber(this.passengers[i].phone_number)) {
            ElMessageBox.alert('乘车人' + this.passengers[i].name + '的电话号格式有误', '更新失败', {
              confirmButtonText: '确定',
              showClose:false
            });
            this.update();
            break;
          }
          if (this.passengers[i].ticket_type === '残疾军人') {
            this.passengers[i].ticket_type = 'DOM'
          }
          else if (this.passengers[i].ticket_type === '儿童') {
            this.passengers[i].ticket_type = 'CHI'
          }
          else if (this.passengers[i].ticket_type === '学生') {
            this.passengers[i].ticket_type = 'STU'
          }
          else if (this.passengers[i].ticket_type === '成人') {
            this.passengers[i].ticket_type = 'ADU'
          }
          axios.post('/api/user/update_passenger/', {
            passenger_id: this.passengers[i].id,
            ticket_type: this.passengers[i].ticket_type,
            phone_number: this.passengers[i].phone_number,
          },{
             headers:{
                   "Authorization":this.token
                     }
                })
            .then((response) => {
              console.log(response);
              flag++;
              if (flag === 1)
                ElMessageBox.alert('已更新乘车人', '更新成功', {
                  confirmButtonText: '确定',
                  showClose:false
                });
              this.update();
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
      this.isedit = !this.isedit
    },
    exitedit() {
      this.update();
      this.isedit = false;
    },
    delete2(id) {
      axios.post('/api/user/remove_passenger/', {
        user_id: "4",
        passenger_id: id
      },{
             headers:{
                   "Authorization":this.token
                     }
                })
        .then((response) => {
          console.log(response);
          ElMessageBox.alert('已删除乘车人', '删除成功', {
            confirmButtonText: '确定',
            showClose:false
          });
          this.update();
        })
        .catch((error) => {
          console.log(error);
        });
    },
    async update() {
      axios.post('/api/user/get_user_info/', {
        user_id: "4",
      },{
             headers:{
                   "Authorization":this.token
                     }
                })
        .then((response) => {
          this.passengers = response.data.passengers;
          for (let i = 0; i < this.passengers.length; i++) {
            //判断优惠类型
            if (this.passengers[i].ticket_type === 'CHI') {
              this.passengers[i].ticket_type = '儿童'
            }
            else if (this.passengers[i].ticket_type === 'STU') {
              this.passengers[i].ticket_type = '学生'
            }
            else if (this.passengers[i].ticket_type === 'ADU') {
              this.passengers[i].ticket_type = '成人'
            }
            else if (this.passengers[i].ticket_type === 'DOM') {
              this.passengers[i].ticket_type = '残军'
            }
            //判断证件类型
            if (this.passengers[i].id_type === 'CIC') {
              this.passengers[i].id_type = '中国居民身份证'
            }
            else if (this.passengers[i].id_type === 'HTP') {
              this.passengers[i].id_type = '港澳居民来往内地通行证'
            }
            else if (this.passengers[i].id_type === 'TTP') {
              this.passengers[i].id_type = '台湾居民来往大陆通行证'
            }
            else if (this.passengers[i].id_type === 'PSP') {
              this.passengers[i].id_type = '护照'
            }
            else if (this.passengers[i].id_type === 'FRI') {
              this.passengers[i].id_type = '外国人永久居留身份证'
            }
            else if (this.passengers[i].id_type === 'HMT') {
              this.passengers[i].id_type = '港澳台居民居住证'
            }
          }
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
    },
    isValidPhoneNumber(phoneNumber) {
      var regExp = /^1\d{10}$/;
      return regExp.test(phoneNumber);
    },
    submit() {
      //console.log(this.new_passenger)
      let flag=0;
      if (this.new_passenger.name === '') {
        ElMessageBox.alert('姓名不能为空', '添加失败', {
          confirmButtonText: '确定',
          showClose:false
        });
        flag=1;
      }else if (this.new_passenger.id_type === '') {
        ElMessageBox.alert('请选择证件类型', '添加失败', {
          confirmButtonText: '确定',
          showClose:false
        });
        flag=1;
      }else if (this.new_passenger.id_number === '') {
        ElMessageBox.alert('证件号不能为空', '添加失败', {
          confirmButtonText: '确定',
          showClose:false
        });
        flag=1;
      }else if (this.new_passenger.phone_number === '') {
        ElMessageBox.alert('手机号不能为空', '添加失败', {
          confirmButtonText: '确定',
          showClose:false
        });
        flag=1;
      }else if (this.new_passenger.phone_region === '') {
        ElMessageBox.alert('请选择您的地区', '添加失败', {
          confirmButtonText: '确定',
          showClose:false
        });
        flag=1;
      }else if (this.new_passenger.ticket_type === '') {
        ElMessageBox.alert('请选择优惠类型', '添加失败', {
          confirmButtonText: '确定',
          showClose:false
        });
        flag=1;
      }else if (!this.isValidPhoneNumber(this.new_passenger.phone_number)) {
        ElMessageBox.alert('手机号格式有误', '添加失败', {
          confirmButtonText: '确定',
          showClose:false
        });
        flag=1;
      }
      if(flag===1)return;
      axios.post('/api/user/add_passenger/', {
        user_id: "4",
        id_type: this.new_passenger.id_type,
        name: this.new_passenger.name,
        id_number: this.new_passenger.id_number,
        ticket_type: this.new_passenger.ticket_type,
        phone_region: this.new_passenger.phone_region,
        phone_number: this.new_passenger.phone_number
      }, {
             headers:{
                   "Authorization":this.token
                     }
                })
        .then((response) => {
          console.log(response.data);
          ElMessageBox.alert('成功添加乘车人', '添加成功', {
            confirmButtonText: '确定',
            showClose:false
          })
          this.update();
          this.cancelForm();
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
          ElMessageBox.alert(error.response.data.message, '添加失败', {
            confirmButtonText: '确定',
            showClose:false
          })
        });
    },
    cancelForm() {
      this.dialog = false
      this.new_passenger={...this.empty_passenger}
    },
  },
  mounted() {
    this.update();
  }
}
</script>

<style scoped>
* {
  margin: 0;
  padding: 0;
}

.table {
  text-align: left;
  font-weight: bold;
}

.main {
  margin-top: 15px;
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
  float: right;
  transition: border-color ease-in-out 0.15s, box-shadow ease-in-out 0.15s, color ease-in-out 0.15s, ease-in-out 0.15s, -webkit-box-shadow ease-in-out 0.15s;
}

.delete_btn {
  background-color: lightcoral;
  color: white;
}

.my-label {
  background: var(--el-color-success-light-9);
}

.my-content {
  background: var(--el-color-danger-light-9);
}

.el-form-item {
  margin-top: 15px;
}
</style>