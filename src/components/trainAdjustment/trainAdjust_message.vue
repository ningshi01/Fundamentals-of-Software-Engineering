<template>
    <div class="mycon">
        <div class="blur-background"></div>
        <fornav msg1=车次调控 msg2=主页 msg3=个人信息 msg4=列车信息 msg5=设置
        href1=#/trainAdjust1 href2=#/trainAdjust2 href3=#/trainAdjust3 href4=#/trainAdjust4 href5=#/ ></fornav>
        <div class="hcon">
            <img src="../../assets/cat.png" alt="" class="flg">
            <img src="../../assets/logo.png" alt="" class="lg">
            <br><h1>个人信息</h1><br>
        </div>
        <div class="table1">
            <div class="profile-card" :class="{ flipped: isFlipped, moveToLeft: moveToRight }" @click="flipCard">
                <div class="card-header">
                    <div :class="{ pic: true, enlarged: !isFlipped }">
                        <img src="../../assets/imgs/head.jpeg" alt="">
                    </div>
                    <div v-if="isFlipped" class="name">{{ AdminName }}</div>
                    <div v-if="isFlipped" class="desc">Railway Administrator(Admin)</div>
                    <div v-if="isFlipped" class="sm"></div>
                </div>
                <div class="card-footer">
                    <div class="numbers">
                        <div class="item">
                            <span>已登录</span>状态
                        </div>
                        <div class="border"></div>
                        <div class="item">
                            <span>铁路系统员</span>权限
                        </div>
                    </div>
                </div>
            </div>
            <div class="profile-sidebar" :class="{ active: isFlipped }">
                <el-card shadow="hover" :style="{ height: '100%',width: '100%', margin: '0 auto' }" class="card-content" v-if="isFlipped">
                    <div class="profile-info">
                      <div class="info-row">
                        <span class="label">用户名:</span>
                        <span class="value">{{ username }}</span>
                      </div>
                      <div class="info-row">
                        <span class="label">权限:</span>
                        <span class="value">{{ permission }}</span>
                      </div>
                      <div class="info-row">
                        <span class="label">年龄:</span>
                        <span class="value">{{ age }}</span>
                      </div>
                      <div class="info-row">
                        <span class="label">邮箱:</span>
                        <span class="value">{{ email }}</span>
                      </div>
                    </div>
                  </el-card>
            </div>

        
        </div>
    </div>
</template>

<script>
import fornav from './fornav.vue';
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
    name: "My_trainAdjust_message",
    data(){
        return{
            username: 'WX2',
            permission: 'Admin',
            age: 19,
            email: 'buaa2@buaa.com',
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

<style>
@import url("https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&display=swap");
.label {
    margin-right: 10px;
    font-weight: bold;
    color:cornflowerblue;
  }
  
.value {
    font-family:Georgia;
    font-size: 30px;
    color: rgba(16, 45, 98, 0.758);
}   
</style>

<style scoped>
@import '../../assets/css/forMessage.css';
@import 'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.14.0/css/all.min.css';

.table1{
    padding: 0 0rem 0 25rem;
    text-align: center;
    display: flex;
    align-items: stretch;
}
  
.card-content {
    background-image: url("https://webstatic.mihoyo.com/upload/op-public/2023/05/30/e70210b1e339914842f4a19f6845abf7_237256773028712797.png"),url('https://webstatic.mihoyo.com/upload/op-public/2022/08/10/706e1d017fa0c693609803d9c82014a9_6896184362091703764.png');
    
    /*background-image: url('https://webstatic.mihoyo.com/upload/op-public/2022/08/10/706e1d017fa0c693609803d9c82014a9_6896184362091703764.png');*/
    background-size:cover,auto;
    background-position: center;
    /*background-color: rgba(166, 205, 211, 0.7);*/
    opacity: 0.9;
  }

.profile-sidebar {
    position: absolute;
    top: 25%;
    right: 0;
    bottom: 25%;
    width: 60%;
    background-color: rgba(0, 0, 0, 0.5);
    color: #fff;
    padding: 10px;
    transition: transform 0.3s, box-shadow 0.3s;
    transform: translateX(100%);
    
    display: flex;
    justify-content: center;
    align-items: center;
    height: 56vh;
    border-radius: 10px; /* 添加圆角 */
}
  
.profile-sidebar.active {
    transform: translateX(0);
    box-shadow: -10px 0 20px rgba(0, 0, 0, 0.2);
}
  

.info-row {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 20px;
    font-size: 18px;
    line-height: 1.5;
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