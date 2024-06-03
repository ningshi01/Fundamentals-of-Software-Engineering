<template>
    <div class="container">
        <div class="blur-background"></div>
        <fornav msg1=信息管理 msg2=主页 msg3=个人信息 msg4=信息查询 msg5=设置
        href1=#/mesdeal1 href2=#/mesdeal2 href3=#/mesdeal3 href4=#/mesdeal4 href5=#/ ></fornav>
        <h1>设置</h1>
        <hr>
        <div class="table1">
            <el-button type="primary" plain size="large" @click="returnLast">返回上级</el-button>
        </div>
        <div class="table1">
            <el-button type="warning" plain size="large" @click="switchAccount">切换账号</el-button>
        </div>
        <div class="table1">
            <el-popconfirm
                width="220" 
                confirm-button-text="OK"
                cancel-button-text="No, Thanks"
                :icon="InfoFilled"
                icon-color="#626AEF"
                title="您确定需要注销您的账号吗"
                @confirm="confirmForUnsub">
                <template #reference>
                    <el-button type="danger" plain size="large" @click="unsubscribe">注销账号</el-button>
                </template>
            </el-popconfirm>
        </div>
    </div>
</template>

<script>
import { ElMessage } from 'element-plus';
import fornav from './fornav.vue';
import axios from 'axios';
import { mapState } from "vuex";
import router from '@/router';


export default {
    computed: {
    ...mapState(["token"]),
    ...mapState(["isLogin"]),
  },
    name: "My_mesdeal_message",
    components: {
        fornav,
    },
    methods: {
        returnLast(){
            window.location.hash = '/'
        },
        switchAccount(){
            window.location.hash = '/Login'
        },
        unsubscribe(){
            console.log('正在尝试注销账号');
            axios.post('/api/user/logoff/',{},{
                     headers:{
                         "Authorization":this.token
                     }
                })
            .then((res)=>{
                console.log(res);
            }).catch((error) => {
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
        confirmForUnsub(){
            ElMessage({
                message:'注销成功！',
                type:'success',
            })
        },
    }
}
</script>

<style scoped>
.table1{
    padding-top: 2rem;
    text-align: center;
    display: flex;
    justify-content: center; /* 水平居中对齐 */
    align-items: center; /* 垂直居中对齐 */
}
</style>