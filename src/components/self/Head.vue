<!-- eslint-disable vue/multi-word-component-names -->

<template #headPicture>
    <div class="demo-type">
      <div>
        <el-avatar> {{userName.substring(0,3)}} </el-avatar>
      </div>
    </div>
</template>
  
<script>
import axios from 'axios';
import { mapState } from "vuex";
import { ElMessage } from 'element-plus';
    export default {
      computed: {
    ...mapState(["token"]),
    ...mapState(["isLogin"]),
  },
        data(){
            return{
                userName:'aaaa'//此处应为用户名
            } 
        },
        mounted() {
    axios.post('/api/user/get_user_info/', {
      user_id: "4",
    }, {
             headers:{
                   "Authorization":this.token
                     }
                })
      .then((response) => {
        //console.log(response.data);
        let data = response.data;
        this.userName=data.username;
      })
      .catch((error) => {
        console.log(error);
        ElMessage({
                    showClose: true,
                    message: '登录失效,请重新登录',
                    type: 'error',
                })
      });
  }
   }
</script>
  
  <style scoped>
  .demo-type {
    display: flex;
  
  }
  .demo-type > div {
    flex: 1;
    text-align: center;
  }
  
 
  </style>
  