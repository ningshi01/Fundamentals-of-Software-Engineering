<template>
    <div class="container">
        <div class="blur-background"></div>
        <fornav msg1=信息管理 msg2=主页 msg3=个人信息 msg4=信息查询 msg5=设置
        href1=#/mesdeal1 href2=#/mesdeal2 href3=#/mesdeal3 href4=#/mesdeal4 href5=#/ ></fornav>
        <h1>个人信息</h1>
        <hr>
        <div class="table1">
                <div class="profile-card" :class="{ flipped: isFlipped, moveToLeft: moveToRight }" @click="flipCard">
                    <div class="card-header">
                        <div :class="{ pic: true, enlarged: !isFlipped }">
                            <img src="../../assets/imgs/9.jpg" alt="">
                        </div>
                        <div v-if="isFlipped" class="name">{{ AdminName }}</div>
                        <div v-if="isFlipped" class="desc">System Administrator(Admin)</div>
                        <div v-if="isFlipped" class="sm"></div>
                    </div>
                    <div class="card-footer">
                        <div class="numbers">
                            <div class="item">
                                <span>已登录</span>状态
                            </div>
                            <div class="border"></div>
                            <div class="item">
                                <span>系统管理员</span>权限
                            </div>
                        </div>
                    </div>
                </div>
                <div class="profile-sidebar" :class="{ active: isFlipped }">
                    <div class="sidebar-content">
                      <h1>用户信息</h1>
                      <h1>姓名</h1>
                    </div>
                </div>

            
        </div>
        
        
          
    </div>
</template>

<script>
import fornav from './fornav.vue';
import { mapState } from "vuex";
const columnList = [
  { prop: "type", label: '元素类型', show: true },
  { prop: "data", label: '数据实值', show: true },
]
const tableData = [
    {
        type:"id",
        data: 8,
        show:true,
    },
    {
        type:"username",
        data: "testcase3",
        show:true,
    },
    {
        type:"password",
        data: "******",
        show:true,
    },
    {
        type:"abstractuser_ptr_id",
        data: 8,
        show:true,
    },
]
export default {
    computed: {
    ...mapState(["token"]),
    ...mapState(["isLogin"]),
  },
    name: "My_mesdeal_message",
    data(){
        return{
            AdminName:'MewTrain Admin',
            isFlipped: false,
            moveToRight: false,
            tableData,
            columnList,
            isFirstFlip: true,
        }
    },
    methods:{
        flipCard() {
                if (this.isFirstFlip) {
                    this.isFirstFlip = false;
                    this.isFlipped = true;
                } else {
                    this.isFirstFlip = true;
                    this.isFlipped   = false;
                    this.moveToRight = true;
                    this.moveToRight = false;
                }
        },
    },
    components: {
        fornav,
    }
}
</script>

<style scoped>
@import '../../assets/css/forMessage.css';
@import 'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.14.0/css/all.min.css';
.table1{
    padding: 0 0rem 0 25rem;
    text-align: center;
    display: flex;
    align-items: stretch;
}
  
.profile-sidebar {
    position: absolute;
    top: 10%;
    right: 0;
    bottom: 10%;
    width: 60%;
    background-color: rgba(0, 0, 0, 0.5);
    color: #fff;
    padding: 20px;
    transition: transform 0.3s, box-shadow 0.3s;
    transform: translateX(100%);
}
  
.profile-sidebar.active {
    transform: translateX(0);
    box-shadow: -10px 0 20px rgba(0, 0, 0, 0.2);
}
  
.sidebar-content {
/* 侧边栏内容样式 */
}
.profile-card {
    position: absolute;
    top: 55%;
    left: 50%;
    transform: translate(-50%, -50%);
    transition: transform 0.3s, left 1s;
    perspective: 1000px;
    cursor: pointer;
  }
.enlarged {
    transform: scale(3);
    padding:6px;
}
.flipped {
animation-name: flip;
animation-duration: 1s; /* 动画持续1秒 */
animation-timing-function: linear;
animation-iteration-count: 1; /* 动画重复两次 */
left: 20.75rem; /* 资料卡的新位置 */
}
.moveToLeft {
  animation: moveToLeft 0.5s forwards;
}
@keyframes flip {
    0% {
        transform: translate(-50%, -50%) rotateY(0);
    }
    50% {
        transform: translate(-50%, -50%) rotateY(180deg);
    }
    100% {
        transform: translate(-50%, -50%) rotateY(360deg);
    }
}
  
  .profile-card:hover {
    transform: translate(-50%, -50%) scale(1.03); /* 鼠标移上去时，将资料卡放大到原始大小的1.1倍，并保持居中 */
  }
  
</style>