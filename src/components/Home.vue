<!-- eslint-disable vue/multi-word-component-names -->
<template>
    <el-container class="home-container">
      <!--  头部 -->
      <el-header>
        <div>
          <img src="" alt="">
          <span>MewTrain MewTrain MewTrain MewTrain </span>
        </div>
        <HeadItems></HeadItems>
      </el-header>
      <!-- 页面主体 -->
      <el-container>
        <!-- 左侧导航 或许可以考虑实现伸缩 -->
        <el-aside width="200px">
        <el-menu
        default-active="1"
        class="el-menu-vertical-demo"
        @open="handleOpen"
        @close="handleClose"
        router="true">
        <el-menu-item index="WELCOME">
          <template #title>
            <el-icon><location /></el-icon>
            <span class="ItemName">首页</span>
          </template> 
        </el-menu-item>
        <el-menu-item index="TicketInquiry">
          <el-icon><document /></el-icon>
          <span class="ItemName">列车信息查询</span>
        </el-menu-item>
        <el-sub-menu index="_">
          <template #title>
            <el-icon>
              <icon-menu />
            </el-icon>
            <span class="ItemName">订单信息</span>
          </template >
          <el-menu-item-group>
            <el-menu-item index="HistoryOrders" class="ItemName">全部订单</el-menu-item>
            <el-menu-item index="NoTripOrderList" class="ItemName">未出行订单</el-menu-item>
            <el-menu-item index="NoPayOrderList" class="ItemName">未支付订单</el-menu-item>
          </el-menu-item-group>
        </el-sub-menu>
        <el-sub-menu index="">
          <template #title>
            <el-icon><location /></el-icon>
            <span class="ItemName">管理员界面</span>
          </template>
          <el-menu-item-group>
            <el-menu-item index="mesdeal1" class="ItemName">系统管理员</el-menu-item>
            <el-menu-item index="trainAdjust1" class="ItemName">铁路系统员</el-menu-item>
          </el-menu-item-group>
        </el-sub-menu>
      </el-menu>
        </el-aside>
        <!-- 右侧内容主体 -->
        <el-main>
          <!-- 路由占位 -->
          <router-view></router-view>
        </el-main>
      </el-container>
    </el-container>
</template>
<script>
import HeadItems from './self/HeadItems.vue'
import {
  Menu as IconMenu,
} from '@element-plus/icons-vue'
export default{
  methods:{
    logout(){
        window.sessionStorage.clear()
        this.$router.push({name: 'Login'})
    }
  },
  components:{
    HeadItems,
    IconMenu
  }
}
</script>
<style lang="less" scoped>
  .ItemName{
    color: white;
  }
  .el-menu-vertical-demo {
    --text-color: white;
    background-color: #373d41;
    --text-color: white;
  }
  .home-container{
  height: 100%;
}
  .LogoutButton{
  align-items: center;
}
  .el-menu-item-group
  {
    background-color: #373d41;
  }
  .el-header{
    color: #ffff;
    align-items: right;
    padding-left: 0;
    display: flex;
    justify-content: space-between;
    width: 100;
    background-color: #373d41;
    font-size: 20px;
    > div{
      display: flex;
      align-items: center;
      span{
        margin-left :15px ;
      }
    }
    
  }
  
  .el-aside {
    background-color: #333744;
    color: #333;
    text-align: center;
    line-height: 200px;
  }
  
  .el-main {
    background-color: #EAEDF1;
    color: #333;
    text-align: center;
    line-height: 160px;
  }
  
  body > .el-container {
    margin-bottom: 40px;
  }
  

</style>