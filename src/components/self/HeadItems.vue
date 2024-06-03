<template>
    <el-dropdown @command="handleCommand">
      <span class="el-dropdown-link">
        <Head></Head>
      </span>
      <template #dropdown>
        <el-dropdown-menu >
          <el-dropdown-item command="historyOrders">历史订单</el-dropdown-item>
          <el-dropdown-item command="selfCenter">个人中心</el-dropdown-item>
          <el-dropdown-item command="recharge">充值</el-dropdown-item>
          <el-dropdown-item divided command="logout">退出登录</el-dropdown-item>
        </el-dropdown-menu>
      </template>
    </el-dropdown>
  </template>
  
<script>
    import Head from './Head'
    import { ArrowDown } from '@element-plus/icons-vue'
    import { mapMutations } from "vuex";
    export default{
        name:'HeadItems',
        components:{
            // eslint-disable-next-line vue/no-unused-components
            ArrowDown,
            Head
        },
        methods:{
          ...mapMutations(["setToken"]),
          ...mapMutations(["setLogin"]),
            handleCommand(text){
                if(text==='historyOrders'){
                    this.$router.push({
                        name:'historyOrders'
                    })
                }
                else if(text==='selfCenter'){
                    this.$router.push({
                        name:'selfCenter'
                    })
                }
                else if(text==='recharge'){
                    this.$router.push({
                        name:'recharge'
                    })
                }
                else if(text==='logout'){
                    this.setToken(null)
                    this.setLogin(false)
                    window.sessionStorage.clear()
                    this.$router.push('/Login')
                }
            }
        }
    }
</script>
  <style scoped>
  .example-showcase .el-dropdown-link {
    cursor: pointer;
    color: var(--el-color-primary);
    display: flex;
    align-items: center;
  }
  </style>
  